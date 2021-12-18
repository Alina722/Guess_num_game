from random import random
answer = (random.randint(1, 100))
user_input = None
alina_inputs = 0
while user_input != answer:

    alina_input = int(input('input number and the number in range  cross 100 : '))

    if alina_input > answer:
        print('min')
    elif alina_input < answer:
        print('big')
    alina_inputs += 1
    if alina_input == answer:
        print("you get it")
    elif alina_inputs >= 15:
        print("game over"+'and the answer is '+str(answer))
        break
