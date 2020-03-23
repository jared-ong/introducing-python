secret = 7
guess = input("Enter a number between 1-10:")
guess = int(guess)
if guess < secret:
    print('Too low')
elif guess > secret:
    print('Too high')
elif guess == secret:
    print('Just right')
else:
    print('Unsure what your guess was')
