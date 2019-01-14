#!/usr/bin/python3

# set up a morse code beacon with the Si5351 breakout board from Etherkit and a raspberry pi zero.

# note:  I measured 2.7V after the bandpass filter into a 50 ohm load. 
# I think this yields 73mw: I= (2.7 / sqrt(2) / 50) Erms= (2.7 / sqrt(2))  P=I*E

from Si5351 import Si5351
import k5dru_morse
from time import gmtime, strftime 

# si_freq_mhz=0.474474
si_freq_mhz=28.2019
si = Si5351()
si.setFreq(pll=si.PLL_A, output=0, freqMHz = si_freq_mhz)

def enable_tone():
  si.enableOutputs(True)

def disable_tone(): 
  si.enableOutputs(False)

mo = k5dru_morse.morse(wpm=12, tone_callback=enable_tone, notone_callback=disable_tone, print_symbols=True)

while True: 
  mo.send_text("E E E E E E")
  mo.send_text("K5DRU BEACON")
  mo.send_text("PWR 73MW")
  mo.send_text("LOC EM35SA")
  mo.send_text("FREQ " + str(si_freq_mhz) + " MHZ.")
  mo.send_text("THE TIME")
  mo.send_text(strftime("%H:%MZ", gmtime()))
  mo.send_text("PLS QSL")

