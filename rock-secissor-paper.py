import random
computer_choice=random.choice(['rock','paper','secissor'])
user_choice=input("Do yoy want rock,paper,secissor?\n")
if computer_choice==user_choice:
    print("TIE")
elif user_choice=='secissor' and computer_choice=='paper':
    print("You won, Computer lose")
elif user_choice=='paper' and computer_choice=='rock':
    print("You won, Computer lose")
elif user_choice=='rock' and computer_choice=='secissor':
    print("You won, Computer lose")
else:
    print("Computer won, You lose")