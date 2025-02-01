# Get age(int), dob(str of format "dd/mm/yy") and weight(float) from the standard input and print the tenth_month, fifth_birthday and last_birthday formatted as "day/month/year"(do not include the preceeding zero for single digit number) separated by comma and a space a single line and print the weight_readable(str formatted as "55 kg 200 grams")

# Note: while formatting dates you may have to convert back int to str using the type conversion. There is something called as "f-strings" or "formatted strings" that will help us format things by automatically doing type conversion. This will be covered in later weeks. But you can explore that (Google or ChatGPT) and compare the difference.

# Note: The last_birthday depends on the dob and age. For example if the dob is "20/02/2001" and the age is 5 the last birthday will be "20/02/2006".



age = int(input()) # int: Read a number as integer from standard input
dob = str(input()) # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob[:2]), int(dob[3:5]), int(dob[6:]) # int, int, int: Get the correct parts from dob as int
fifth_birthday = str(day) + '/' + str(month) + '/' + str(year + 5) # str: fifth birthday formatted as day/month/year 

last_birthday = str(day) + '/' + str(month) + '/' + str(year + age) # str: last birthday formatted as day/month/year

month += 10
month, year = (month-1)%12+1, year+(month-1)//12
tenth_month = str(day) + '/' + str(month) + '/' + str(year) # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month,fifth_birthday,last_birthday,sep=", ")

weight = float(input()) # float: Read a number as float from stdin(Standard input)

kg = int(weight)  # Get the integer part (kg)
grams = int((weight - kg) * 1000)  # Get the fractional part converted to grams

weight_readable = str(kg)+" kg "+str(grams)+" grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable)