# Available Pins: 11,13,15,29,31,37,36,32,28,26,24,22,18,16
import RPi.GPIO as GPIO
import time
import cv2
import datetime
#creating a camera object using opencv with default camera port of raspberrypi 

'''
Hardware used:
Nema 17 Stepper motor
Raspberry Pi
OV5640 Raspberry Pi 5MP Camera Module
3V3 to 5V Voltage translator circuit
A4988 Stepper Motor Driver
Microscope Brightfield Light Source
'''
#Initalizing rpi gpio pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW) # Dir pin x- dir motor
GPIO.setup(18,GPIO.OUT,initial=GPIO.LOW) # Step Pin x- dir motor
GPIO.setup(22,GPIO.OUT,initial=GPIO.LOW) # Dir pin y-dir motor
GPIO.setup(24,GPIO.OUT,initial=GPIO.LOW) # Step pin y-dir motor
GPIO.setup(13,GPIO.OUT,initial=GPIO.LOW) # Dir pin z-dir motor
GPIO.setup(31,GPIO.OUT,initial=GPIO.LOW) # Step pin z-dir motor

GPIO.setup(11,GPIO.OUT,initial=GPIO.HIGH) # Enable bar pin 8 of shield => Initially the motor is not enabled
GPIO.setup(38,GPIO.OUT,initial=GPIO.HIGH) # Enable bar pin for Y motor
GPIO.setup(40,GPIO.OUT,initial=GPIO.HIGH) # Enable bar pin for Z motor

#the below fuction takes previous positions and current positions.It computes number of steps required to move to the specified location.This function calls x,y movement functions accordingly
def hardware_action(x_prev,y_prev,z_prev,x_curr,y_curr,z_curr):
    print("Zoom Lens motor action!")
    #The full step resolution of stepper motor is 126um.(8mm pitch and 200 steps per revolution)
    stepconst=126
    
    print("prevx = ",x_prev," prevy = ",y_prev)
    xsteps =int((x_curr-x_prev)*1000/(stepconst))
    ysteps = int((y_curr-y_prev)*1000/(stepconst))
    print("xsteps ",xsteps," ysteps ",ysteps)
    if(xsteps<0):
        xsteps = -xsteps
        forward(xsteps)
    else:
        backward(xsteps)

    if(ysteps<0):
        ysteps = -ysteps
        upward(ysteps)
    else:
        downward(ysteps)
    return capture()
    #GPIO.cleanup()
            

def forward(steps):
    GPIO.output(11,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    for i in range(0,steps):
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.02)
    print("FORWARD MOVEMENT ",steps," STEPS")
    GPIO.output(11,GPIO.HIGH)
def backward(steps):
    GPIO.output(11,GPIO.LOW)
    GPIO.output(16,GPIO.HIGH)
    for i in range(0,steps):
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.02)
    print("BACKWARD MOVEMENT ",steps," STEPS")
    GPIO.output(11,GPIO.HIGH)
def upward(steps):
    GPIO.output(11,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
    for i in range(0,steps):
        GPIO.output(24,GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(24,GPIO.LOW)
        time.sleep(0.02)
    print("UPWARD MOVEMENT ",steps," STEPS")
    GPIO.output(11,GPIO.HIGH)
def downward(steps):
    GPIO.output(11,GPIO.LOW)
    GPIO.output(22,GPIO.HIGH)
    for i in range(0,steps):
        GPIO.output(24,GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(24,GPIO.LOW)
        time.sleep(0.02)
    print("DOWNWARD MOVEMENT ",steps," STEPS")
    GPIO.output(11,GPIO.HIGH)
def zplus(zoom_steps):
    GPIO.output(11,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    for i in range(0,zoom_steps):
        GPIO.output(31,GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(31,GPIO.LOW)
        time.sleep(0.02)
    print("LENS CHANGED TO ZOOM LEVEL : ",zoom_steps)
    GPIO.output(11,GPIO.HIGH)

def zminus(zoom_steps):
    GPIO.output(11,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    for i in range(0,zoom_steps):
        GPIO.output(31,GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(31,GPIO.LOW)
        time.sleep(0.02)
    print("LENS CHANGED TO ZOOM LEVEL : ",zoom_steps)
    GPIO.output(11,GPIO.HIGH)
#Testing code    
#print("Code is without errors and syntax issues")
#forward(20)
#backward(20)
#downward(20)
#upward(20)
#zplus(5)
#zminus(5)

#zplus(22)
#zminus(11)
def capture():
    cam = cv2.VideoCapture(0)
    time.sleep(0.2)
    ok,image = cam.read()
    #cv2.imshow("frame",image)
    #cv2.waitKey(0)
    ts=time.time()
    st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    cv2.imwrite("/home/pi/Desktop/CA-MICROSCOPE/Code-Challange/Digital_Microscope/static/images/image"+st+".png",image)
    time.sleep(0.2)
    del cam
    return st
