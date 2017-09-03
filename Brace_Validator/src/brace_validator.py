#!/bin/python

import sys

# number of input brace strings
count = int(raw_input().strip())

# iterate over each string and validate it
for i in xrange(count):

    str = raw_input().strip()

    # list used to stack the frequency of opening and closing braces
    tmpBraceList = []

    validationFlag = "YES"

    # find all condition where input string can be validated and discared
    if len(str) == 0 or len(str)%2 == 1:
        validationFlag = "NO"
    else:
        for brace in str:
            if brace == '[' or brace == '{' or brace == '(':
                tmpBraceList.append(brace)
            else:
                if not tmpBraceList:
                     validationFlag = "NO"
                     break
                else:
                     br = tmpBraceList.pop()
                     if ( (br == '[' and brace != ']') or (br == '{' and brace != '}') or (br == '(' and brace != ')') ):
                         validationFlag = "NO";
                         break;

    if tmpBraceList:
        validationFlag = "NO"
    # print the final value of validationFlag    
    print validationFlag

