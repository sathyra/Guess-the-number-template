import random as rn
print("Let's play the number guessing game")
print('Choose the secret number')
secret_num = rn.randint(1, 50)
print('Enter your guesses')
print('Enter the first guess')
guess1 = int(input())
print('Enter the second guess')
guess2 = int(input())
print('Enter the third guess')
guess3 = int(input())
if guess1 > 50 or guess1 < 1 or guess2 > 50 or guess2 < 1 or guess3 > 50 or guess3 < 1:
  print('You have given the invalid entry. Guess the number only in the range of 1 to 50. Result will be calculated now on the correct entries') 
if secret_num == guess1 or secret_num == guess2 or secret_num == guess3:
    print('Your guess is correct, you won the game')
    print('Correct number is :')
    print(secret_num)
elif secret_num < guess1 and secret_num < guess2 or secret_num < guess2 and secret_num < guess3 or secret_num < guess1 and secret_num < guess3:
    print('Your guess was on a higher range')
    print('Correct number is :')
    print(secret_num)
else:
    print('Your guess was on a lower range')
    print('Correct number is :')
    print(secret_num)
