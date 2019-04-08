from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from boxworld import thymio_world


class MySMClass(sm.SM):
    def __init__ (self):
        self.start_state = 0

    def get_next_values(self, state, ground):
        ground = ground.prox_ground.delta
        left = ground[0]
        right = ground[1]
        print(left,right)
        if state == 0 and ground[0]> 200 and ground[1]>200:
            return 0, io.Action(0, 0.2)
        elif state == 0 and ground[0]<200 and ground[1]< 200:
            return 0, io.Action(0,0.2)
        elif state==0 and ground[0]> 200 and ground[1]<200:
            return 1 , io.Action(0.1,0)
        elif state==0 and ground[0]< 200 and ground[1]>200:
            return 1 , io.Action(0.1,0)
        elif state==1 and ground[0]> 200 and ground[1]>200:
            return 0 , io.Action(0.0,0.2)
        elif state==1 and ground[0]< 200 and ground[1]<200:
            return 1 , io.Action(0.0,-0.2)
        elif state==1 and ground[0]> 200 and ground[1]<200:
            return 1 , io.Action(0.1,0.0)
        elif state==1 and ground[0]< 200 and ground[1]>200:
            return 1 , io.Action(0.1,0.0)
        
        #####################################

        # ground = inp.prox_ground.reflected
        # ground = inp.prox_ground.ambiant

       
        next_state = state
        return next_state, io.Action(fv=0.0, rv=0.0)  #Edit this part

    #########################################
    # Don't modify the code below.
    # this is to stop the state machine using
    # inputs from the robot
    #########################################
    def done(self, state):
        if state == 'halt':
            return True
        else:
            return False

MySM = MySMClass()

############################

m = ThymioSMReal(MySM) #thymio_world, scale=2)
try:
    m.start()
except KeyboardInterrupt:
    m.stop()
