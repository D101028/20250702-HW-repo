import random

while True:
    try:
        level = float(input("Level: "))
        assert level > 0 and int(level) == level
        level = int(level)
        break
    except:
        continue

n = random.randint(1, level)

while True:
    try:
        guess = float(input("Guess: "))
        assert guess > 0 and int(guess) == guess
    except:
        continue
    if guess < n:
        print("Too small!")
    elif guess > n:
        print("Too large!")
    else:
        print("Just right!")
        break

