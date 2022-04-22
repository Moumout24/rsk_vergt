import rsk
import time
import math
from rsk import field_dimensions


with rsk.Client('10.10.10.2') as client:
    robot1 = client.robots['green'][1]
    robot2 = client.robots['green'][2]
    Long_terrain = field_dimensions.length
    larg_terrain = field_dimensions.width

   # un kick pour le fun  
    #client.robots['green'][1].kick()
    
   # calculer alpha pour le robot1 - Angle balle / but par rapport à l'axe X
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

    # Zones de garages en place au garage ( wait=False)
    def garage1(bot):
        client.robots['green'][bot].goto(0,0,0)

    def garage2(bot):
        client.robots['green'][bot].goto(-0.5, -0.7, 1.57)

    # while True:

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
        
        # choix du sens de rotation du robot
        #if robot1.position[1] > 0:
            #calc_alpha()
            #robot1.control(0., 0., -math.radians(alpha))
        #else:
            #calc_alpha()
            #robot1.control(0., 0., math.radians(alpha))

    def tir_cadre():
        
        if client.ball[1] > 0:
            calc_alpha()
            robot1.goto((client.ball[0]-0.10, client.ball[1]+0.10, -math.radians(alpha)+0.4))
            robot1.goto((client.ball[0]-0.06, client.ball[1]+0.06, -math.radians(alpha)))
        else:
            calc_alpha()
            robot1.goto((client.ball[0]-0.08, client.ball[1]-0.12, -math.radians(alpha)))
            robot1.goto((client.ball[0]-0.04, client.ball[1]-0.08, -math.radians(alpha)))
        
        # et tire !!!!!!!!
        time.sleep(0.1)
        #robot1.kick()

    print(client.ball[0])
    print(client.ball[1])
    print(field_dimensions.length)
    robot1.goto((0, 0 ,0))
    tir_cadre()
    time.sleep(2)
    robot1.goto((0, 0 ,0))
    tir_cadre()
    robot1.kick()
    