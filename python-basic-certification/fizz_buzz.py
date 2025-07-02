"""
Problem: FizzBuzz

Description:
Print the numbers from 1 to n. But for multiples of 3, print "Fizz" instead of the number, 
and for the multiples of 5, print "Buzz". For numbers which are multiples of both 3 and 5, 
print "FizzBuzz".

Function Signature:
def fizz_buzz(n: int) -> None

Parameters:
- n (int): The upper limit of the range (inclusive).

Returns:
- None: The function prints each value (number, "Fizz", "Buzz", or "FizzBuzz") on a new line.

Input Format:
A single integer `n`, the range end.

Output Format:
Print each value from 1 to `n` on a new line, replacing:
- Multiples of 3 with "Fizz"
- Multiples of 5 with "Buzz"
- Multiples of both with "FizzBuzz"

Constraints:
- 1 ≤ n ≤ 10^4

Sample Input:
15

Sample Output:
1  
2  
Fizz  
4  
Buzz  
Fizz  
7  
8  
Fizz  
Buzz  
11  
Fizz  
13  
14  
FizzBuzz

Explanation:
All numbers from 1 to 15 are printed. Multiples of 3 and 5 are replaced as specified.
"""

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)