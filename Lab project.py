from engi1020.arduino import *
import random
from time import sleep
word=''
def printData(index, value):
  i = str(int(index))
  lcd_move_cursor(0, 2)
  lcd_print(i)
  for i in range(4+len(i), 10):
    lcd_print(' ')

  v = (value)
  lcd_move_cursor(0, 12)
  lcd_print(v)
  for i in range(12+len(v), 16):
    lcd_print(' ')

def Alphabets():
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Range=(1023/25)
    while True:
        index=round(analog_read(0)/Range)
        value=letters[index]
        printData(index, value)
        if digital_read(4):
            lcd_clear()
            return value

Words=['MOUSE','CAT','AVENGERS','CUCMBER','CHICKEN','FRENCH','BARBEQUE','DEER']
Choice=random.choice(Words)
Final=Words.index(Choice)
lcd_print('Welcome2Hangman')
sleep(2)
lcd_clear()
lcd_print('Only 5 Turns')
sleep(2)
lcd_clear()
if Choice==Words[0] or Choice==Words[1] or Choice==Words[4] or Choice==Words[7]:
    lcd_print('Length of word')
    lcd_print(len(Choice))
    sleep(2)
    lcd_clear()
    lcd_print('Hint=Animal')
    sleep(2)
    lcd_clear()
elif Choice==Words[2]:
    lcd_print('Length of word')
    lcd_print(len(Choice))
    sleep(2)
    lcd_clear()
    lcd_print('Hint=Movie')
    sleep(2)
    lcd_clear()
elif Choice==Words[3]:
    lcd_print('Length of word')
    lcd_print(len(Choice))
    sleep(2)
    lcd_clear()
    lcd_print('Hint=Vegetable')
    sleep(2)
    lcd_clear()
elif Choice==Words[5]:
    lcd_print('Length of word')
    lcd_print(len(Choice))
    sleep(2)
    lcd_clear()
    lcd_print('Hint=Language')
    sleep(2)
    lcd_clear()
else:
    lcd_print('Length of word')
    lcd_print(len(Choice))
    sleep(2)
    lcd_clear()
    lcd_print('Hint=Sauce')
    sleep(2)
    lcd_clear()
i=0
while i<5:
    lcd_print('Turn')
    lcd_print(i+1)
    sleep(1)
    lcd_clear()
    letter=Alphabets()
    Count=Choice.count(letter)
    if Count>0:
        lcd_print('Correct')
        sleep(2)
        lcd_clear()
        lcd_print('letter found')
        lcd_print(letter)
        Choice=Choice.replace(letter,'')
        sleep(2)
        lcd_clear()
        lcd_print('No.letters left')
        lcd_print(len(Choice))
        sleep(2)
        lcd_clear()
    else:
        buzzer_note(2, 440, 500)
        sleep(2)
        buzzer_stop(2)
        lcd_print('Incorrect')
        sleep(2)
        lcd_clear()
        i+=1
    if Choice=='':
        analog_write(2, 255)
        lcd_print('You WON!')
        sleep(3)
        lcd_clear()
        lcd_print('Word Found')
        sleep(1)
        lcd_clear()
        lcd_print(Words[Final])
        sleep(2)
        lcd_clear()
        exit()
lcd_print('You Lost')
sleep(3)
lcd_clear()
lcd_print('Word Was')
sleep(1)
lcd_clear()
lcd_print(Words[Final])
sleep(2)