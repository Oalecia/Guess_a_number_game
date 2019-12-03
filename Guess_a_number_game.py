print("enter a whole number between 1-10, You have 1 in 10 chance of being correct")
from random import randint
for _ in range(10):
    a=randint(0, 10)
x=int(input())
if x<a:
    print("YOU LOSE! The number you have entered is too low")
if x>a:
    print("YOU LOSE! The number you have entered is too high")
if x==a:
    print("Congratulations, the odds were in your favour, You should enter Hunger games or something")