import rsk
import time
import math
from rsk import field_dimensions

# détail du fichier fct_alphabut
# fonction calc_alpha pour calculer l'angle balle but par rapport à l'axe X en sens trigo
# fonction prépa tir pour se placer à 10 cm de la balle :
# calcule x_prepa_tir et y_prepa_tir à placer dans le goto

# fonction tire cadre avec argument 'bot' pour le choix du robot... à utiliser ou à refaire...
# inclu la fonction prépa tire pour se caller à 0.1cm de la balle

# fonction garage_vert_1 et 2 argument (bot) indique le garage des robot1 et 2

with rsk.Client('172.16.0.100') as client:
    robot1 = client.robots['green'][1]
    robot2 = client.robots['green'][2]
    robot3 = client.robots['blue'][2]
    Long_terrain = field_dimensions.length
    larg_terrain = field_dimensions.width
    ypoteauvert1 = -field_dimensions.goal_width / 2
    xpoteauvert1 = (-field_dimensions.length / 2) + 0.1
    ypoteauvert2 = field_dimensions.goal_width / 2
    xpoteauvert2 = -field_dimensions.length / 2 + 0.1

    
   # calculer alpha - Angle balle / but par rapport à l'axe X
    def calc_alpha():

        # position robot but en X
        dist_balle_butX = Long_terrain/2 - client.ball[0]
        # position robot but en Y
        dist_balle_butY = client.ball[1]
        # angle robot but
        tanalpha = dist_balle_butY/dist_balle_butX
        global alpha
        alpha = math.degrees(math.atan(tanalpha))
        print("tanalpha =", tanalpha) 
        print("dist_balle_butX =", dist_balle_butX) 
        print("alpha =", alpha) 

    # Zones de garages de la team vert ( wait=False)
    def garage_vert_1(bot):
        client.robots['green'][bot].goto(-0.5, 0.5, 1.57)

    def garage_vert_2(bot):
        client.robots['green'][bot].goto(-0.5, 0.8, 1.57)

    # on la coordonée d'un point à 0,1 m de la balle sur la droite balle but.
    def prepa_tir():
        x_balle = client.ball[0]
        y_balle = client.ball[1]
        global x_prepa_tir
        global y_prepa_tir

        L_x = math.cos(math.radians(alpha)) * 0.2
        L_y = math.sin(math.radians(alpha)) * 0.2
        if client.ball[1] > 0:
            x_prepa_tir = x_balle - L_x
            y_prepa_tir = y_balle + L_y
        else: 
            x_prepa_tir = x_balle - L_x
            y_prepa_tir = y_balle + L_y

        print("x_prepa_tir =", x_prepa_tir) 
        print("x_balle = ", x_balle)
        print("y_balle = ", y_balle)
        print("L_y = ", L_y)
        print("y_prepa_tir =", y_prepa_tir) 
        print("alpha =", alpha) 

    def calc_avant_tir():
        calc_alpha()
        prepa_tir()

    def dep_avant_tir(bot):
        if client.ball[1] > 0:
            bot.goto((x_prepa_tir, y_prepa_tir, -math.radians(alpha)))
        else:
            bot.goto((x_prepa_tir, y_prepa_tir, -math.radians(alpha)))

   # garage_vert_1(robot1)
    # garage_vert_2(robot2)

    arrived1 = False
    arrived2 = False
    # aller aux points de départ
    #while (not arrived1) or (not arrived2):
        #arrived1 = robot1.goto((-0.2, 0 ,0), wait=False)
        #arrived2 = robot2.goto((-Long_terrain/2, 0 ,0), wait=False)
        #time.sleep(0.1)
    
    
    def test():
        calc_avant_tir()
        dep_avant_tir(robot2)
        time.sleep(1)
        #tir_cadre(robot1)

    def depart():
        arrived1 = False
        arrived2 = False
        while (not arrived1) or (not arrived2):
            arrived1 = robot2.goto((0, 0.2 ,0), wait=False)
            arrived2 = robot1.goto((0, -0.2 ,0), wait=False)
            time.sleep(0.1)

    def passe_but(): 
    # demander au robot2 d'aller aux buts
    # demander au robot 1 d'aller tirer 
       
        arrived1 = False
        arrived2 = False
        while (not arrived1) or (not arrived2):
            arrived1 = robot2.goto((0, 0.2 ,0), wait=False)
            arrived2 = robot1.goto((0, -0.2 ,0), wait=False)
            time.sleep(0.1)
        calc_avant_tir()
        calc_alpha()
        if client.ball[1] > 0:
            dep_avant_tir(robot2)
            robot2.goto((client.ball[0], client.ball[1]+0.18, -math.radians(alpha) - (3.14159265359 / 3)))
            robot2.goto((client.ball[0], client.ball[1]+0.08, -math.radians(alpha) - (3.14159265359 / 3)))
            robot2.kick(0.5)
        elif client.ball[1] < 0:
            dep_avant_tir(robot1)
            robot1.goto((client.ball[0], client.ball[1]-0.18, -math.radians(alpha) + (3.14159265359 / 3)))
            robot1.goto((client.ball[0], client.ball[1]-0.08, -math.radians(alpha) + (3.14159265359 / 3)))
            robot1.kick(0.5)

    def tir_apres_passe():
        calc_avant_tir()
        calc_alpha()
        if client.ball[1] < 0:
            dep_avant_tir(robot1)
            robot1.goto((client.ball[0]-0.05, client.ball[1]-0.05, -math.radians(alpha)))
            robot1.kick()
            time.sleep(1)
        elif client.ball[1] > 0:    
            dep_avant_tir(robot2)
            robot2.goto((client.ball[0]-0.05, client.ball[1]+0.05, -math.radians(alpha)))
            robot2.kick()
            time.sleep(1)
    
    def defense():
        arrived1 = False
        arrived2 = False
        while (not arrived1) or (not arrived2):
            arrived1 = robot2.goto((-0.2, 0.4 ,0), wait=False)
            arrived2 = robot1.goto((-0.2, -0.4 ,0), wait=False)
            time.sleep(0.1)
        if client.ball[1] > 0:
            arrived1 = False
            arrived2 = False
            while (not arrived1) or (not arrived2):
                arrived2 = robot2.goto((client.ball[0]-0.10, client.ball[1], 0), wait=False)
                arrived1 = robot1.goto((-0.8, 0, 0), wait=False)
                time.sleep(0.1)
            robot2.goto((client.ball[0]-0.08, client.ball[1], 0))
            robot2.kick(0.8)
        elif client.ball[1] < 0:
            arrived1 = False
            arrived2 = False
            while (not arrived1) or (not arrived2):
                arrived1 = robot2.goto((-0.8, 0, 0), wait=False)
                arrived2 = robot1.goto((client.ball[0]-0.10, client.ball[1], 0), wait=False)
                time.sleep(0.1)
            robot1.goto((client.ball[0]-0.08, client.ball[1], 0))
            robot1.kick(0.8)
    
    depart()

    # Loop that can't stop
    while True :
        # If robot have the ball, so run the program below.
        if client.ball is not None :

            if client.ball[0] > 0:

                # The robot give the ball to the second robot
                passe_but()

                # Wait 2.5 seconds
                time.sleep(1)

                # The robot try to goal
                tir_apres_passe()

                # Wait 3 seconds
                time.sleep(1)
            # Second condition to send robots to defence     
            elif client.ball[0] < 0:
                defense()
                time.sleep(0.1)