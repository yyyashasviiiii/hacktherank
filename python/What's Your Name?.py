"""
Problem: What's Your Name?
Link: https://www.hackerrank.com/challenges/whats-your-name/problem

Description:
You are given the first name and the last name of a person on two separate lines. 
Your task is to print a greeting using their full name in the format:
"Hello <first> <last>! You just delved into python."

Function Signature:
def print_full_name(first: str, last: str) -> None

Parameters:
- first (str): The person's first name.
- last (str): The person's last name.

Returns:
- None: This function prints the output directly.

Input Format:
- The first line contains the first name.
- The second line contains the last name.

Output Format:
- Prints the message: "Hello <first> <last>! You just delved into python."

Sample Input:
Ross
Taylor

Sample Output:
Hello Ross Taylor! You just delved into python.

Example:
>>> print_full_name("John", "Doe")
Hello John Doe! You just delved into python.
"""

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    # Using f-string
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)