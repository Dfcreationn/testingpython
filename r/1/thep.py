from time import sleep as sm
from random import randrange as rm

ui = input("Please enter a number between 0 and 1000")
uii = int(ui)

signal1 = False
signal2 = False

load = 0
b = 0
a = False

if 1000 > uii > 0:
    signal1 = True

else:
    print("ERROR")

while signal1:
    trn = rm(1, 110000000000)
    b = b + 1
    if trn == uii:
        signal2 = True
        print("The number you choosed is perfect")
        signal1 = False


while signal2:
    print("loading")
    sm(3)
    a = True
    while a:
        print(load)
        load = load + 0.5
        sm(0.05)
        if load > 100:
            sm(2)
            print("The result is:")
            sm(1)
            print(b)
            signal2 = False
            a = False
