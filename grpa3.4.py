# factors - Find the factors of a number n (including 1 and itself) in ascending order.
# find_min - Take n numbers from the input and print the minimum number.
# prime_check - Check whether a given number is prime or not.
# is_sorted - Check if all characters of the given string from input are in alphabetical order. Print the output as "True" or "False" accordingly.
# any_true - Take n numbers from input and check if any of the numbers are divisible by 3. Print the output as "True" or "False" accordingly.
# manhattan - Take inputs directions such as "UP", "DOWN", "LEFT" and "RIGHT" from the input until the input is "STOP". Assume you are starting from (0,0) in a cartesian coordinate. Find the Manhattan distance between the starting point and the ending point by following the steps in the cartesian plane.
# Write a program to solve these tasks. Use loops where necessary.

task = input()

if task == "factors":
    n = int(input())
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

elif task == "find_min":
    n = int(input())
    minimum = int(input())
    for i in range(n-1):
        current = int(input())
        if current< minimum:
            minimum = current
    print(minimum)

elif task == "prime_check":
    n = int(input())
    if n <= 1:
        print(False)
    else:
        flag = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                flag = False
                print(False)
                break
        if flag:
            print(True)
    # The below is an alternate implementation using for...else block in python which do not require the flag variable.
    #     for i in range(2, int(n**0.5) + 1):
    #        if n % i == 0:
    #            print(False)
    #            break
    #    else:
    #         print(True)

elif task == "is_sorted":
    s = input()
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            print(False)
            break
    else:
        print(True)

elif task == "any_true":
    n = int(input())
    for _ in range(n):
        n = int(input())
        if n % 3 == 0:
            print(True)
            break
    else:
        print(False)

elif task == "manhattan":
    x, y = 0, 0
    while True:
        move = input().strip()
        if move == "STOP":
            break
        elif move == "UP":
            y += 1
        elif move == "DOWN":
            y -= 1
        elif move == "LEFT":
            x -= 1
        elif move == "RIGHT":
            x += 1
    print(abs(x) + abs(y))

else:
    print("Invalid task")
