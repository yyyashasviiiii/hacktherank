"""
Problem: Python If-Else
Link: https://www.hackerrank.com/challenges/py-if-else/problem

Task:
Given an integer `n`, perform the following conditional actions:

- If `n` is odd, print "Weird"
- If `n` is even and in the inclusive range of 2 to 5, print "Not Weird"
- If `n` is even and in the inclusive range of 6 to 20, print "Weird"
- If `n` is even and greater than 20, print "Not Weird"

Input Format:
A single line containing a positive integer `n`.

Constraints:
1 <= n <= 100

Output Format:
Print "Weird" if the number is weird. Otherwise, print "Not Weird".

Sample Input 0:
3

Sample Output 0:
Weird

Explanation 0:
3 is odd and odd numbers are weird, so the output is "Weird".

Sample Input 1:
24

Sample Output 1:
Not Weird

Explanation 1:
24 is even and greater than 20, so the output is "Not Weird".
"""

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")