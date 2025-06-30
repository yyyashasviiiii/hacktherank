"""
Problem: Leap Year
Link: https://www.hackerrank.com/challenges/write-a-function/problem

Description:
An extra day is added to the calendar almost every four years as February 29, known as a leap day.
It accounts for the fact that Earth takes approximately 365.25 days to orbit the sun.
A year containing a leap day is called a leap year.

In the Gregorian calendar, a leap year satisfies the following conditions:
- The year is evenly divisible by 4;
    - Except years evenly divisible by 100;
        - Unless the year is also evenly divisible by 400.

This means:
- Years like 2000, 2400 are leap years.
- Years like 1800, 1900, 2100, 2300 are **not** leap years.

Task:
Write a function `is_leap(year)` that returns `True` if the given year is a leap year, and `False` otherwise.

Input Format:
- A single integer, `year`, where 1900 <= year <= 10^5

Output Format:
- Return a Boolean value: `True` if it's a leap year, `False` otherwise

Sample Input 0:
1990

Sample Output 0:
False

Explanation:
1990 is not divisible by 4, so it is not a leap year.
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

year = int(input())
print(is_leap(year))