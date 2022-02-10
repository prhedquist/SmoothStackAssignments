#Question 14 (5 level 1)
#Define a class which has at least 2 methods
#getString: to get a string from console input
#printString: to print the string in upper case

class InputOutputString(object):
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input("Input string: ")

    def printString(self):
        print(self.s.upper())

testStr = InputOutputString()
testStr.getString()
testStr.printString()


