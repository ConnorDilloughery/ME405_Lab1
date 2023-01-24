import pyb
import time
Count = 0

def main():
    pinPA5 = pyb.Pin (pyb.Pin.board.PA5, pyb.Pin.OUT_PP)
    pinPA9 = pyb.Pin (pyb.Pin.board.PA9, pyb.Pin.OUT_PP)
    tim1 = pyb.Timer (1, freq=20000)
    tim2 = pyb.Timer (2, freq=20000)
    ch1 = tim2.channel (1, pyb.Timer.ENC_AB, pin=pinPA5)
    ch2 = tim1.channel (2, pyb.Timer.ENC_AB, pin=pinPA9)
    #print(tim2.counter())

    pinC6 = pyb.Pin (pyb.Pin.board.PC6, pyb.Pin.IN)
    enc_timer1 = pyb.Timer (8, prescaler=0, period =0xFFFF)
    enc_channel1 = enc_timer1.channel (1, pyb.Timer.ENC_AB, pin = pinC6)
        
    pinC7 = pyb.Pin (pyb.Pin.board.PC7, pyb.Pin.IN)
    enc_timer2 = pyb.Timer (8, prescaler=0, period =0xFFFF)
    enc_channel2 = enc_timer2.channel (2, pyb.Timer.ENC_AB, pin = pinC7)

    while True:
        

        
        Count1 = enc_timer1.counter()
        Count2 = enc_timer2.counter()
        print("Count 1", Count1)
       # print("Count 2", Count2)
        
        time.sleep(0.1)
        


if __name__ == "__main__":
    main()
