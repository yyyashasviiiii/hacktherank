"""
Problem: String Formatting
Link: https://www.hackerrank.com/challenges/python-string-formatting/problem

Description:
Given an integer `number`, print the following values for each integer `i` from 1 to `number`:
- Decimal
- Octal
- Hexadecimal (capitalized)
- Binary

Each output line contains these values separated by a single space, right-aligned to match the width of the binary representation of `number`.

Function Signature:
def print_formatted(number: int) -> None

Parameters:
- number (int): The maximum integer value to print (1 <= number <= 99)

Returns:
- None (prints the formatted values to stdout)

Constraints:
- The binary representation of `number` determines the fixed width of all output columns.

Sample Input:
17

Sample Output:
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
   16    20    10 10000
   17    21    11 10001

Example:
>>> print_formatted(5)
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
"""

def print_formatted(number):

    width = len(bin(number)[2:])
    for i in range(1, number+1):
        
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        
        print(f"{decimal} {octal} {hexadecimal} {binary}")

        # this was approach logic is correct but not the formatting
        # print(f"{str(i)}  {oct(i)[2:]}  {hex(i)[2:].capitalize()}  {bin(i)[2:]}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)