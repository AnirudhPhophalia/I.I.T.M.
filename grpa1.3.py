'''output1 = ... # str: get the third character of s

output2 = ... # str: get the fourth last character of s

output3 = ... # str: get the first 3 characters of s

output4 = ... # str: get every second character of s

output5 = ... # str: get the last 3 characters of s

output6 = ... # str: get the reverse of s

course_term = ... # int: get the term of the year as number from course_code
course_year = ... # int: get the year as two digit number from course_code'''
s = "hello pyhton"
course_code = "24t2cs1002" # 24 - year, t2 - term 2, cs1002 - course id
output1 = s[2] # str: get the third character of s

output2 = s[-4] # str: get the fourth last character of s

output3 = s[:3] # str: get the first 3 characters of s

output4 = s[::2] # str: get every second character of s

output5 = s[-3:] # str: get the last 3 characters of s

output6 = s[::-1] # str: get the reverse of s

course_term = int(course_code[3]) # int: get the term of the year as number from course_code
course_year = int(course_code[:2]) # int: get the year as two digit number from course_code
print(output1)
print(output2)
print(output3)
print(output4)
print(output5)
print(output6)
print(course_term)
print(course_year)