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

with rsk.Client('10.10.10.2') as client:
    robot1 = client.robots['green'][1]
    robot2 = client.robots['green'][2]
    Long_terrain = field_dimensions.length
    larg_terrain = field_dimensions.width

    
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

    def action():

        # Mise en place 
        robot1.goto((-0.5, 0 ,0))

        arrived1 = False
        arrived2 = False
        # les robots se mettent en place en même temps
        while (not arrived1) or (not arrived2):
            arrived1 = robot1.goto((-0.2, 0 ,0), wait=False)
            arrived2 = robot2.goto((-Long_terrain, 0 ,0), wait=False)
            time.sleep(0.1)
    

        # robot1 va devant la balle 
        robot1.goto((client.ball[0]-0.1, client.ball[1], 0), wait=False)
        time.sleep(2)
        

    def tir_cadre(bot):
        
        if client.ball[1] > 0:
            calc_alpha()
            prepa_tir()
            bot.goto((x_prepa_tir, y_prepa_tir, -math.radians(alpha)))
            time.sleep(500)
            # bot.goto((client.ball[0]-0.06, client.ball[1]+0.06, -math.radians(alpha)))
        else:
            calc_alpha()
            prepa_tir()
            bot.goto((x_prepa_tir, y_prepa_tir, -math.radians(alpha)))
            time.sleep(500)
            bot.goto((client.ball[0]-0.04, client.ball[1]-0.08, -math.radians(alpha)))
        
        # et tire !!!!!!!!
        time.sleep(0.1)
        #robot1.kick()

    print(client.ball[0])
    print(client.ball[1])
    print(field_dimensions.length)
    
    