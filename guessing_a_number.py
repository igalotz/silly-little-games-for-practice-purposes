import random

computer_choice =random.choice(range(1,101))
print(computer_choice)
my_guess = 0

while my_guess != computer_choice:
    try:
        my_guess = int(input("Zgadnij liczbę: "))

    except ValueError:
        print("To nie jest liczba!")

    if my_guess < computer_choice:
        print("Za mało!")

    elif my_guess > computer_choice:
        print("Za dużo!")

    else:
        print("Zgadłeś!")
