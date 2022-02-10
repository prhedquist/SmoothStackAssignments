#Smoothstaick Python Basics Day 3a
#Coding Exercise 7
#Patrick Hedquist
#####################################
import random

#Question 1
#Write a python program to find those numbers which are divisble by 7 and a multiple of 5, between 1500 and 2700
r = range(1500,2700)
s2 = ''
for n in r:
    if ((n%7) == 0):
        if (n%5):
            s2 = s2 + '%s, ' %(n)

print(s2)
print('\n')

#Question 2
#Write a python program to convert temperature to and from celsius, fahrenheit
unit = input("type unit(c/f): ")
temp = int(input("provide temperature: "))
if unit == 'f':
    cel = int(((temp-32)*5)/9)
    print(f"{temp} degrees {unit} is {cel} in Celsius")
if unit == 'c':
    fahr = int((temp * (9/5)) + 32)
    print(f"{temp} degrees {unit} is {fahr} in Fahrenheit")


#Question 3
#Write a python program to guess a number between 1 to 9.
rand = random.choice([1,2,3,4,5,6,7,8,9])
guess = 0

while guess != rand:
    guess = int(input("take a guess (1-9): "))

print("well guessed!")
print('\n')

#Question 4
#write a python program to construct the following pattern using a nested for loop
for i in range(5):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(5,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

print('\n')

#Question 6
#Write a python program that accepts a word from the user and reverse it
word = input("type word: ")
print(word[::-1])
print('\n')

#Question 7
#write a python program to count the number of even and odd numbers from a series of numbers
series = tuple(input("input series of numbers: "))
posCount = 0
negCount = 0
print(series)
for i in range(len(series)):
    cur = series[i]
    if (int(cur)%2):
        negCount += 1
    else:
        posCount += 1
print(f"Number of even numbers: {posCount}")
print(f"Number of odd numbers: {negCount}")

print('\n')

#Question 8
#Write a python program that prints each item and its corresponding type from the following list
#datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0,-1),[5,12], {"class":'V',"section":'A'}]
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0,-1),[5,12], {"class":'V',"section":'A'}]

for p in datalist:
    print("{p}", type(p))

print('\n')

#Question 9
#Write a python program that prints all the numbers from 0 to 6 except 3 and 6

for m in range(6):
    if (m == 3) or (m == 6):
        continue
    print(m, end=' ')

print('\n')



