"""
Problem: Missing Characters

Description:
You are given a string that may contain lowercase letters and digits. Your task is to identify
which lowercase letters (a–z) and digits (0–9) are missing from the string.

- The digits should appear first in the result (in sorted order).
- Then the lowercase letters that are missing (also in sorted order).
- Return the final result as a single concatenated string.

Function Signature:
def missingCharacters(s: str) -> str

Parameters:
- s (str): A string possibly containing digits and lowercase letters.

Returns:
- str: A string containing all missing digits followed by all missing letters, both sorted.

Input Format:
A single line string `s` containing alphanumeric characters.

Output Format:
A single string of missing characters (digits followed by lowercase letters).

Sample Input:
abc3458z

Sample Output:
012679defghijklmnopqrstuvwxy

Explanation:
The input contains characters from the digit set and lowercase letters. All characters not found
in the input are included in the output string in ascending order.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def missingCharacters(s):
    
    digits_all = set("0123456789")
    letters_all = set("abcdefghijklmnopqrstuvwxyz")
    given = set(s)
    
    missing_digits = sorted(digits_all - given)
    missing_letters = sorted(letters_all - given)
    result = missing_digits + missing_letters
    
    return "".join(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

    fptr.close()