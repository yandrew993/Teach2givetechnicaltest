
#Question 1: FizzBuzz

# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
#multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
#"FizzBuzz".

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


#Question 2: Fibonacci Sequence

#Write a program to generate the Fibonacci sequence up to 100.


def fib(n):
   fib_numbers = [0, 1]

   while fib_numbers[-1] + fib_numbers[-2] <= n:
       next_fib_number = fib_numbers[-1] + fib_numbers[-2]
       fib_numbers.append(next_fib_number)

   return fib_numbers
n = 100

fib_sequence_generated = fib(n)
print(*fib_sequence_generated)


#Question 3: Power of Two
#Write a program that takes an integer as input and returns true if the input is a power of two.

def power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0

integer_number = int(input("Enter an integer: "))

result = power_of_two(integer_number)

print(f"{integer_number} is a power of two: {result}")
        

#Question 4: Capitalize Words

#Question 4: Capitalize Words
#Write a program that accepts a string as input, capitalizes the first letter of each word in the
#string, and then returns the result string.
#Examples:

#"hi"=> returns "Hi"
#"i love programming"=> returns "I Love Programming"


def capitalize_first_letter(input_string):
    return input_string.title()

example1 = "hi"
example2 = "i love programming"

string1 = capitalize_first_letter(example1)
string2 = capitalize_first_letter(example2)

print(string1)
print(string2) 


#Question 5: Reverse Integer

#Write a program that takes an integer as input and returns an integer with reversed digit
#ordering.
#Examples:

#For input 500, the program should return 5.
#For input -56, the program should return -65.
#For input -90, the program should return -9.
#For input 91, the program should return 19.


def reverse_digits(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num

user_input = int(input("Enter an integer: "))

result = reverse_digits(user_input)

print(f"The integer with reversed digit ordering: {result}")



#Question 6: Count Vowels
#Write a program that counts the number of vowels in a sentence.
#eg " Hello World " => returns 2

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0

    for char in sentence:
        if char in vowels:
            count += 1

    return count

sentence = "Hello World"
result = count_vowels(sentence)
print(f"The number of vowels in the sentence '{sentence}' is: {result}")



                                                                                                                                                                                                                                                                                                                                           


