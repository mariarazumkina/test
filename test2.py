file_path = "data.txt"
data = open(file_path,'r')

from my_functions import count_lines, count_words, count_chars

count_lines(data)
count_words(data)
count_chars(data)
