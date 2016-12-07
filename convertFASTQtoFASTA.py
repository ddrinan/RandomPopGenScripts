

# convert FASTQ to FASTA

import sys
input_file = open(sys.argv[1], 'r')


first_line = True
line1 = ''

while line1 or first_line:
    first_line = False
    line1 = input_file.readline()
    line2 = input_file.readline()
    line3 = input_file.readline()
    line4 = input_file.readline()
    
    print '>' + line1[0:-1]
    print line2[0:-1]

input_file.close()


