#SOPHIA INTRODUCTION TO CS ASSIGNMENT MORSECODE
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

def dot():
    GPIO.output(11, True)
    time.sleep(0.2)
    GPIO.output(11, False)
    time.sleep(0.2)

def dash():
    GPIO.output(11, True)
    time.sleep(0.5)
    GPIO.output(11, False)
    time.sleep(0.2)
def space():
    time.sleep(0.5)
       
morse_code = dict() #dictionary
morse_code = {
    'H':'....',
    'E':'.',
    'L':'.-..',
    'O':'---',
    'W':'.--',
    'R':'.-.',
    'D':'-..',
    ' ':' '}

greetings = 'hello world'
for letters in greetings.upper():
    key = morse_code[letters] #call each key from the dictionary
    for value in key: #goes through each value of the key
        if value == '.':
            dot()
        elif value == '-':
            dash()
        else:
            space()
