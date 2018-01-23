import time



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
    GPIO.out(7, True)
    time.sleep(1)
    GPIO.out(7, False)
    time.sleep(1)


def message(string):
    my_message = ''
    for letter in string:
        my_message += morse[letter] + ' '
    return my_message


def broadcast(message, dot, dash):
    for letter in message:
        if letter == '*':
            dot()
        elif letter == '-':
            dash()
        elif letter == ' ':
            space()



print(print_morse(input('> ')))
