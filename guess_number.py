import random

def guess (x):
    random_number = random.randint (1, x)
    guess = 0
    while guess != random_number:
        guess= int (input(f'guest a number betwaeen 1 and {x} : '))
        if guess < random_number :
            print("salah tolong tebak lagi")
        elif guess > random_number :
            print("terlalu tinggi bang")
    print (f'jawaban kamu tepat {random_number}')

def computer_guess (x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c' :
        if low != high:
            guess = random.randint(low, high)
        else :
            guess = low
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C)')
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1

        print (f"anda benar, {guess} jawabannya")


computer_guess (10)
