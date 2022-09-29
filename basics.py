print("Hello World")
x = 100
print(f"Double of {x} is {x*2}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)

print(even)

com = 1 + 2j
print(com)


def euclidean_division(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return (quotient, remainder)


t = euclidean_division(3, 2)
print(t, t[0], t[1])

q, r = euclidean_division(42, 4)
print(q, r)
