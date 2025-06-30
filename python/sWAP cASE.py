"""
Problem: Swap Case
Link: https://www.hackerrank.com/challenges/swap-case/problem

Description:
You are given a string. Your task is to swap the case of each character in the string:
- Convert all lowercase letters to uppercase.
- Convert all uppercase letters to lowercase.
- Non-alphabetic characters remain unchanged.

Function Signature:
def swap_case(s: str) -> str

Parameters:
- s (str): A single string containing alpha-numeric characters and symbols.

Returns:
- str: A new string with all letter cases swapped.

Input Format:
- A single line of input containing the string `s`.

Constraints:
- 0 < len(s) ≤ 1000

Output Format:
- Return the modified string after swapping the case for each character.

Sample Input 0:
HackerRank.com presents "Pythonist 2".

Sample Output 0:
hACKERrANK.COM PRESENTS "pYTHONIST 2"
"""

def swap_case(s):
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)