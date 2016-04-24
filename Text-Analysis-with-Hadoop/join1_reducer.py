#!/usr/bin/env python
import sys
          



prev_word = None
print_variable = 0
running_total = 0

for line in sys.stdin:
    line       = line.strip()
    key_value = line.split('\t')       
    curr_word  = key_value[0]        
    value_in   = key_value[1]
    if (prev_word != curr_word):
        if (print_variable ==1):
            print('%s\t%s' % (prev_word,running_total))
            print_variable = 0
            running_total = 0
        if (value_in != "ABC"):
            running_total = int(value_in) 
    else:
        if (value_in != "ABC"):
            running_total = running_total + int(value_in)
    if (value_in == "ABC"):
        print_variable = 1
    prev_word = curr_word
 


