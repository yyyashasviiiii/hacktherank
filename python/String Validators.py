"""
Problem: String Validators  
Link: https://www.hackerrank.com/challenges/string-validators/problem

Description:
You are given a string `s`. Your task is to determine whether the string contains any of the following character types:
1. Alphanumeric characters (letters and/or digits)
2. Alphabetical characters (only letters)
3. Digits (only 0–9)
4. Lowercase characters (a–z)
5. Uppercase characters (A–Z)

You must print a separate boolean result (`True` or `False`) for each of the five character type checks, in the order listed above.
Use Python's built-in string methods with `any()` to check if at least one character in the string satisfies each condition.

Input Format:
- A single line containing a non-empty string `s`.

Constraints:
- 0 < len(s) < 1000

Output Format:
- Five lines of output. Each line prints either `True` or `False`.
  1. True if `s` contains at least one alphanumeric character.
  2. True if `s` contains at least one alphabetical character.
  3. True if `s` contains at least one digit.
  4. True if `s` contains at least one lowercase character.
  5. True if `s` contains at least one uppercase character.

Sample Input 0:
qA2

Sample Output 0:
True  
True  
True  
True  
True

Explanation:
- The string "qA2" contains:
  - Alphanumeric characters: q, A, 2
  - Alphabetical characters: q, A
  - A digit: 2
  - A lowercase letter: q
  - An uppercase letter: A
"""

if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))