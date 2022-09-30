from random import randint, seed

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [number for number in numbers if number % 2 == 0]
print(even)  # [2, 4, 6, 8, 10]

seed(2)
random_elements = [randint(1, 10) for i in range(5)]
print(random_elements)

seed(2)
random_dictionary = {i: randint(1, 10) for i in range(5)}
print(random_dictionary)

