# find_min: Find the minimum value in a list of integers.
# Input: A list of integers.
# Output: An integer, the minimum value in the list.
def find_min(items:list):
    min = items[0]
    for item in items:
        if item < min:
            min = items
    return min

# odd_increment_even_decrement_no_modify: Increment all the odd numbers in a list by 1 and decrement all the even numbers by 1, without modifying the original list.
# Input: A list of integers.
# Output: A new list of integers with the modified values.
def odd_increment_even_decrement_no_modify(items) -> list:
    new_items = []
    for item in items:
        if item%2!=0:
            new_items.append(item+1)
        else:
            new_items.append(item-1)
    return new_items

# odd_square_even_double_modify: Square all the odd numbers and double all the even numbers in a list, modifying the list in place.
# Input: A list of integers.
# Output: None (the input list is modified in place).
def odd_square_even_double_modify(items:list) -> list:
    for i in range(len(items)):
        if items[i]%2!=0:
            items[i]**=2
        else:
            items[i]*=2
    return items

# more_than_two_unique_vowels: Given a string of comma-separated words, return a set containing words that have more than two unique vowels.
# Input: A string of comma-separated words.
# Output: A set of words with more than two unique vowels.
def more_than_two_unique_vowels(sentence):
    vowels = set("aeiou")
    words = set()
    for word in sentence.split(","):
        if len(set(word) & vowels)>2:
            words.add(word)
    return words

# sum_of_list_of_lists: Given a list of lists of integers, find the sum of all the integers in all the lists.
# Input: A list of lists of integers.
# Output: An integer, the sum of all the integers in the nested lists.
def sum_of_list_of_lists(lol):
    total = 0
    for row in lol:
        for n in row:
            total+=n
    return total

# flatten: Flatten a list of lists into a single list.
# Input: A list of lists.
# Output: A single flattened list.
def flatten(lol):
    flat = []
    for row in lol:
        for item in row:
            flat.append(item)
    return flat

# all_common: Find the common characters that are present in all strings in a list of strings and return them as a string in ascending order.
# Input: A list of strings.
# Output: A string containing common characters in ascending order.
def all_common(strings):
    common_chars = set(strings[0])
    for string in strings[1:]:
        common_chars &= set(string)
    return ''.join(sorted(common_chars))

# vocabulary: Given a list of sentences (with only alphabets and spaces), find the vocabulary (list of unique words) and return it as a set. Convert all words to lowercase before adding to the vocabulary.
# Input: A list of sentences.
# Output: A set of unique words in lowercase.
def vocabulary(sentences):
    vocab = set()
    for sentence in sentences:
        for word in sentence.split(" "):
            vocab.add(word.lower())
    return vocab