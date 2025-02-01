# # Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
# with open(__file__) as f:
#     content = f.read().split("# <eoi>")[2]
# if "while " in content:
#     print("You should not use while loop or the word while anywhere in this exercise")

# # your code should not use more than 7 for loops 
# # assuming one for loop per problem
# if content.count("for ")>7:
#     print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>

#factorial - print factorial of a given non-negative integer n (Type: Accumulation)
# by for loop
if task == 'factorial':
    n = int(input())
    fact = 1
    for i in range(1,n+1):
        fact *= i
        i += 1
    print(fact)

#even_numbers - Print the even numbers from 0 (including) till the given input number n(including) in multiple lines (Type: Just Iterating)
elif task == 'even_numbers':
    n = int(input())
    for i in range(n+1):
        if(i % 2 == 0):
            print(i)



#power_sequence
#  - Print the sequence 1, 2, 4, 8, 16, ... n terms in same line in multiple lines, where n is taken from the input(Type: Mapping)
elif task == 'power_sequence':
    n = int(input())
    for i in range(n+1) :
        print(2 ** i)


#sum_not_divisible - Print the sum of positive less that the given number n and not divisible by 4 and 5. (Type: Filtered Accumulation)
elif task == 'sum_not_divisible':
    n = int(input())
    total = 0
    for i in range(1, n):
        if i % 4 != 0 and i % 5 != 0:
            total += i
    print(total)

#from_k - Starting from 100 and going in the decreasing order, print the reverse(digits reversed) of first n numbers starting from k which do not have the digit 5 and 9 and is odd number in multiple lines.
elif task == 'from_k':
    n = int(input())
    k = int(input())
    count = 0
    for i in range(k, 0, -1):
        i_1 = str(i)
        if i % 2 != 0 and '5' not in i_1 and '9' not in i_1 :
            print(i_1[::-1])
            count += 1
        if count == n :
            break
    # # Same code using while loop
    # n = int(input())
    # k = int(input())
    # count = 0
    # c = k-1
    # while count < n :
    #     if '5' not in str(c) and '9' not in str(c) and c % 2 != 0:
    #         rev = int(str(c)[::-1])
    #         print(rev)
    #         count += 1
    #     c -= 1


# string_iter - Given a string s of digits print the numerical value of the digit multiplied by the previous digit. Assume the pevious digit for the first element to be 1.
elif task == 'string_iter':
    s = input()
    prev = 1
    for char in s:
        num = int(char)
        print(num * prev)
        prev = num

# list_iter - Print the elements of a list l line by line in the format {element} - type: {type} where the element is the current element being iterated by the for loop and type is the type of the element. (Even though list are not covered in this week, this is included to demonstrate the similarity between iterating characters in a str and items in a list)
elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input
    for item in lst():
        print(f'{item} - type: {type(item)}')

else:
    print("Invalid")