import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GP_TRIGGER = 18
GP_ECHO = 24

GPIO.setup(GP_TRIGGER, GPIO.OUT)
GPIO.setup(GP_ECHO, GPIO.IN)

def distance():
    GPIO.output(GP_TRIGGER, True)
    
    time.sleep(0.00001)
    GPIO.output(GP_TRIGGER, False)
    
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GP_ECHO) == 0:
        StartTime = time.time()
        
    while GPIO.input(GP_ECHO) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    distance = TimeElapsed * 17150 
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print(str(dist) + 'cm')
            
    except KeyboardInterrupt:
        print('Stopped')
        GPIO.cleanup()