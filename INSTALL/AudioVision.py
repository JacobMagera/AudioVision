import os
os.system("sudo pigpiod") # Starts the pigpio library
from gpiozero import *
from time import sleep

buzzer = Buzzer(17)
button = Button(18)
trigPin = 23
echoPin = 24
sensor = DistanceSensor(echo = echoPin, trigger = trigPin, max_distance = 5)

def onButtonPressed():
    sensor.close()
    os.system("sudo shutdown -h now") # Turns off raspberry pi

def loop():
    button.when_pressed = onButtonPressed
    while True:
        print('Distance: ', sensor.distance * 100, 'cm')
        buzzer.on()
        sleep(0.05)
        buzzer.off()
        sleep(sensor.distance)


if __name__ == '__main__': # This is the entrance
    print('Program is starting...')
    loop()