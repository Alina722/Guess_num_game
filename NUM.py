from random import randint

print("Welcome to the number guessing game!")
print("guess a number between 1 and 300")
num = randint(1, 300)
userinput = None #定義變數
while userinput != num:
    try:
        userinput = int(input("Enter a number: "))
        if userinput > num:
            print('too big')
        elif userinput < num:
            print('too small')
        if userinput == num:
                print('you guessed it!')
                break
    except ValueError:
        print('please enter a number')