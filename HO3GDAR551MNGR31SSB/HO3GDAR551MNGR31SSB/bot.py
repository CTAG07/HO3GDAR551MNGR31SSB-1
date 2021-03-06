from tools import  *
from objects import *
from routines import *


#This file is for strategy

class ExampleBot(GoslingAgent):
    def __init__(self):
        print('ready')

    '''
    def get_output(agent, self, packet: GameTickPacket) -> SimpleControllerState:
        
        controls = SimpleControllerState()

        ball_x_right = agent.ball.location.x+94
        ball_x_left = agent.ball.location.x-94
        ball_y_front = agent.ball.location.y+94
        ball_y_back = agent.ball.location.y-94
        ball_z_up = agent.ball.location.z+94
        ball_z_down = agent.ball.location.z-94


        agent.renderer.begin_rendering()
        agent.renderer.draw_rect_2d(20, 20, 200, 200, True, self.renderer.black())
        agent.renderer.end_rendering()

        return controls
    '''

    def run(agent):
        
        if len(agent.stack) < 1:
            if agent.kickoff_flag:
                agent.push(omen_kickoff())
            else:
                relative_target = agent.ball.location - agent.me.location
                local_target = agent.me.local(relative_target)
                defaultPD(agent, local_target)
                defaultThrottle(agent, 2300)


