# CMSC 128: Introduction to Software Engineering
# Assignment 002: Programming a Simple Bioinformatics Library
# Author: Shannon Francis N. Retuerma
# Section: AB - 4L
# Description: A library written in Python programming language that handles string operations for simple Bioinformatics concept like skews and hamming distance
# Note: Written in Python 2.7.11

#!/usr/bin/python

# function for getting the Hamming Distance of 2 strings
def getHammingDistance(str1, str2):
    if ((type(str1) is str) & (type(str2) is str)):                             # type mismatch handler
        differ = 0;
        str1len = len(str1)
        str2len = len(str2)
        if ((str1len!=str2len) | (str1len == 0)):                               # invalid input if strign length not equal
            print ("Error: Invalid Argument Length")
        else:
            i = 0
            while i < str1len:                                                  # compute for hamming distance
                if (str1[i] != str2[i]):
                    differ = differ + 1;
                i = i + 1

        return differ
    else:
        print("Error: Invalid Argument Type")

# function for counting occurence of a substring from a given string
def countSubstrPattern(original, pattern):
    if((type(original) is str) & (type(pattern) is str)):                       # type mismatch handler
        origlen = len(original)
        pattlen = len(pattern)
        if((origlen == 0) | (pattlen == 0)):                                    # if length of 1 of the string is 0
            print("Error: Invalid Argument Length")
        else:
            i = 0
            substrCount = 0
            while i < origlen:                                                  # get the substring count through string traversal
                j = 0
                count = 0
                step = i
                while j < pattlen:
                    if(step>=origlen):
                        break
                    if(pattern[j] == original[step]):
                        count = count + 1
                    step = step + 1
                    j = j + 1
                if(count == pattlen):
                    substrCount = substrCount + 1
                i = i + 1

        return substrCount
    else:
        print("Error: Invalid Argument Type")


# function for checking if a string is valid to a given language/set of characters
def isValidString(str1, alphabet):
    if((type(str1) is str) & (type(alphabet) is str)):                          # type mismatch handler
        strlen = len(str1)
        alen = len(alphabet)
        if ((alen == 0) | (strlen == 0)):                                       # if the strings passed have length 0
            print("Error: Invalid Argument Length")
            return False
        else:
            i = 0
            while i < strlen:                                                   # check if the string is valid according to the language given
                j = 0
                count = 0
                while j < alen:
                    if (str1[i] == alphabet[j]):
                        count = count + 1
                    j = j + 1
                if(count == 0):
                    return False
                i = i + 1

        return True
    else:
        print("Error: Invalid Argument Type");

# function for getting the skew of G and C  of the given string
def getSkewN(str1, n):
    if((type(str1) is str) & (isinstance(n,int))):                              # type mismatch handler
        if((n <= 0) | (len(str1) == 0) | (len(str1) < n)):                      # if the given n is  wrong or the string length is too small
            print("Error: Invalid Argument")
        else:
            countG = 0                                                          # count the number of G and C that occured in the string and compute for the skew
            i = 0
            while i < n:
                if(str1[i] == "G"):
                    countG = countG + 1
                i = i + 1

            countC = 0
            j = 0
            while j < n:
                if(str1[j] == "C"):
                    countC = countC + 1
                j = j + 1

            skew = countG - countC
            return skew
    else:
        print("Error: Invalid Argument Type");

# function for getting the maximum skew of a given string up to nth iteration
def getMaxSkewN(str1, n):
    if((type(str1) is str) & (isinstance(n,int))):                              # type mismatch handler
        if((n <= 0) | (len(str1) == 0) | (len(str1) < n)):                      # error handling for the input
            print("Error: Invalid Argument")
        else:
            i = 1
            skew = 0                                                            # get the maximum computed skew
            maxSkew = 0
            while i-1 < n:
                skew = getSkewN(str1, i)
                if(skew > maxSkew):
                    maxSkew = skew
                i = i + 1

            return maxSkew
    else:
        print("Error: Invalid Argument Type");

# function for getting the minimum skew of a given string up to nth iteration
def getMinSkewN(str1, n):
    if((type(str1) is str) & (isinstance(n,int))):                              # type mismatch handler
        if((n <= 0) | (len(str1) == 0) | (len(str1) < n)):                      # error handling for the input
            print("Error: Invalid Argument")
        else:
            i = 1                                                                # get the minimum computed skew
            skew = 0
            minSkew = float('inf')
            while i-1 < n:
                skew = getSkewN(str1, i)
                if(minSkew > skew):
                    minSkew = skew
                i = i + 1

            return minSkew
    else:
        print("Error: Invalid Argument Type");
