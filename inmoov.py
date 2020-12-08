import Adafruit_PCA9685
import logging
import time
from servo import Servo



try:
    PWM = Adafruit_PCA9685.PCA9685()
    
    time.sleep(1)
    
except OSError as error:
    LOG_STRING = "failed to initialise the servo driver board (Adafruit PCA9685)"
    logging.error(LOG_STRING)

    DO_NOT_USE_PCA_DRIVER = True
    PWM = ""
    
else: 
    DO_NOT_USE_PCA_DRIVER = False
    

servo_min = 150
servo_max = 600
SLEEP_COUNT = 0.05

try:
    if not DO_NOT_USE_PCA_DRIVER:
        PWM.set_pwm_freq(60)
        time.sleep(1)
    else:
        logging.warning("DO NOT USE PCA DRIVER value is true, so not actually setting the frequency")
except ValueError as error:
    LOG_STRING = "failed to set the pwm frequency, " + error
    logging.error(LOG_STRING)
    
def set_servo_pulse(channel, pulse):
    if 0 <= channel <= 15 and \
       type(channel) is int and \
       pulse <= 4096 and \
       pusel >= 0:
        pulse_length = 1000000
        pulse_length //=60
        logging.info('{0}us per period'.format(pulse_lenth))
        pulse_length //=4096
        logging.info('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        if DO_NOT_USE_PCA_DRIVER:
            logging.warning("PCA9685 driver not loaded, so only pretending to set servo")
        else:
        
            try:
                PWM.set_pwm(channel, 0, pulse)
            except:
                logging.warning("Failed to set pwm - did the driver load?")
            
        return True
    print("channel less than 0 or greater than 15, or not an integer, \
    or pulse is grater than 4096:", channel, pulse)
    
    return False


class InMoov_head():
    
    __name = "Sonny"
    __eye_angle = 90
    __eye_tilt = 90

    def __init__(self):

        EYE_CHANNEL = 0
        EYE_TILT_CHANNEL = 1
        JAW_CHANNEL = 2
        self.__eyes = Servo("eye_angle", channel=EYE_CHANNEL, min_angle=80, max_angle=100)
        self.__eye_tilt = Servo("eye_tilt", channel=EYE_TILT_CHANNEL, min_angle=80, max_angle=100)
        self.__jaw = Servo("jaw", channel=JAW_CHANNEL,min_angle=0,max_angle=30)

        # set the servos to the middle position (between the min and max value)
        self.__eyes.default()
        self.__eye_tilt.default()
        self.__jaw.default()

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        
    @property    
    def eye_angle(self):
        return self.__eyes.angle
    
    @eye_angle.setter
    def eye_angle(self, value):
        self.__eyes.angle = value

    @property
    def jaw(self):
        return self.__jaw.angle
        
    @jaw.setter
    def jaw(self, value):
        self.__jaw.angle = value
    
    @property
    def eye_tilt(self):
        return self.__eye_tilt.angle

    @eye_tilt.setter
    def eye_tilt(self, value):
        self.__eye_tilt.angle = value

def main():
    Sonny = InMoov_head()
    Sonny.eye_angle = 80
    time.sleep(0.2)
    Sonny.eye_angle = 100
    time.sleep(0.2)
    Sonny.eye_angle = 90

if name == __main__:
    main()    