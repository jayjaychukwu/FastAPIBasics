numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_generator = (number for number in numbers if number % 2 == 0)

even = list(even_generator)
even_bis = list(even_generator)

print(even)
print(even_bis)

# generator function
def even_numbers(max):
    for i in range(2, max + 1):
        if i % 2 == 0:
            yield i
    print("Generator Exhausted")


even = list(even_numbers(10))
print(even)
