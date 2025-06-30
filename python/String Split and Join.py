"""
Problem: Split and Join
Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

Description:
In Python, strings can be split using a delimiter and then joined using another delimiter.

Task:
You are given a string of space-separated words. 
- First, split the string on spaces (" ") to get a list of words.
- Then, join the words using a hyphen ("-") and return the resulting string.

Function Signature:
def split_and_join(line: str) -> str

Parameters:
- line (str): A single string containing space-separated words.

Returns:
- str: A new string where the words are joined by hyphens.

Input Format:
- A single line containing a string of space-separated words.

Output Format:
- Return a single string with the words joined by hyphens.

Sample Input:
this is a string

Sample Output:
this-is-a-string

Example:
>>> split_and_join("hello world")
'hello-world'
"""

def split_and_join(line):
    # write your code here
    
    splitted = line.split(" ")
    joined = "-".join(splitted)
    return joined

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)