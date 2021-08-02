import random

# numbers ----------------------------
"""
Exercise 1 Guess the number
"""
# def guessing_game():
#     num = random.randint(0, 100)
#     print(num)
#     while True:
#         user_input = input('Guess the number: ')
#         if int(user_input) > num:
#             print('Too high')
#         elif int(user_input) < num:
#             print('Too low')
#         elif int(user_input) == num:
#             print(f'Just right, the answer is {user_input}')
#             break
#
# guessing_game()

"""
Exercise 2 Summing numbers
"""
# def mysum(*nums):
#     s = 0
#     for i in nums:
#         s += i
#     return s
#
# print(mysum(1,3,3))

"""
Exercise 3 Run timing
"""
# def run_timing():
#     total_time = 0
#     number_of_runs = []
#     while True:
#         q = input('Enter 10 km run time: ')
#         if not q:
#             break
#         number_of_runs.append(q)
#         total_time += float(q)
#     avarege = total_time / len(number_of_runs)
#     print(f'Average of {avarege} over {len(number_of_runs)} runs')
#
# run_timing()

"""
Exercise 4 Hexadecimal output
"""
# print(hex(101))
# def hex_output():
#     # list = []
#     # while True:
#     #     hex_num = input('Enter a hex number: ')
#     #     list.append(hex_num)
#     #     # play with enumerate func
#     #     for number, digit in enumerate(list, start=1):
#     #         print(number, int(digit, 16))
#     #     if not hex_num:
#     #         break
#     hex_num = input('Enter a hex number: ')
#     return int(hex_num, 16)
#
# print(hex_output())


# strings ----------------------------
"""
Exercise 5 Pig Latin
"""
# def pig_latin(word):
#     if word[0] in 'aeiou':
#         return f"{word}way"
#     else:
#         return f"{word[1:]}{word[:1]}ay"
#
# print(pig_latin("python"))

"""
Exercise 6 Pig Latin sentence
"""
# def pl_sentence(sen):
#     list = []
#     for word in sen.lower().split():
#         if word[0] in 'aeiou':
#             list.append(f"{word}way")
#         else:
#             list.append(f"{word[1:]}{word[:1]}ay")
#     return " ".join(list)
#
# print(pl_sentence('My test a sentence'))
"""
Exercise 7 Ubbi Dubbi
"""
# def ubbi_dubbi(word):
#     list = []
#     for w in word:
#         if w in 'aeiou':
#             list.append(f"ub{w}")
#         else:
#             list.append(w)
#     return "".join(list)
#
# print(ubbi_dubbi('elephant'))
"""
Exercise 8 Sorting a string
"""
# def strsort():
#     word = input('Type any word: ')
#     # list = []
#     # for w in word:
#     #     list.append(w)
#     # new = sorted(list)
#     # return "".join(new)
#     return ''.join(sorted(word))
# print(strsort())

# lists and tuples ----------------------------
"""
Exercise 9 First-last
"""
# def firstlast(some):
#     return some[:1] + some[-1:]
#
# print(firstlast("hello"))
"""
Exercise 10 Summing anything
"""
# def mysum(*items):
#     if not items:
#         return items
#     output = items[0]
#     for item in items[1:]:
#         output += item
#     return output
#
# print(mysum("hel", "lo"))
"""
Exercise 11 Alphabetizing names
"""
# import operator
#
# PEOPLE = [{
#             'first': 'Erik',
#             'last': 'Arakelyan',
#             'email': 'some@mail.com',
#            },
#            {
#                'first': 'Donald',
#                'last': 'Trump',
#                'email': 'dtrmp@gmail.com',
#            }]
#
# def alphabetize_names(people):
#     return sorted(people, key=operator.itemgetter('last', 'first'))
#      #for dict in sorted(people, key=lambda x: [x['last'], x['first']]):
#      # for dict in sorted(people, key=operator.itemgetter('last', 'first')):
#      #     return f'{dict["last"]} {dict["first"]}: {dict["email"]}'
#
# print(alphabetize_names(PEOPLE))
"""
Exercise 12 Word with most repeated letters
"""
# from collections import Counter
#
# words = ['this', 'is', 'an', 'elementary', 'test', 'exammple']
#
# def most_repeated_letter(word):
#     return Counter(word).most_common(1)[0][1]
#
# def most_repeated_letter_in_word(words):
#     return max(words, key=most_repeated_letter)
#
# print(most_repeated_letter_in_word(words))
"""
Exercise 13 Printing tuple records
"""
# import operator
#
# PEOPLE = [('Donald', 'Trump', 7.85),
#           ('Vladimir', 'Putin', 3.626),
#           ('Jinping', 'Xi', 10.603)]
#
# def format_sort_records(people):
#     list = []
#     template = '{1:10} {0:10} {2:5.2f}' # tricky shit for me (5 characters in number and .2f its a decimal point)
#     for person in sorted(people, key=operator.itemgetter(1, 0)):
#         list.append(template.format(*person)) # splat *
#     return list
#
# print('\n'.join(format_sort_records(PEOPLE)))

# dicts and sets ---------------------------------------------------------
"""
Exercise 14 Restaurant
"""
# MENU = {
#     'salate': 10,
#     'coffe': 5,
#     'cheesecake': 12,
#     'soup': 4,
#     'steak': 22
# }
#
# def restaurant():
#     total = 0
#     while True:
#         order = input('Enter a dish: ')
#         if not order:
#             break
#
#         if order in MENU:
#             total += MENU[order]
#             print(f'{order} costs {MENU[order]}, total is {total}')
#         else:
#             print(f'We are fresh out of {order} today')
#
#
#         # i started do stuff with forloop and it was my mistake, i used MENU.items instead of just MENU const
#         # for key, val in MENU.items():
#         #     if order in key:
#         #         total += val
#         #         print(f'{order} costs {val}, total is {total}')
#         #     if order not in key:
#         #         print(f'We are fresh out of {order} today')
#
#     return f'Your total is {total}'
#
# print(restaurant())
"""
Exercise 15 Rainfall
"""
# def get_rainfall():
#     dict = {}
#     total_rain = 0
#     while True:
#         city = input('City: ')
#         if not city:
#             print(f'total rainfall - {total_rain}')
#             break
#
#         try:
#             rainfall = int(input('Rainfall: '))
#         except ValueError as e:
#             print('Must be integer. Try again \n', e)
#             continue
#
#         dict[city] = rainfall
#         total_rain += rainfall
#
#     return '\n'.join(f'{k.capitalize()}: {v}' for k, v in dict.items())
#
# print(get_rainfall())
"""
Exercise 16 Dictdiff
"""
# d1 = {'a':1, 'b':2, 'c':2}
# d2 = {'a':1, 'b':2, 'c':3}
#
# def dictdiff(x, y):
#     dict = {}
#     keys = x.keys() | y.keys()
#
#     for key in keys:
#         if x.get(key) != y.get(key):
#             dict[key] = [x.get(key), y.get(key)]
#     return dict
#
#
# print(dictdiff(d1, d2))
"""
Exercise 17 How many different numbers?
"""
# numbers = [1, 2, 3, 1, 2, 3, 4, 1]
#
# def how_many_different_numbers(nums):
#     return len(set(numbers))
#
# print(how_many_different_numbers(numbers))

# Files ---------------------------------------------------------
"""
Exercise 18 Final line
"""
# f = 'text.txt'
#
# def get_final_line(file):
#     # my solution was:
#     # list = []
#     # with open (file) as f:
#     #     for line in f:
#     #         list.append(line)
#     # return ''.join(list[-1])
#
#     final_line = ''
#     for current_line in open(file):
#         final_line = current_line
#     return final_line
#
# print(get_final_line(f))
"""
Exercise 19 /etc/passwd to dict
"""
# def passwd_to_dict(filename):
#     dict = {}
#     with open(filename) as f:
#         for line in f:
#             if not line.startswith(('#', '\n')):
#                 new_line = line.split(':')
#                 dict[new_line[0]] = new_line[2]
#     return dict
#
#
# print(passwd_to_dict('passwd.txt'))
"""
Exercise 20 Word count
"""
# def wordcount(filename):
#     chars = 0
#     words = 0
#     lines = 0
#     u_words = set()
#     with open(filename) as f:
#         for line in f:
#             lines += 1
#             words += len(line.split())
#             chars += len(line)
#             u_words.update(line.split())
#         u_words = len(u_words)
#     return f'chars: {chars} \nlines: {lines} \nwords: {words} \nu-words {u_words}'
#
# print(wordcount('wcfile.txt'))
"""
Exercise 21 Longest word per file
"""
# import os
#
# def find_logest_word(filename):
#     word = ''
#     with open(filename) as f:
#         for line in f:
#             for one_word in line.split():
#                 if len(one_word) > len(word):
#                     word = one_word
#     return word
#
# def find_all_logest_words(dirname):
#     return {filename: find_logest_word(os.path.join(dirname, filename))
#             for filename in os.listdir(dirname)
#             if os.path.isfile(os.path.join(dirname, filename))}
#
# print(find_all_logest_words('/Users/Pro/Desktop/IT/fluent-python/files'))
"""
Exercise 22 Reading and writing CSV
"""
# import csv
# def pass_to_csv(passfile, csvfile):
#     with open(passfile) as passwd, open(csvfile, "w") as output:
#         infile = csv.reader(passwd, delimiter=':')
#         outfile = csv.writer(output, delimiter='\t')
#         for record in infile:
#             if len(record) > 1:
#                 outfile.writerow((record[0], record[2]))
#
#
# print(pass_to_csv('passwd.txt', 'csvpass.csv'))
"""
Exercise 23 Json
"""
# import json
# import glob #glob.glob('*.json')
# def print_scores(jfile):
#     dict = {}
#     with open(jfile) as file:
#         data = json.load(file)
#         for i in data:
#             for k,v in i.items():
#                 dict.setdefault(k, []) # nice one
#                 dict[k].append(v)
#     for subject, score in dict.items():
#         min_score = min(score)
#         max_score = max(score)
#         average_score = (sum(score) / len(score))
#         print(f'{str(subject.capitalize())}\nmin: {min_score} | max: {max_score} | average: {average_score}')
#     return ''
#
# print(print_scores('8b.json'))
"""
Exercise 24 Reverse lines
"""
# def reversed(input_file, output_file):
#     text = ''
#     with open(input_file) as f, open(output_file, "w") as output:
#         for data in f:
#             text = data
#             output.write(f'{text.strip()[::-1]}\n')
#
# reversed('files/random.txt', 'files/reverse.txt')

# Functions ---------------------------------------------------------
"""
Exercise 25 XML generator
"""
# def myxml(tagname, content='', **kwargs):
#     attrs = ''.join([f'{k}="{v}" ' for k, v in kwargs.items()])
#     return f'<{tagname} {attrs}>{content}</{tagname}>'
#
# print(myxml('div', 'hello', a=3, b=4))
"""
Exercise 26 Prefix notation calculator
"""
# my solution was
# def calc():
#     math = input('Write down: ')
#     list = []
#     for num in math.split():
#         list.append(num)
#     if list[0] == '+':
#         result = int(list[1]) + int(list[2])
#     elif list[0] == '-':
#         result = int(list[1]) - int(list[2])
#     elif list[0] == '*':
#         result = int(list[1]) * int(list[2])
#     elif list[0] == '/':
#         result = int(list[1]) / int(list[2])
#     return result
#
# print(calc())


# import operator
# def calc():
#     solve = input('Write down: ')
#     operators = {'+': operator.add,
#                  '-': operator.sub}
#     op, first, second = solve.split()
#     return operators[op] (int(first), int(second))
# print(calc())

"""
Exercise 27 Password generator
"""
# import random
# import string
# def create_password_generator(num):
#     numbers = string.digits
#     alpha = string.ascii_letters
#     symbol = string.punctuation
#     output = []
#     new_pass = list(zip(alpha, symbol, numbers))
#     for item in new_pass:
#         for i in item:
#             output.append(i)
#
#     generate = ''.join(random.choices(output, k=num))
#     return generate
#
#
# print(create_password_generator(8))

# Functional programming with comprehemsions ---------------------------------------------------------
"""
Exercise 28 Join numbers
"""
# def join_numbers(numbers):
#     return ', '.join(str(x) for x in range(numbers))
#
# print(join_numbers(15))
"""
Exercise 29 Add numbers
"""
# def sum_numbers(nums):
#     return sum(int(num)
#                for num in nums
#                if num.isdigit())
#
# print(sum_numbers('1 ds 5 akd 2 9'))
"""
Exercise 30 Flatten a list
"""
# def flatten(mylist):
#     return list(i
#                 for l in mylist
#                 for i in l)
#
# print(flatten([[1, 2], [3, 4]]))
"""
Exercise 31 Pig Latin translation of a file
"""
# def plword(word):
#     if word[0] in 'aeiou':
#         return word+ 'way'
#
#     return word[1:] + word[0] + 'ay'
#
# def new_pig_latin(filename):
#     return ' '.join(w
#                    for i in open(filename)
#                    for w in i.split())
#
# print(plword(new_pig_latin('text.txt')))
"""
Exercise 32 Flip a dict
"""
# d = {'a':1, 'b':2, 'c':3}
# def flip(param):
#     flipped = {v: k
#                for k, v in param.items()}
#     return flipped
#
# print(flip(d))
"""
Exercise 33 Transform values
"""
# d = {'a':1, 'b':2, 'c':3}
#
# def calc(val):
#     return int(val) * int(val)
#
#
# def transform_values(params):
#     return {k: calc(v)
#             for k,v in params.items()}
#
# print(transform_values(d))
"""
Exercise 34 Supervocalic words
"""
# def supervocalic(filename):
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     my_list = {i.strip()
#                for i in open(filename)
#                if vowels < set(i.lower())}
#
#     print(my_list)
#
# print(supervocalic('words.txt'))
"""
Exercise 35A Gematria, part1
"""
# import string
#
# def gematria():
#     letters = string.ascii_lowercase
#     return {v: k
#             for k, v in enumerate(letters, 1)}
#
# print(gematria())
"""
Exercise 35B Gematria, part2
"""
# import string
# def gematria():
#     letters = string.ascii_lowercase
#     return {v: k
#             for k, v in enumerate(letters, 1)}
#
# GEMATRIA = gematria()
#
# def gematria_for(word):
#     return sum(GEMATRIA.get(one_char, 0)
#                for one_char in word)
#
#
# def gematria_equal_words(input_word):
#     our_score = gematria_for(input_word.lower())
#     return  [one_word.strip()
#              for one_word in open('words.txt')
#              if gematria_for(one_word.lower()) == our_score]
#
# print(gematria_equal_words('some'))

# modules and packages ----------------------------------------
"""
Exercise 36 Sales tax
"""
# from freedonia import calculate_tax
# test = calculate_tax(500, 'Chico', 2)
# print(test)
"""
Exercise 37 Menu
"""
# from freedonia import menu
#
# def func_a():
#     return "A"
#
# print(menu(a=func_a()))

# Objects ----------------------------------------------------
"""
Exercise 38 Ice cream scoop
"""
# class Scoop():
#     def __init__(self, flavor):
#         self.flavor = flavor
#
# def create_scoop():
#     scoops = [Scoop('vanilla'),
#               Scoop('chocolate'),
#               Scoop('strawberry')]
#
#     flavors = []
#     for scoop in scoops:
#         flavors.append(scoop.flavor)
#
#     return ', '.join(flavors)
#
# print(create_scoop())
"""
Exercise 39 Ice cream bowl
"""
# class Scoop():
#     def __init__(self, flavor):
#         self.flavor = flavor
#
#
# class Bowl():
#     def __init__(self):
#         self.scoops = []
#
#     def add_scoops(self, *scoop):
#         for s in scoop:
#             self.scoops.append(s)
#
#     def __str__(self):
#         return '\n'.join(s.flavor for s in self.scoops)
#
#
# s1 = Scoop('chocolate')
# s2 = Scoop('vanilla')
#
# b = Bowl()
# b.add_scoops(s1, s2)
# print(b)
"""
Exercise 40 Bowl limits
"""
# class Scoop():
#     def __init__(self, flavor):
#         self.flavor = flavor
#
#
# class Bowl():
#     max_scoops = 3
#
#     def __init__(self):
#         self.scoops = []
#
#     def add_scoops(self, *scoop):
#         for s in scoop:
#             if len(self.scoops) < Bowl.max_scoops:
#                 self.scoops.append(s)
#
#     def __str__(self):
#         return '\n'.join(s.flavor for s in self.scoops)
#
#
# s1 = Scoop('chocolate')
# s2 = Scoop('vanilla')
# s3 = Scoop('strawberry')
# s4 = Scoop('coco')
#
# b = Bowl()
# b.add_scoops(s1, s2, s3, s4)
# print(b)
"""
Exercise 41 A bigger bowl
"""
# class Scoop():
#     def __init__(self, flavor):
#         self.flavor = flavor
#
#
# class Bowl():
#     max_scoops = 3
#
#     def __init__(self):
#         self.scoops = []
#
#     def add_scoops(self, *scoop):
#         for s in scoop:
#             if len(self.scoops) < self.max_scoops:
#                 self.scoops.append(s)
#
#     def __str__(self):
#         return '\n'.join(s.flavor for s in self.scoops)
#
#
# class BigBowl(Bowl):
#     max_scoops = 5
#
# s1 = Scoop('chocolate')
# s2 = Scoop('vanilla')
# s3 = Scoop('strawberry')
# s4 = Scoop('coco')
#
# b = BigBowl()
# b.add_scoops(s1, s2, s3, s4)
# print(b)
"""
Exercise 42 FlexibleDict
"""
# class FlexibleDict(dict):
#     def __getitem__(self, key):
#         try:
#             if key in self:
#                 pass
#             elif str(key) in self:
#                 key = str(key)
#             elif int(key) in self:
#                 key = int(key)
#         except ValueError:
#             pass
#
#         return dict.__getitem__(self, key)
#
#
# fd = FlexibleDict()
#
# fd['5'] = 100
# print(fd[5])
"""
Exercise 43 Animals
"""
# class Animal():
#     def __init__(self, color, legs):
#         self.title = self.__class__.__name__
#         self.color = color
#         self.legs = legs
#
#     def __str__(self):
#         return f'{self.color} {self.title} with {self.legs} legs.'
#
#
# class Sheep(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)
#
#
# class Snake(Animal):
#     def __init__(self, color):
#         super().__init__(color, 0)
#
#
# sheep = Sheep('White')
# snake = Snake('Black')
#
# print(snake.color)
"""
Exercise 44 Cages
"""
# class Animal():
#     def __init__(self, color, legs):
#         self.title = self.__class__.__name__
#         self.color = color
#         self.legs = legs
#
#     def __str__(self):
#         return f'{self.color} {self.title} with {self.legs} legs.'
#
#
# class Sheep(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)
#
#
# class Snake(Animal):
#     def __init__(self, color):
#         super().__init__(color, 0)
#
#
# class Wolf(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)
#
#
# sheep = Sheep('White')
# snake = Snake('Black')
# wolf = Wolf('Grey')
#
#
# class Cage():
#     def __init__(self, pk):
#         self.pk = pk
#         self.cage_animals = []
#
#     def add_animals(self, *animals):
#         for animal in animals:
#             self.cage_animals.append(animal)
#
#     def __str__(self):
#         output = f'Cage number {self.pk}\n'
#         output += ', '.join(str(animal)
#                             for animal in self.cage_animals)
#         return output
#
#
# c1 = Cage(1)
# c1.add_animals(sheep, snake)
#
# c2 = Cage(2)
# c2.add_animals(wolf)
#
# print(c2)
"""
Exercise 45 Zoo
"""
# class Animal():
#     def __init__(self, color, legs):
#         self.title = self.__class__.__name__
#         self.color = color
#         self.legs = legs
#
#     def __str__(self):
#         return f'{self.color} {self.title} with {self.legs} legs.'
#
#
# class Sheep(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)
#
#
# class Snake(Animal):
#     def __init__(self, color):
#         super().__init__(color, 0)
#
#
# class Wolf(Animal):
#     def __init__(self, color):
#         super().__init__(color, 4)
#
#
# class Cage():
#     def __init__(self, pk):
#         self.pk = pk
#         self.cage_animals = []
#
#     def add_animals(self, *animals):
#         for animal in animals:
#             self.cage_animals.append(animal)
#
#     def __str__(self):
#         output = f'Cage number {self.pk}\n'
#         output += ', '.join(str(animal)
#                             for animal in self.cage_animals)
#         return output
#
#
# class Zoo():
#     def __init__(self):
#         self.cages = []
#         self.color = []
#         self.legs = []
#
#     def add_cages(self, *cages):
#         for cage in cages:
#             self.cages.append(cage)
#
#     def animals_by_color(self, color):
#         return [animal
#                 for cage in self.cages
#                 for animal in cage.cage_animals
#                 if animal.color == color]
#
#     def animals_by_legs(self, legs):
#         return [animal
#                 for cage in self.cages
#                 for animal in cage.cage_animals
#                 if animal.legs == legs]
#
#     def number_of_legs(self):
#         return sum(animal.legs
#                    for cage in self.cages
#                    for animal in cage.cage_animals)
#
#     def __str__(self):
#         output = ', '.join(str(cage)
#                            for cage in self.cages)
#         return output
#
#
# sheep = Sheep('White')
# snake = Snake('Black')
# wolf = Wolf('Grey')
#
# c1 = Cage(1)
# c1.add_animals(sheep, snake)
#
# c2 = Cage(2)
# c2.add_animals(wolf)
#
#
# z = Zoo()
# z.add_cages(c1, c2)
#
# print(z.animals_by_legs(4))


# Iterators and generators --------------------------------------------
"""
Exercise 46 MyEnumerate
"""

# class MyEnumerate():
#     def __init__(self, data):
#         self.index = 0
#         self.data = data
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise  StopIteration
#         value = (self.index, self.data[self.index])
#         self.index += 1
#         return value
#
#
# for index, letter in MyEnumerate('abc'):
#     print(f'{index} : {letter}')

"""
Exercise 47 Circle
"""
# class CircleIterator():
#     def __init__(self, data, max_times):
#         self.data = data
#         self.max_times = max_times
#         self.index = 0
#
#     def __next__(self):
#         if self.index >= self.max_times:
#             raise StopIteration
#         value = self.data[self.index % len(self.data)]
#         self.index += 1
#         return value
#
# class Circle():
#     def __init__(self, data, max_times):
#         self.data = data
#         self.max_times = max_times
#
#     def __iter__(self):
#         return CircleIterator(self.data, self.max_times)
#
# c = Circle('abc', 5)
# print(list(c))
"""
Exercise 48 All lines, all files
"""
# import os
#
# def all_lines(path):
#     for filename in os.listdir(path):
#         full_filename = os.path.join(path, filename)
#         try:
#             for line in open(full_filename):
#                 yield line
#         except OSError:
#             pass
"""
Exercise 49 Elapsed since
"""
# import time
#
# def elapsed_since(data):
#     last_time = None
#     for item in data:
#         current_time = time.perf_counter()
#         delta = current_time - (last_time or current_time)
#         last_time = time.perf_counter()
#         yield (delta, item)
"""
Exercise 50 MyChain
"""
# def MyChain(*args):
#     for a in args:
#         for item in a:
#             yield item
#
#
# for one_item in MyChain('abc', [1, 2, 3], {'a':1, 'b':2}):
#     print(one_item)