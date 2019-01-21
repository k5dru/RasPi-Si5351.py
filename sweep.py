#!/usr/bin/python3


from Si5351 import Si5351
import time

# sweep a range of useful frequencies 
# in the center of the amateur bands

si = Si5351()
while True: 
  #for freq in [ 0.136, 0.474, 1.9, 3.7, 5.35, 7.2, 10.1, 14.1, 18.1, 21.1, 24.9, 28.2019, 51, 144 ]: 
  for freq in range(10, 3000):
    si.setFreq(pll=si.PLL_A, output=0, freqMHz = freq / 100.0)
    si.enableOutputs(True)
    print ("Now " + str(freq / 100.0) + " MHz", flush=True)
    time.sleep(0.0420) 


