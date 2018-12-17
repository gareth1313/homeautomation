import RPi.GPIO as GPIO
import time
import os 

LedPin = 35    # pin11
pir = 40                                          #Associate pin 26 to pir
def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led
  GPIO.setwarnings(False)
  GPIO.setup(pir, GPIO.IN)                          #Set pin as GPIO in

print "Waiting for sensor to settle"
time.sleep(2)                                     #Waiting 2 seconds for the sensor to initiate
print "Detecting motion"  
  
def blink():
   while True:
      if GPIO.input(pir):                            #Check whether pir is HIGH
         print "Motion Detected!"
         os.system('fswebcam -r 1280x720 -S 3 --jpeg 50 --save /home/pi/webcam/%H%M%S.jpg') # uses Fswebcam to take picture  
         GPIO.output(LedPin, GPIO.HIGH)  # led on
         time.sleep(1)
         GPIO.output(LedPin, GPIO.LOW) # led off
         time.sleep(1)
#   	time.sleep(0.1)                                #While loop delay should be less than detection(hardware) delay

def destroy():
  GPIO.output(LedPin, GPIO.LOW)   # led off
  GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    blink()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
