def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

def square_integers(numbers):
    return [num ** 2 for num in numbers]

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)



print("Happy New Year:")
happy_new_year()
print("\nSquared Integers:")
print(square_integers([1, 2, 3, 4, 5]))
print("\nFizzBuzz:")
fizzbuzz()       