
################################################################################
#   
# parseGenepopHWE.py
#
# Daniel Drinan <ddrinan@uw.edu> 2017-01-20
#
# This script parses a genepop output file for tests of Hardy-Weinberg Equilibrium
# (probability test). The script will spit out the loci that should be retained
# 
# Usage:
# $> python parseGenepopHWE.py
#
################################################################################


import sys

genepopFile = open(sys.argv[1], 'r')

line = genepopFile.readline()
numPops = -1
numLoci = -1

while 'Results by locus' not in line:
    if 'Number of populations detected' in line:
        numPops = int(line.split()[-1])
    if 'Number of loci detected' in line:
        numLoci = int(line.split()[-1])
        
    line = genepopFile.readline()

print 'Number of populations detected:', numPops
print 'Number of loci detected:', numLoci



# get user input to figure out how many loci must be in HWE to retain
value = input('How many populations must be in HWE to retain a locus? ')

try:
    threshold = int(value)
except ValueError:
    print('\nHey joker, you did not enter a valid integer.')
    sys.exit(0)




# parse the meat of the file
while numLoci > 0:
    if 'Locus' in line:
        numLoci -= 1
        tmpLocus = line.split()[1].replace('"', '')
        tmpPvals = []
        
        while 'POP' not in line:
            line = genepopFile.readline()

        line = genepopFile.readline()
        line = genepopFile.readline()

        for i in range(numPops):
            tmpP = line.split()[1]

            if tmpP == '-':
                tmpPvals.append(1)
            else:
                tmpPvals.append(float(tmpP))
            line = genepopFile.readline()

        if sum(i > 0.05 for i in tmpPvals) >= threshold:
            print tmpLocus

    line = genepopFile.readline()

genepopFile.close()


'''
Example genepop output file:

Genepop  version 4.2.1: Hardy-Weinberg test

File: batch_1_pop_gen.txt (Stacks version 1.35; Genepop version 4.1.3; January 20, 2017)

Number of populations detected:    5
Number of loci detected:           2613


Estimation of exact P-Values by the Markov chain method. 
---------------------------------------------
Markov chain parameters for all tests:
Dememorization:              10000
Batches:                     20
Iterations per batch:        5000
Hardy Weinberg: Probability test
        ************************


==========================================
     Results by locus
==========================================


Locus "12_40"
-----------------------------------------
                             Fis estimates
                            ---------------
POP         P-val   S.E.    W&C     R&H     Steps 
----------- ------- ------- ------- ------- ------
ANI_M095_1  0.0005  0.0001  -0.8824 -0.8854  64489 switches
ATU_M092_0  0.0000  0.0000  -1.0000 -1.0000  65492 switches
PBC_w04_M0  0.0000  0.0000  -1.0000 -1.0000  66207 switches
PTR_M092_0  0.0000  0.0000  -1.0000 -1.0000  62753 switches
QCI_M075_1  0.0008  0.0002  -0.8000 -0.8042  65313 switches

All (Fisher's method):
 Chi2:    Infinity
 Df   :    10.0000
 Prob :    High. sign.

Locus "12_106"
-----------------------------------------
                             Fis estimates
                            ---------------
POP         P-val   S.E.    W&C     R&H     Steps 
----------- ------- ------- ------- ------- ------
ANI_M095_1  0.0000  0.0000  -1.0000 -1.0000  61459 switches
ATU_M092_0  0.0000  0.0000  -1.0000 -1.0000  65006 switches
PBC_w04_M0  0.0000  0.0000  -1.0000 -1.0000  66291 switches
PTR_M092_0  0.0001  0.0000  -1.0000 -1.0000  62666 switches
QCI_M075_1  0.0000  0.0000  -1.0000 -1.0000  65984 switches

......

'''
