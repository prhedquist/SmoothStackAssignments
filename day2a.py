#Smoothstaick Python Basics Day 2a
#Coding Exercise 3
#Patrick Hedquist
#####################################

#Question 1
#write a string that returns the letter 'r' from 'Hello world'
#For example, 'Hello World'[0] returns 'H'. It should be one line of code
#dont assign a variable to the string

print('Hello world'[8])

#Question 2
#String slicing to grab the word 'ink' from the word 'thinker'
#S='hello' what is the output of h[1]? Answer: 'e'

print('thinker'[2:5])
print('\n')

#Question 3
#S='Sammy' what is the output of S[2:]? Answer: mmy

print('Sammy'[2:])
print('\n')

#Question 4
#With a single set function can you turn the word 'Mississippi' to distinct chatacter word?

print(set('Mississippi'))
print('\n')

#Question 5
#The word or whole phase which has the same sequence of letters in both directions is called a palindrome
#Here are a few examples
#   Stats
#   Amore, rose
#   No 'x' in Nixon
#   Was it a cat I saw?
#your goal is to determine whether the phrase represents a palindrome or not


input1 = input("Enter word to test: ")                  #prints "Enter word to test: " and user can input a word
list = [input1]                                         #creates a list using the word user inputted
cont = input("add another word?(y/n)")                  #ask user if they want to add new word

while cont != 'n':                                      #checks if answer is NOT n
    if cont == 'y':                                     #checks if answer was y
        input2 = input("Enter word to test: ")          #input word prompt
        list = list + [input2]                          #update list
    cont = input("add another word?(y/n)")              #ask user if they want new word

for i in list:                                          #prints items in list on new lines
    print(i)

ans = []


def palindrome(pal):                                   #algorithm based off code from Sachin Bisht on geeksforgeeks
    j = 0
    k = len(pal)-1
    pal = pal.lower()

    while (j <= k):                                    #while loop to iterate through list and test palindromes
        if(not(pal[j] >= 'a' and pal[j] <= 'z')):
            j += 1
        elif (not(pal[k] >= 'a' and pal[k] <= 'z')):
            k -= 1
        elif (pal[j] == pal[k]):
            j += 1
            k -= 1
        else:
            return False
    return True

for i in list:
    if(palindrome(i)):
        ans = ans + ['Y']
    else:
        ans = ans + ['N']

print(len(list))
print(ans)                                              #print ans list














