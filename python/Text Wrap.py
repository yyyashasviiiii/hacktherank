"""
Problem: Text Wrap  
Link: https://www.hackerrank.com/challenges/text-wrap/problem

Description:
You are given a long string and an integer value `max_width`.  
Your task is to wrap the string into lines, where each line has exactly `max_width` characters, 
except possibly the last line. The function should return the entire wrapped text as a single string, 
with newline characters (`\n`) indicating where the lines break.

Function Signature:
def wrap(string: str, max_width: int) -> str

Parameters:
- string (str): The input text to wrap.
- max_width (int): The maximum number of characters per line.

Returns:
- str: The wrapped text, with line breaks (`\n`) after every `max_width` characters.

Input Format:
The first line contains the string.  
The second line contains the integer `max_width`.

Output Format:
Return a string with newline characters separating the wrapped lines.

Constraints:
- 0 < len(string) ≤ 1000
- 0 < max_width ≤ len(string)

Sample Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ  
4

Sample Output:
ABCD  
EFGH  
IJKL  
IMNO  
QRST  
UVWX  
YZ

Explanation:
The string is split into parts of width 4 and joined with newline characters.
"""

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width) # used text wrap

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)