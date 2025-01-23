#Secret number finding
secret_num = 11
guess = int(input("Enter your guess: "))
if secret_num > guess:
    print("Your guess is low")
elif secret_num == guess:
    print('Your guess is correct')
elif secret_num < guess:
    print("Your guess is high")