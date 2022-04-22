import rsk
from rsk import field_dimensions
import time
import math
from fct_alphabut_v2 import *

# détail du fichier fct_alphabut
    # fonction calc_alpha() pour calculer l'angle balle but par rapport à l'axe X en sens trigo

    # fonction prepa_tir() pour se placer à 10 cm de la balle
    # calcule x_prepa_tir et y_prepa_tir à placer dans le goto

    # fonction tire_cadre(bot) avec argument 'bot' pour le choix du robot... à utiliser ou à refaire...
    # inclu la fonction prépa tire pour se caller à 0.1cm de la balle

    # fonction garage_vert_1(bot) et 2 argument (bot) indique le garage des robot1 et 2

# time.sleep(0.1) faire une pause
# robot1.kick() tirer

# les robots se mettent en place en même temps
# arrived1 = False
# arrived2 = False
# while (not arrived1) or (not arrived2):
    # arrived1 = robot1.goto((-0.2, 0 ,0), wait=False)
    # arrived2 = robot2.goto((-Long_terrain/2, 0 ,0), wait=False)
    # time.sleep(0.1)

# afficher les coordonnées de la balle
# print(client.ball[0])
# print(client.ball[1])



with rsk.Client(host='10.10.10.2', key='') as client:

    robot1 = client.robots['green'][1]
    robot2 = client.robots['green'][2]
    Long_terrain = field_dimensions.length
    larg_terrain = field_dimensions.width
    ypoteauvert1 = -field_dimensions.goal_width / 2
    xpoteauvert1 = (-field_dimensions.length / 2) + 0.1
    ypoteauvert2 = field_dimensions.goal_width / 2
    xpoteauvert2 = -field_dimensions.length / 2 + 0.1
    
    # garage_vert_1(robot1)
    # garage_vert_2(robot2)
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

    while True:
        test()

    def passe_but(): 
    # demander au robot2 d'aller aux buts
    # demander au robot 1 d'aller tirer 
       
        arrived1 = False
        arrived2 = False
        while (not arrived1) or (not arrived2):
            arrived1 = robot2.goto((-0.5, 0 ,0), wait=False)
            arrived2 = robot1.goto((-0.5, -0.4 ,0), wait=False)
            time.sleep(0.1)
        calc_avant_tir()
        calc_alpha()
        dep_avant_tir(robot2)
        robot2.goto((client.ball[0], client.ball[1]+0.2, -math.radians(alpha) - (3.14159265359 / 3)))
        robot2.goto((client.ball[0], client.ball[1]+0.1, -math.radians(alpha) - (3.14159265359 / 3)))
        robot2.kick(0.7)

    def tir_apres_passe():
        calc_avant_tir()
        calc_alpha()
        dep_avant_tir(robot1)
        robot1.goto((client.ball[0]-0.05, client.ball[1]+0.05, -math.radians(alpha)))
        robot1.kick()
        time.sleep(1)

    #passe_but()
   # time.sleep(3)
    #tir_apres_passe()