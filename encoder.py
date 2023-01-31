import pyb

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
     
#if __name__== "__main__":
#  EN_PIN= 'PC1'
#  IN1= 'PA0'
#  IN2= 'PA1'
#  TIMER=5;
#  ENC1= 'PC6'
#  ENC2= 'PC7'
#  ENCT= 8
#  #in1b A0 PA0
# #in2b A! PA 1
# #enb A4 pc1 
#  Motor1= MotorDriver(EN_PIN, IN1, IN2, TIMER)
#  Motor1.set_duty_cycle(50)
#  Motor1E= Encoder(ENC1, ENC2, ENCT)
#  while True:
#      time.sleep(0.01)
#      print("count", Motor1E.read())
#      if Motor1E.read()>70000:
#          Motor1E.zero()     