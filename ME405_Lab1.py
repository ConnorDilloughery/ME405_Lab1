import pyb
import time
import motorDriver
import encoder


class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several pin parameters)
        """
        self.Pin1 = pyb.Pin(in1pin, pyb.Pin.OUT_PP)
        self.Pin2 = pyb.Pin(in2pin, pyb.Pin.OUT_PP)
        self.PinENA = pyb.Pin(en_pin, pyb.Pin.IN, pull = pyb.Pin.PULL_UP)#pyb.Pin.OPEN_DRAIN)
        self.Timer1= pyb.Timer(timer, freq=20000)
        self.Timer2= pyb.Timer(timer, freq=20000)
        self.TimChannel1=self.Timer1.channel(1, pyb.Timer.PWM, pin = self.Pin1)
        self.TimChannel2=self.Timer2.channel(2, pyb.Timer.PWM, pin = self.Pin2)
        
        
        #Setting the motor to 0 speed
        self.set_duty_cycle(10)
        
        print ("Creating a motor driver")

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        if level < 0 and level >=-100:
            self.TimChannel1.pulse_width_percent(-level)
            self.TimChannel2.pulse_width_percent(0)
            self.PinENA.value(True)
        elif level == 0:
            
            self.TimChannel1.pulse_width_percent(0)
            self.TimChannel2.pulse_width_percent(0)
            time.sleep(0.1)
            self.PinENA.value(True)
           
            
        elif level > 0 and level<=100:

            #Write code set the level in a postiive direction
            self.TimChannel1.pulse_width_percent(0)
            self.PinENA.value(False)
            self.TimChannel2.pulse_width_percent(level)
            time.sleep(.01)
            self.PinENA.value(True) 
        
        print (f"Setting duty cycle to {level}")


class Encoder:
    def __init__(self,PinIn1, PinIn2, timer):
        self.Count=0
        self.Previous =0
        self.Pin1 = pyb.Pin(PinIn1, pyb.Pin.IN)
        self.Pin2 = pyb.Pin(PinIn2, pyb.Pin.IN)
        self.ENC_Timer1= pyb.Timer(timer, prescaler=0, period =0xFFFF)
        self.ENC_Timer2= pyb.Timer(timer, prescaler=0, period =0xFFFF)
        self.ENC_CHANNEL1=self.ENC_Timer1.channel(1, pyb.Timer.ENC_AB, pin=self.Pin1)
        self.ENC_CHANNEL2=self.ENC_Timer1.channel(2, pyb.Timer.ENC_AB, pin=self.Pin2)
    
    def read(self):
        self.readd= self.ENC_Timer1.counter()
    #13255    
        self.delta= self.readd-self.Previous
        if self.delta> 0:
         if self.delta> (0xFFFF+1)/2:
          self.delta -= (0xFFFF+1)
          self.Count+= self.delta
          
         elif self.delta<(0xFFFF+1)/2:
          self.Count+= self.delta
          
        if self.delta< 0:
         if self.delta< -(0xFFFF+1)/2:
          self.delta += (0xFFFF+1)
          self.Count-= self.delta
          
         elif self.delta>-(0xFFFF+1)/2:
          self.Count+= self.delta
          
        self.Previous= self.readd        
        return self.Count

    def zero(self):
     self.Count=0


def main():
     EN_PIN= 'PC1'
     IN1= 'PA0'
     IN2= 'PA1'
     TIMER=5;
     ENC1= 'PC6'
     ENC2= 'PC7'
     ENCT= 8
     Motor1= MotorDriver(EN_PIN, IN1, IN2, TIMER)
     Motor1.set_duty_cycle(-60)
     Motor1E= Encoder(ENC1, ENC2, ENCT)
     while True:
         time.sleep(0.01)
         print("count", Motor1E.read())

if __name__ == "__main__":
    main()
