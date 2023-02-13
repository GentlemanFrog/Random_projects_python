#Celem jest stworzenie małej gry w konnsoli gdzie komputer
#bedzie genenrował losową liczbe a my mamy ją zgadnąć
# podając na wejście nasze sugestie

import random


#funkcja obługująca gessing game:
def guess_number(x):
    random_number = random.randint(1, x)
    #w celu zapobiegniecia sytuacji, w której ta liczba ustawi się na coś dziwnego:
    guess_number = 0
    while guess_number != random_number:
        guess_number = input(f'Zgadnij liczbe od 1 do {x}: ')
        if int(guess_number) < random_number:
            print("Inna liczba. Podana była za niska.")
        elif int(guess_number) == random_number:
            print(f"Liczba została znaleziona! Szukaną byłą {random_number}.")
            exit(0)
        else:
            print("Inna liczba. Podanan była za wysoka.")
        #print(guess_number)

temp_input = input("Podaj gorny zakres: ")
guess_number(int(temp_input))

