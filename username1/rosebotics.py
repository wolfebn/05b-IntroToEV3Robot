"""
The python-ev3dev library tailored for Rose-Hulman.
"""

import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
import ev3dev
import ev3dev.auto
import ev3dev.helper

class LargeMotor(ev3.LargeMotor, ev3dev.helper.MotorMixin):
    def start(self):
        print('start')
        self.run_forever()

    def stop(self):
        print('stop this')
        super().stop()

    def hold(self):
        print('hold')

# ev3.LargeMotor
#
# ev3.MediumMotor
#
# ev3.Motor
#
# ev3.Sound
#
# Button
#
# Tone
#
# Song
#
# Note
