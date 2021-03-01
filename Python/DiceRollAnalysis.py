#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)

    Nmeas = 1
    Rolls = []
    need_rate = True
    with open(InputFile) as ifile:
        for line in ifile:
           if need_rate:
               need_rate = False
               rate = (line)
               continue

           lineVals = line.split()
           Nmeas = len(lineVals)
           t_avg = 0
           for v in lineVals:
               t_avg += float(v)
               Rolls.append(float(v)) 
Rolls.sort()
    
    # code to analyze the diceroll
w = np.ones_like(Rolls) / len(Rolls)


fig1 = plt.figure()
#quant = np.quantile(fig1, [0.05, 0.5, 0.95], axis=1)
ax1 = fig1.add_subplot()
ax1.hist(Rolls, 10, rwidth = 0.5, align = 'left')
ax1.set_yscale('log')
ax1.set_xlim(0,7)
ax1.set_xlabel('Dice number')
ax1.set_ylabel('times rolled')

#W = np.ones_like(times_avg) / len(times_avg)

#fig2 = plt.figure()
#ax2 = fig2.add_subplot()
#ax2.hist(times_avg, 50, weights = W)
#ax2.set_yscale('log')
#ax2.set_xlabel('Average times')
#ax2.set_ylabel('Probability')

#fig1.savefig('time.png')
#fig2.savefig('average.png')
plt.show()
