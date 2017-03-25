


print("Pomyśl liczbę od zera do tysiąc, a ja ją zgadnę w max 10 próbach")

_min = 0
_max = 1000

while True:
    guess = int((_max - _min) /2) + _min
    print ("Zgaduję.", guess)

    answer = input("(+) za dużo, (-) za mało, (=) zgadłeś")
    
    if answer == "=":
        print("Wygrałem")
        break
    elif answer == "+":
        _max = guess
    elif answer == "-":
        _min = guess
    else:
        print("NIe oszukuj!")







