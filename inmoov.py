import Adafruit_PCA9685
import logging
import time
from servo import Servo



try:
    PWM = Adafruit_PCA9685.PCA9685()
    
    time.sleep(1)
    DO_NOT_USE_PCA_DRIVER = False
    
except OSError as error:
    LOG_STRING = "failed to initialise the servo driver board (Adafruit PCA9685)"
    logging.error(LOG_STRING)

    DO_NOT_USE_PCA_DRIVER = True
    PWM = ""
    
servo_min = 150
servo_max = 600
SLEEP_COUNT = 0.05

try:
    if not DO_NOT_USE_PCA_DRIVER:
        PWM.set_pwm_freq(60)
        time.sleep(0.1)
        loggin.info("PWM Set Successfully")
    else:
        logging.warning("DO NOT USE PCA DRIVER value is true, so not actually setting the frequency")
except ValueError as error:
    LOG_STRING = "failed to set the pwm frequency, " + error
    logging.error(LOG_STRING)
    
class InMoov_head():
    
    __name = "Sonny"
    __eye_angle = 90
    __eye_tilt = 90

    def __init__(self):

        EYE_CHANNEL = 0
        EYE_TILT_CHANNEL = 1
        JAW_CHANNEL = 2
        self.__eyes = Servo(name = "eye_angle", channel=EYE_CHANNEL, min_angle=80, max_angle=100)
        self.__eye_tilt = Servo(name = "eye_tilt", channel=EYE_TILT_CHANNEL, min_angle=80, max_angle=100)
        self.__jaw = Servo(name = "jaw", channel=JAW_CHANNEL,min_angle=0,max_angle=30)

        # set the servos to the middle position (between the min and max value)
        logging.info("setting eyes, eye tilt and jaw to default positions")
        self.__eyes.default()
        self.__eye_tilt.default()
        self.__jaw.default()

    @property
    def name(self):
        logging.info("def name: returning name %s", self.__name)
        return self.__name
    
    @name.setter
    def name(self, new_name):
        logging.info("def name: setting name %s", new_name)
        self.__name = new_name
        
    @property    
    def eye_angle(self):
        logging.info("def eye_angle: returning angle %s", self.__eyes.angle)
        return self.__eyes.angle
    
    @eye_angle.setter
    def eye_angle(self, value):
        logging.info("def eye_angle: setting eye angle to : %s", value)
        self.__eyes.angle = value

    @property
    def jaw(self):
        logging.info("def jaw: returning jaw %s", self.__jaw.angle)
        return self.__jaw.angle
        
    @jaw.setter
    def jaw(self, value):
        logging.info("def jaw: setting jaw %s", value)
        self.__jaw.angle = value
    
    @property
    def eye_tilt(self):
        logging.info("def eye_tilt: returning eye_tilt %s", self.__eye_tilt.angle)
        return self.__eye_tilt.angle

    @eye_tilt.setter
    def eye_tilt(self, value):
        logging.info("def eye_tilt: setting eye_tilt %s", value)
        self.__eye_tilt.angle = value

def main():
    
    Sonny = InMoov_head()
    print("setting eye angle to 80")
    Sonny.eye_angle = 80
    time.sleep(0.2)

    print("setting eye angle to 100")
    Sonny.eye_angle = 100
    time.sleep(0.2)

    print("setting eye angle to 90")
    Sonny.eye_angle = 90

if __name__ == '__main__':
    main()    