# for i in range(10):
#     print("i is now {}".format(i))
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
# available_exists = ["east", "north east", "south"]
# #
# # chosen_exit = ""
# # while chosen_exit not in available_exists:
# #     chosen_exit = input("Please choose a direction: ")
# #     if chosen_exit == "quit":
# #         print("Game Over")
# #         break
# # else:
# #     print("aren't you glad you got out of there!")

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0
while guess != answer:
    guess = int(input())
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done, you guessed it")

