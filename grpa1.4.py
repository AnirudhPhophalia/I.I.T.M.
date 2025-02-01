'''output1 = ... # str: join word1 and word2 with space in between

output2 = ... # str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between

output3 = ... # str: join the word3 and n1 with a space in between

output4 = ... # str: just the hypen "-" repeated 50 times

output5 = ... # str: just the hypen "-" repeated n2 times

output6 = ... # str: repeat the number n1, n2 times

are_all_words_equal = ... # bool: True if all three words are equal

is_word1_comes_before_other_two = ... # bool: True if word1 comes before word2 and word3 assume all words are different

has_h = ... # bool: True if word1 has the letter h

ends_with_a = ... # bool: True if word1 ends with letter a or A

has_the_word_python = ... # bool: True if the sentence has the word python'''
word1 = "Wingardium" # str
word2 = "Leviyosa" # str
word3 = "Silver" # str
sentence = "Learning python is fun"
n1 = 6 # int
n2 = 4 # int

output1 = word1 + ' ' + word2 # str: join word1 and word2 with space in between

output2 = word1[0:4] + '-' + word2[-4:] # str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between

output3 = word1 + ' ' + str(n1) # str: join the word3 and n1 with a space in between

output4 = ('-' * 50) # str: just the hypen "-" repeated 50 times

output5 = ('-' * n2) # str: just the hypen "-" repeated n2 times

output6 = (str(n1) * n2)# str: repeat the number n1, n2 times

are_all_words_equal = word1 == word2 and word2 == word3 and word3 == word1 # bool: True if all three words are equal

is_word1_comes_before_other_two = word1 < word2 and word1 < word3 # bool: True if word1 comes before word2 and word3 assume all words are different

has_h = 'h' in word1 # bool: True if word1 has the letter h

ends_with_a = word1.endswith('a' or 'A') # bool: True if word1 ends with letter a or A

has_the_word_python = 'python' in sentence # bool: True if the sentence has the word python


print(output1)
print(output2)
print(output3)
print(output4)
print(output5)
print(output6)
print(are_all_words_equal)
print(is_word1_comes_before_other_two)
print(has_h)
print(ends_with_a)
print(has_the_word_python)