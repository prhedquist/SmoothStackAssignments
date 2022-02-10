#Smoothstaick Python Basics Day 2b
#Coding Exercise 4
#Patrick Hedquist
#####################################

#Question 1
#Create a list with one number, one word, and one float value. Display the output of the list

list = [45, 'hello', 45.45]
print(list)

#Question 2
#i have a nested list [1,1,[1,2]], how to grab the value of 2 from the list

nlist = [1,1,[1,2]]
print(nlist[2][1])

#Question 3
#lst=['a','b','c'] what is the result of lst[1:]
lst=['a','b','c']
print(lst[1:])

#Question 4
#Create a dictionary with weekdays as keys and week index numbers as values. Assign dictionary to a variable
dict={'Monday':'0', 'Tuesday':'1', 'Wednesday':'2','Thursday':'3', 'Friday': '4' }

#Question 5
#D={'k1':[1,2,3]} what is the output of d[k1][1]
d={'key1':[1,2,3]}
print(d['key1'][1])

#Question 6
#Can you create a list [1,[2,3]] into a tuple
list2=[1,[2,3]]
t = tuple(list2)

#Question 7
#With a single set function can you turn the word Mississippi to distinct character word
print(set('Mississippi'))

#Question 8
#Can you add an element 'X' to the above created set?
s = set('Mississippi')
s.add('X')

#Question 9
#Output of set([1,1,2,3])
print(set([1,1,2,3]))

#Question 10
#Write a program which will find all such members which are divisible by 7 but are not a multiple of 5, between 2000 and 3200
#The numbers obtained should be printed in a comma-separated sequence on a single line.
r = range(2000,3200)
s2 = ''
for n in r:
    if ((n%7) == 0):
        if (not(n%5)):
            s2 = s2 + '%s, ' %(n)

print(s2)
print('\n')

#Question 11 (2 level 1)
#Write a program which can compute the factorial of a given numbers. The results should be brinted in a comma-separated
#sequence on a single line
num = int(input("Input number: "))
total = 1
if num == 0:
    pass
while num > 0:
    total = total * num;
    num -= 1

print(total)
print('\n')

#Question 12 (3 level 1)
#With a given integral numner n, write a program to generate a dictionary that contains (i, i*i) such that is an
#integral number between 1 and n (both included). Then the program should pring the dictionary
n = int(input('Choose Number: '))
dic={}
for i in range(1,n+1):
    dic[i]=i*i
print(dic)
print('\n')

#Question 13 (4 level 1)
#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
#contains every number
seq = input("input comma separated sequence of numbers: ")
list3 = seq.split(',')
t2 = tuple(list3)
print(list3)
print(t2)
print('\n')


