"""
HackerRank Problem: Finding the percentage
Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

Task:
You have a record of students. Each record contains the student's name, and their scores in three subjects.
You are required to calculate the average marks of a student provided by their name, and print the result
correct to two decimal places.

Input Format:
- The first line contains the integer n, the number of students' records.
- The next n lines contain the name and the marks obtained by that student, separated by a space.
- The last line contains the query_name, the name of the student whose average marks need to be printed.

Constraints:
- 2 <= n <= 10
- 0 <= Marks[i] <= 100
- Length of student name <= 10

Output Format:
- Print one line: The average of the marks obtained by the queried student, formatted to 2 decimal places.

Sample Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output:
56.00
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")