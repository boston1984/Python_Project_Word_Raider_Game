import random

with open('words.txt','r') as open_file:
    words = open_file.readlines()

    word_bank = []

    for word in words:
        cleaned_word = word.rstrip().lower()
        word_bank.append(cleaned_word)
        #print(word_bank)

    random_word = random.choice(word_bank)
    #print(random_word)

    letters_incorrect_place = []
    incorrect_letters = []
    max_num_turns = 5
    current_num_turn = 0

    print("Welcome to Word Raider!")
    print('\n')
    print("These are 5 letter words for you to guess. Good luck!")
    print('\n')
    

    while current_num_turn < max_num_turns:
        print(f"You have {max_num_turns-current_num_turn} turns left!")
        guess_word = input("Guess the word: ").lower()
        if not guess_word.isalpha():
            print("Wrong! Please input letters only.")
            continue

        if len(guess_word) != len(random_word):
            print("Please input 5 letters only!")
            continue       

        index = 0
        for char in guess_word:
            if char == random_word[index]:
                print(char, end='')
                if char in letters_incorrect_place:
                    letters_incorrect_place.remove(char)

            elif char in random_word:
                letters_incorrect_place.append(char)
                print('_', end='')

            else:
                if char not in random_word:
                    incorrect_letters.append(char)
                    print('_', end='')
            index += 1

        print(f"Letters in incorrect place: {letters_incorrect_place} ")
        print('\n')
        print(f"Incorrect letters guessed: {incorrect_letters}")

        if guess_word == random_word:
            print("Congratulations!  You guessed right!")
            break

        else:
            print("Wrong!  Guess again!")
            current_num_turn +=1

        if current_num_turn == max_num_turns:
            print(f"Game over! The correct word is {random_word}")
            break

    


        


        

