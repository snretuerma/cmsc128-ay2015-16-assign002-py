# cmsc128-ay2015-16-assign002-py
Assign 002: Programming a Simple Bioinformatics Library<br /> 
Author: Shannon Francis N. Retuerma<br /> 
Section: AB - 4L<br /> 
Note: Written using Python 2.7.11

*Includes 6 Functions:*

1. getHammingDistance(string1, string2) : Accepts 2 strings with equal length and computes its hamming distance (which is the number of inversions in the strings).<br />
                                          Returns an integer value for the Hamming Distance.<br />
2. countSubstrPattern(string, substr): Accepts 2 strings, the main string and the substring to be checked. Returns an integer value for the substring count in the given string.<br />
3. isValidString(string, alphabet): Accepts 2 strings, the string to be checked and the alphabet string. Returns a boolean value depending on the check (True if the string is valid else false).<br />
4. getSkewN(string, n) : Accepts a string and an integer value. It gets the difference in number of occurrences of G and C in the string input until the nth index. Returns the difference of the number of G's and C's<br />
5. getMaxSkewN(string, n): Gets the maximum skew of from a string until the n iteration. Returns an integer for the maximun<br /> 
6. getMinSkewN(string, n): Gets the minimum skew of from a string until the n iteration. Returns an integer for the minimum<br />
