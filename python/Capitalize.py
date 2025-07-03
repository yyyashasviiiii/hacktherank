"""
Problem: Capitalize!

Link: https://www.hackerrank.com/challenges/capitalize/problem

Description:
You are given a full name as a string. Your task is to capitalize the name properly:
- Capitalize the first letter of each word.
- All other characters in each word should remain lowercase.
- Words may contain digits, and only the first alphabetical character should be capitalized.
- If a word begins with a digit (e.g. "12abc"), it remains unchanged.

Function Signature:
def solve(s: str) -> str

Parameters:
- s (str): A single string containing a full name consisting of alphanumeric characters and spaces.

Returns:
- str: A properly capitalized version of the input string.

Input Format:
A single line of input containing the full name.

Output Format:
A single line with each word's first letter capitalized.

Constraints:
- The string consists of alphanumeric characters and spaces.

Sample Input:
chris alan

Sample Output:
Chris Alan

Example:
>>> solve("alison heck")
'Alison Heck'
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    s = s.strip()
    
    ls = s.split(" ")
    for i in range(len(ls)):
        ls[i] = ls[i].capitalize()
    return " ".join(ls)
    
    # return " ".join(word.capitalize() for word in s.split(" "))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()