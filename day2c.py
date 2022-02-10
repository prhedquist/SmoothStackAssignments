#Smoothstaick Python Basics Day 2c
#Coding Exercise 6
#Patrick Hedquist
#####################################

#Three is a crowd
list = ['Carter', 'Parker', 'Thomas', 'Ned']

def crowd(list):
    if len(list) > 3:
        print("the room is crowded")

crowd(list)
print('\n')

list.pop()
list.pop()

crowd(list)
print("#################################")
print('\n')

#Three is a crowd part2
list = ['Carter', 'Parker', 'Thomas', 'Ned']

def crowd2(list):
    if len(list) > 3:
        print("the room is crowded")
    else:
        print("the room is not very crowded")

crowd2(list)
list.pop()
list.pop()
print('\n')
crowd2(list)
print("#################################")
print('\n')

#Six is a mob
list2 = ['Carter', 'Parker', 'Thomas', 'Ned', 'Ben', 'Cam', 'Zoe']

def mobTest(list):
    if len(list) > 5:
        print("there is a mob in the room")
    elif ((len(list) > 3) and (len(list) <= 5)):
        print("the room is crowded")
    elif (len(list) == 1 or len(list) == 2):
        print("the room is not very crowded")
    else:
        print("the room is empty")

mobTest(list2)
print('\n')
list2.pop()
list2.pop()
mobTest(list2)
print('\n')
list2.pop()
list2.pop()
mobTest(list2)
