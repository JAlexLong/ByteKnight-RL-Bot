# This file is for strategy

from util.objects import *
from util.routines import *


class ByteKnight(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        # set_intent tells the bot what it's trying to do
        if self.kickoff_flag:
            self.set_intent(kickoff())
            print("Kicking off...")

        # if ball is on their side of the field
        elif self.ball.location.y > 0:
            print("In front?")

        # default routine
        else:
            self.set_intent(magikarp())
