'''Create a class named StringManipulation that has the following specification:

Attributes

words: list of strings, all of which will be in lower case

Methods

(1) __init__: accept a list words as argument and assign it to the corresponding attribute
(2) total_words: return the total number of words in words
(3) count: accept an argument named some_word and return the number of times this word occurs in the list words
(4) words_of_length: accept a positive integer length as argument and return a list of all the words in the list words that have a length equal to length
(5) words_start_with: accept a character char as argument and return the list of all the words in words that start with char
(6) longest_word: return the longest word in the list words; if there are multiple words that satisfy this condition, return the first such occurrence
(7) palindromes: return a list of all the words that are palindromes in words

(1) For those methods where you are expected to return a list of words, make sure that the words in the returned list appear in the order in which they are present in the attribute words.

(2) Each test case corresponds to one or more method calls. We will use S to denote the name of the object.

(3) You do not have to accept input from the user or print output to the console. You just have to define the class based on the specifications given in the question.'''
class StringManipulation:
    def __init__(self, words: list):
        self.words = words

    def total_words(self) -> int:
        return len(self.words)

    def count(self, some_word: str) -> int:
        return self.words.count(some_word)

    def words_of_length(self, length: int) -> list:
        return [word for word in self.words if len(word) == length]

    def words_start_with(self, char: str) -> list:
        return [word for word in self.words if word.startswith(char)]

    def longest_word(self) -> str:
        return max(self.words, key=len)

    def palindromes(self) -> list:
        return [word for word in self.words if word == word[::-1]]
