import rsk
from rsk import field_dimensions
import time
import math
from alphabut import *


with rsk.Client(host='10.10.10.2', key='') as client:

    ypoteauvert1 = -field_dimensions.goal_width / 2
    xpoteauvert1 = (-field_dimensions.length / 2) + 0.1
    ypoteauvert2 = field_dimensions.goal_width / 2
    xpoteauvert2 = -field_dimensions.length / 2 + 0.1
    
    # calculer alpha pour le robot1
    def alpharobot1():

        longueurt = field_dimensions.length
        largeurt = field_dimensions.goal_width

        # position robot but en X
        robot1_butX = longueurt/2 - client.green1[0]
        # position robot but en Y
        robot1_butY = client.green1[1]
        # angle robot but
        tanalpha = robot1_butY/robot1_butX
        global alpha
        alpha = math.atan(tanalpha)

    def depart1(choixrobot):
        client.robots['green'][choixrobot].goto((-0.5, 0.35, 0), wait=False)

    def aubut(choixrobot):
        client.robots['green'][choixrobot].goto(client.ball[0]-0.08, client.ball[1], alpha)
   
    def kick(choixrobot):
        client.robots['green'][choixrobot].kick()
   
    def action():
        kick(1)
        depart1(1)
        aubut(1)
        kick(1)
    
    def garage1(bot):
        client.robots['green'][bot].goto((-0.5, 0.7, -1.57), wait=False)

    def garage2(bot):
        client.robots['green'][bot].goto((-0.5, -0.7, 1.57), wait=False)

    def va2(x , y, a):
        client.robots['green'][2].goto((x,y,a), wait=False)


    

    def au_goal():
        va2(xpoteauvert1, ypoteauvert1, 0)
        

    
    def team_depart():
        arrived = False
        while not arrived:
            robot_1_arrived = garage1(1)
            robot_2_arrived = garage2(2)
            arrived = robot_1_arrived and robot_2_arrived


    def action_1():
        arriveda = False
        while not arriveda:
            robot_1_arrived = depart1(1)
            robot_2_arrived = au_goal()
            arriveda = robot_1_arrived and robot_2_arrived
    
    def test():
            arrived = False
            while not arrived:
                robot_1_arrived = client.green1.goto((-0.5, 0.5, 1), wait=False)
                robot_2_arrived = client.green2.goto((-0.5, -0.5, -1), wait=False)
                arrived = robot_1_arrived and robot_2_arrived
    
    def test2():
            arrived = False
            while not arrived:
                robot_1_arrived = client.green1.goto((0.2, 0.3, 0.), wait=False)
                robot_2_arrived = client.green2.goto((0.2, -0.3, 0.), wait=False)
                arrived = robot_1_arrived and robot_2_arrived
    
    def test3():
        arrived1 = False
        arrived2 = False
        # les robots se mettent en place en même temps
        while (not arrived1) or (not arrived2):
            arrived1 = client.green1.goto((-0.2, 0 ,0), wait=False)
            arrived2 = client.green2.goto((-field_dimensions.length/2, 0 ,0), wait=False)
            time.sleep(0.1)

    
    test()
    test2()
    tir_cadre()
    #robot_1_arrived = client.green1.goto((0.2, 0.3, 0.))
    #robot_2_arrived = client.green2.goto((0.2, -0.3, 0.))
    #team_depart()
    #action_1()

    #garage1(1)
    #depart1(1)
    #kick(1)
    #action()

    #client.robots['blue'][1].kick()
    
    
    



# 0.54, -0.2



