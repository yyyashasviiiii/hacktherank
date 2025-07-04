"""
Problem: Find a Substring  
Link: https://www.hackerrank.com/challenges/find-a-string/problem

Description:
You are given two strings:
1. A main string `string`
2. A smaller string `sub_string`

Your task is to count how many times the `sub_string` occurs in the main `string`, **including overlapping occurrences**.

Note:
- The search is case-sensitive.
- You must manually count the occurrences by traversing the main string from left to right.
- Built-in methods like `.count()` will not work correctly because they do not consider overlapping matches.

Input Format:
- The first line contains the original string.
- The second line contains the substring to search for.

Constraints:
- Each character in both strings is an ASCII character.
- 1 ≤ len(sub_string) ≤ len(string) ≤ 200

Output Format:
- Print a single integer: the total number of times the `sub_string` appears in the main `string`, including overlaps.

Sample Input 0:
ABCDCDC  
CDC

Sample Output 0:
2

Explanation:
"CDC" appears twice in "ABCDCDC":
- First at index 2
- Again (overlapping) at index 4
"""

def count_substring(string, sub_string):
    big = len(string)
    small = len(sub_string)
    count = 0
    for i in range(big - small  + 1):
        if string[i:i+small] == sub_string:
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)