import logging
from logutils import *

_F = BraceMessage
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
        else:
            if value > self.__max_angle:
                logging.warning(_F("Servo Value to high: max angle is {self.__max_angle}, value supplied was {value}"))
            if value < self.__min_angle:
                logging.warning(_F("Servo Value to low: min angle is {self.__min_angle}, value supplied was {value}"))

    def default(self):
        middle = self.__max_angle - self.__min_angle
        self.angle = middle
        logging.info(_F("setting the angle to the middle position: {middle}"))

    @property
    def channel(self):
        logging.info(_F("channel is {self.__channel}"))
        return self.__channel
    
    @channel.setter
    def channel(self, value):
        if (value >= 0) and (value <=15):
                self.__channel = value 
                logging.info(_F("setting the channel to {value}"))
