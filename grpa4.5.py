# sum_of_squares - find the sum of squares of numbers in a list - (mapping and aggregation)

def sum_of_squares(numbers):
    return sum([num**2 for num in numbers])

# total_cost - given quantitiy and price of each item as a list of tuples find the total cost using list comprehensions
def total_cost(cart):    
    return sum([quantity*price for quantity, price in cart])

# abbreviation - given a string with multiple words seperated by space, form an abbrevation out of it by taking the first letter in caps. (mapping and aggregation)
def abbreviation(sentence):
    return ".".join([word[0].upper() for word in sentence.split()])+"."

# palindromes - given a list of strings, create a new list with only palindromes filtering
def palindromes(words):
    return [word for word in words if word == word[::-1]]

# all_chars_from_big_words - find the all unique characters (case insensitive, make all lowercase) from all words with size greater than 5 in a given sentence with words seperated by spaces. (filtering)
def all_chars_from_big_words(sentence):
    return {
        letter.lower()
        for word in sentence.split()
        for letter in word
        if len(word)>5
    }

# flatten - flatten a nested list using comprehension
def flatten(lol):
    return [elem for row in lol for elem in row]

# unflatten - given a flat list and number of rows, create a matrix (2d list) with that number of rows. (nested-aggregation)
def unflatten(items, n_rows):
    n_cols = len(items)//n_rows
    return [
        [items[n_cols*j+i] for i in range(n_cols)]
        for j in range(n_rows)
    ]

# make_identity_matrix - make an identity (with ones on the main diagonal and zeros elsewhere) given the size.
def make_identity_matrix(m):
    return [
        [1 if i==j else 0 for i in range(m)]
        for j in range(m)
    ]

# make_lower_triangular_matrix - given number of rows m, create a lower triangular matrix like the pattern below. for m = 5
def make_lower_triangular_matrix(m):
    return [
        [i+1 if i<=j else 0 for i in range(m)]
        for j in range(m)
    ]