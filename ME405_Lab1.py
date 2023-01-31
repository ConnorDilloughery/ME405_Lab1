import pyb
import time
import motorDriver
import encoder
 


def main():
     EN_PIN= 'PC1'
     IN1= 'PA0'
     IN2= 'PA1'
     TIMER=5;
     ENC1= 'PC6'
     ENC2= 'PC7'
     ENCT= 8
     Motor1= motorDriver.MotorDriver(EN_PIN, IN1, IN2, TIMER)
     Motor1.set_duty_cycle(-60)
     Motor1E= encoder.Encoder(ENC1, ENC2, ENCT)
     while True:
         time.sleep(0.01)
         print("count", Motor1E.read())

if __name__ == "__main__":
    main()
