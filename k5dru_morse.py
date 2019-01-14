#!/usr/bin/python3

import time 

# James Lemley, Arduino code 2014-04-21, implemented from forum post by AE5AE (below)
# James Lemley, converted to Python 2019-01-12

# from wikipedia and here: 
#http:# forum.arduino.cc/index.php/topic,8243.0.html, 
#<quote>
#For what it's worth, if you want to show real Morse code:
#a dit is your basic unit of timing.  A dah is supposed to be three times the length of a dit.
#Between each dit or dah in a letter, a dits worth of silence is observed.
#After each letter, three dits of silence is observed.
#After each word, seven dits of silence is observed although older Morse Code operators
#use five.  Current school of thought is seven.
#The length of a dit is determined by the speed, or words per minute, that you intend to send at.
#Code:
#t_dit = 1200/wpm;
#when using seven dits between words.
#For five dits use:
#Code:
#t_dit = 1250/wpm;
#t_dit will be in units of milliseconds, just right for delay().
#[/list]
#When you get done flashing LEDs, try using the tone() function with a
#piezo speaker!  600 Hz is a good pitch for Morse Code.
#
#Programming-wise: Don't write so much code, like your loooonng switch()
#statement, when you can build a data structure to control your code.  In
#other words, create an array with two pieces of data in each element --
#the sequence of dits and dahs, and how many dits/dahs are to be used
#for each letter.  Let a zero bit represent a dit and a 1 represent a dah.
#Let your code select the data element you need per the character input.
#Next have your code loop over the data element selected to decide to
#display a dit or a dah.   End result is that code might be a little more
#complex but it will be much shorted and easier to work on.
#73 de AE5AE
#</quote>

class morse(object):

    # set constants
    morse_dit_between_words = 7  # or 5 

    #   Represent the letter, then the 
    #   number of bits, then a right-justified
    #   Morse word with 0 as dit and 1 as dah. 
    morse_symbols={
    '!': [  6,  int('00101011', 2)], #KW.digraph
    '"': [  6,  int('00010010', 2)],
    '$': [  7,  int('00001001', 2)],  #SX.digraph
    '&': [  5,  int('00001000', 2)],  #AS.digraph
    '(': [  5,  int('00010110', 2)],
    ')': [  6,  int('00101101', 2)],
    '+': [  5,  int('00001010', 2)],
    ',': [  6,  int('00110011', 2)],
    '-': [  6,  int('00100001', 2)],
    '.': [  6,  int('00010101', 2)],
    '/': [  5,  int('00010010', 2)],
    '0': [  5,  int('00011111', 2)],
    '1': [  5,  int('00001111', 2)],
    '2': [  5,  int('00000111', 2)],
    '3': [  5,  int('00000011', 2)],
    '4': [  5,  int('00000001', 2)],
    '5': [  5,  int('00000000', 2)],
    '6': [  5,  int('00010000', 2)],
    '7': [  5,  int('00011000', 2)],
    '8': [  5,  int('00011100', 2)],
    '9': [  5,  int('00011110', 2)],
    ':': [  6,  int('00111000', 2)],
    ';': [  6,  int('00101010', 2)],
    '=': [  5,  int('00010001', 2)],
    '?': [  6,  int('00001100', 2)],
    '@': [  6,  int('00011010', 2)],
    'A': [  2,  int('00000001', 2)],
    'B': [  4,  int('00001000', 2)],
    'C': [  4,  int('00001010', 2)],
    'D': [  3,  int('00000100', 2)],
    'E': [  1,  int('00000000', 2)],
    'F': [  4,  int('00000010', 2)],
    'G': [  3,  int('00000110', 2)],
    'H': [  4,  int('00000000', 2)],
    'I': [  2,  int('00000000', 2)],
    'J': [  4,  int('00000111', 2)],
    'K': [  3,  int('00000101', 2)],
    'L': [  4,  int('00000100', 2)],
    'M': [  2,  int('00000011', 2)],
    'N': [  2,  int('00000010', 2)],
    'O': [  3,  int('00000111', 2)],
    'P': [  4,  int('00000110', 2)],
    'Q': [  4,  int('00001101', 2)],
    'R': [  3,  int('00000010', 2)],
    'S': [  3,  int('00000000', 2)],
    'T': [  1,  int('00000001', 2)],
    'U': [  3,  int('00000001', 2)],
    'V': [  4,  int('00000001', 2)],
    'W': [  3,  int('00000011', 2)],
    'X': [  4,  int('00001001', 2)],
    'Y': [  4,  int('00001011', 2)],
    'Z': [  4,  int('00001100', 2)],
    '\'': [ 6,  int('00011110', 2)],
    '_': [  6,  int('00001101', 2)]  # Not.in.ITU-R.recommendation
    }


    def default_tone_func(): 
        print ("k5dru_morse: set a function to start the tone")

    def default_notone_func(): 
        print ("k5dru_morse: set a function to stop the tone")

    def __init__(self, wpm=12, tone_callback=default_tone_func, notone_callback=default_notone_func, print_symbols=False):

        # set local variables
        self.morse_wpm = wpm
        self.morse_t_dit = 1200.0 / wpm   # /* use 1250 for 5 dits between words, 1200 for 7 dits between words */
        self.morse_t_dah = self.morse_t_dit * 3.0
        self.tone = tone_callback
        self.notone = notone_callback
        self.print_symbols = print_symbols

        # todo:  implement methods to adjust speed. 

#void adjust_speed(int difference)
#{
#   if (difference > 0)
#   {
#      morse_wpm *= 1.02;
#      Serial.println("");
#      Serial.print(morse_wpm);
#      Serial.println("WPM");
#   }
#   if (difference < 0)
#   {
#      morse_wpm *= (1.0 / 1.02);
#   }
#   morse_t_dit = 1200.0 / morse_wpm;   # /* use 1250 for 5 dits between words, 1200 for 7 dits between words */
#   morse_t_dah = morse_t_dit * 3.0;
#}
#
#void check_and_adjust()
#{
#    if (digitalRead(8) == LOW)
#       adjust_speed(1);
#    if (digitalRead(7) == LOW)
#       adjust_speed(-1);
#}


    def delay(self, ms): 
        time.sleep(0.001 * ms)

    def send_dit(self):
        self.tone()
        if self.print_symbols:
            print('.', end='', flush=True)
        self.delay(self.morse_t_dit)
        self.notone()
       #   check_and_adjust();

    def send_dah(self):
        self.tone()
        if self.print_symbols:
            print('-', end='', flush=True)
        self.delay(self.morse_t_dah)
        self.notone()
    #   check_and_adjust(); 

    def send_interchar(self):
        if self.print_symbols:
            print(' ', end='', flush=True)
        self.delay(self.morse_t_dit * 3)   #  3 dits between characters

    def send_interword(self):
        if self.print_symbols:
            print('/', end='', flush=True)
        self.delay(self.morse_t_dit * self.morse_dit_between_words)

    def send_a_char(self, bits, pattern):
        while(bits):
            bits = bits - 1
            if (pattern & (1 << bits)):
                self.send_dah()
            else:
                self.send_dit()
            if (bits):
                self.delay(self.morse_t_dit) 
           
    def send_text(self, text):
        for i in range(0,len(text)):
            if (text[i] == ' '):
                self.send_interword() 
                continue
  
            try: 
                c = self.morse_symbols[text[i]]
            except: 
                self.send_a_char(8, 0x00000000)  #  error? 
                continue
      
            self.send_a_char(c[0], c[1])

            # if this is not the last character: 
            if (i < len(text) - 1 and text[i+1] != ' '): 
                self.send_interchar()

        self.send_interword()
        print ("")
  

if __name__ == '__main__':

    def local_tone_function(): 
        # define a function in your calling program that will start the tone generation.
        pass

    def local_notone_function(): 
        # define a function in your calling program that will STOP the tone generation.
        pass

    mo = morse(wpm=15, tone_callback=local_tone_function, notone_callback=local_notone_function, print_symbols=True)

    mo.send_text("CQ CQ")
    mo.send_text("DE K5DRU K")

