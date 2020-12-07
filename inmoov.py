import Adafruit_PCA9685
import logging
import time


try:
    PWM = Adafruit_PCA9685.PCA9685()
    
    time.sleep(1)
    
except OSError as error:
    LOG_STRING = "failed to initialise the servo driver board (Adafruit PCA9685)"
    logging.error(LOG_STRING)
    
servo_min = 150
servo_max = 600
SLEEP_COUNT = 0.05

try:
    PWM.set_pwm_freq(60)
    time.sleep(1)
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
        try:
            PWM.set_pwm(channel, 0, pulse)
        except:
            logging.warning("Failed to set pwm - did the driver load?")
            
        return True
    print("channel less than 0 or greater than 15, or not an integer, \
    or pulse is grater than 4096:", channel, pulse)
    
    return False

class Servo():
    __min_angle = 0
    __max_angle = 180
    __name = "servo"
    __current_angle = 90
    __channel = 0
    
    def __init__(self, name=False, channel, min_angle, max_angle):
        self.__name = name
        self.__channel = channel
        self.__min_angle = min_angle
        self.__max_angle = max_angle

    @property
    def angle(self):
        return self.__current_angle

    @angle.setter
    def angle(self, value):
        if (value >= self.__min_angle) and (value <= self.__max_angle):
            self.__current_angle = value
            
            mapmax = self.__max_angle - self.min_angle
            percentage = (float(value) / 180) * 100
            pulse = int(((float(mapmax) / 100) * float(percentage)) + self.__min_angle)
            PWM.set_pwm(self.__channel, self.__channel, pulse)
        
class inMoov_head():
    
    __name = "Sonny"
    __eye_angle = 90
    __eye_tilt = 90

    __servos = {}

    def __init__(self):
        eyes = Servo(name)
        

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        
    @property    
    def eye_angle(self):
        return self.__eye_angle
    
    @eye_angle.setter
    def eye_angle(self, new_angle):
        self.__eye_angle = new_angle
        
    
    