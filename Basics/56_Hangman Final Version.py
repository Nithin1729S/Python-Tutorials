import random
import Hangman_Art

End_of_the_game=False
lives=6
display=[]
random_word=random.choice(Hangman_Art.word_list)

for i in range(len(random_word)):
    display+="_"

print(Hangman_Art.logo)

while not End_of_the_game:
    guess=input("Guess a Word: ").lower()

    if guess in display:
        print(f"You have already entered {guess}")


    for i in range(len(random_word)):
        letter=random_word[i]
        if letter==guess:
            display[i]=guess
    print(f"{''.join(display)}")


    if guess not in random_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives==0:
            End_of_the_game=True
            print(f"You Lose.The Correct answer is {random_word} ")



    if "_" not in display:
        print("You Win!!!")

    print(Hangman_Art.stages[lives])


