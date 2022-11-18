# Adam Edwards-Uribe
# section 85214-66
# 10/29/22
# Project 10

#A program that prompts the user to enter types of fruit and how many pounds of fruit there are for each fruit
# The program will display the information you entered.
print('This program will let you create a list of fruits and how many')
print('pounds there are of each and then display them back to you.')
print('When you are done please press return without entering a fruit.')
print()

#Loop for user to enter the fruit and weight
fruits = {}
while True:
    name = input('Please enter a type of fruit: ')
    if (name == ""):
        break
    weight = int(input('Please enter the weight of the fruit in pounds: '))
    print()
    fruits[name] = weight
print()


#display the user input
for k in sorted(fruits):
    print('{}       {} lbs.'.format(k, fruits[k]))

print()
#exit message
print('Have a nice day!!!')
