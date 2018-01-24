import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)

morse = {'a': '*-', 'b': '-***', 'c': '-*-*', 'd': '-**', 'e': '*', 'f': '**-*',
        'g': '--*', 'h': '****', 'i': '**', 'j': '*---', 'k': '-*-', 'l': '*-**',
        'm': '--', 'n': '-*','o': '---', 'p': '*--*', 'q': '--*-', 'r': '*-*',
        's': '***', 't': '-', 'u': '**-', 'v': '***-', 'w': '*--', 'x': '-**-',
        'y': '-*--', 'z': '--**', ' ': '   ', '1': '*---', '2': '**---', '3':
        '***--', '4': '****-', '5': '*****', '6': '-****', '7': '--***', 
        '8': '---**', '9': '----*', '0': '-----'}


def dash():
    GPIO.output(7, True)
    time.sleep(.5)
    GPIO.output(7, False)
    time.sleep(.5)


def dot():
    GPIO.output(7, True)
    time.sleep(.25)
    GPIO.output(7, False)
    time.sleep(.25)


def space():
    GPIO.output(7, True)
    time.sleep(1)
    GPIO.output(7, False)
    time.sleep(1)


def broadcast(string):
    my_message = ''
    for letter in string:
        my_message += morse[letter] + ' '
    for letter in my_message:
        if letter == '*':
            dot()
        elif letter == '-':
            dash()
        elif letter == ' ':
            space()



broadcast(input('> '))


GPIO.cleanup()
