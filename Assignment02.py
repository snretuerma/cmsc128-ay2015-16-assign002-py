#!/usr/bin/python

def getHammingDistance(str1, str2):
    differ = 0;
    str1len = len(str1)
    str2len = len(str2)
    if (str1len!=str2len | str1len <= 0):
        print ("Error: Length of Argument 1 is not equal to length of Argument 2")
    else:
        i = 0
        while i < str1len-1:
            if (str1[i] != str2[i]):
                differ = differ + 1;
            i = i + 1;

    return differ;
