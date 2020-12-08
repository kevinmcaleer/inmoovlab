import logging

class Servo():
    __min_angle = 0
    __max_angle = 180
    __name = "servo"
    __current_angle = 90
    __channel = 0
    
    def __init__(self, channel, min_angle, max_angle,name=None):
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
            
            try:
                PWM.set_pwm(self.__channel, self.__channel, pulse)
            except:
                logging.warning("PWM failed to set, was driver loaded?")
        
    def default(self):
        self.angle = self.__max_angle - self.__min_angle