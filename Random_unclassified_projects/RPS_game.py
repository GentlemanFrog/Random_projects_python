import random


def play_RPS():
    your_wins = 0
    computer_wins = 0
    while True:
        list_of_possible = ["Rock", "Paper", "Scissors"]
        picked_random = random.choice(list_of_possible)
        #print(picked_random)
        user_choice = input("Choose Rock, Paper, Scissors: ")
        if user_choice not in list_of_possible:
            print('You dumbo octopus!!!')
            continue
        if user_choice == picked_random:
            print("Draw")
        elif user_choice == "Rock" and picked_random == "Scissors":
            print(f'You win, computer picked: {picked_random}, {user_choice} beat {picked_random}')
            your_wins += 1
        elif user_choice == "Paper" and picked_random == "Rock":
            print(f'You win, computer picked: {picked_random}, {user_choice} beat {picked_random}')
            your_wins += 1
        elif user_choice == "Scissors" and picked_random == "Paper":
            print(f'You win, computer picked: {picked_random}, {user_choice} beat {picked_random}')
            your_wins += 1
        else:
            print(f'You lose, computer picked: {picked_random} beat {user_choice}')
            computer_wins += 1

        print(f'Your wins: {your_wins}')
        print(f'Computer wins: {computer_wins}')

        if your_wins < computer_wins and computer_wins >= 2:
            print(f'You are really bad at rock, paper, scissors UwU <3.')
            exit(0)
        if your_wins > computer_wins and your_wins >= 2:
            print(f'You are really good at Jan-ken-pon subarashi UwU <3.')
            exit(0)


play_RPS()