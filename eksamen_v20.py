import random

def calculate(p_choice, c_choice):
    """
    Calculates who won in Rock paper scissors.
    """
    if p_choice == "Rock" and c_choice == "Paper":
        return "I win.", True
    if p_choice == "Rock" and c_choice == "Scissors":
        return "you win.", False
    if p_choice == "Paper" and c_choice == "Scissors":
        return "I win.", True
    if p_choice == "Paper" and c_choice == "Rock":
        return "you win.", False
    if p_choice == "Scissors" and c_choice == "Rock":
        return "I win.", True
    if p_choice == "Scissors" and c_choice == "Paper":
        return "you win.", False
    return "Draw!", None

def choose(h):
    """
    Tests if the player choice is a valid input.
    """
    hand = ["Rock", "Paper", "Scissors"]
    try:
        if h in hand: 
            return h
        else:
            raise ValueError
    except ValueError:
        print(f"I don't understand {h}. Try again")
        return ""

def rps():
    hand = ["Rock", "Paper", "Scissors"]
    p_score = 0
    c_score = 0
    count = 1
    while True:
        print(f"Let's play round {count}")
        p_hand = choose(input("Your choice (Rock/Paper/Scissors)? "))
        if not p_hand: # checks if p_hand is an empty string
            continue

        """
        Alternativ til å bruke try except
        p_hand = choose("Your choice (Rock/Paper/Scissors)? ")
        while p_hand not in hand:
            print(f"I don't understand {h}. Try again")
            p_hand = choose("Your choice (Rock/Paper/Scissors)? ")
        """

        c_hand = hand[random.randint(0, 2)]
        win = calculate(p_hand, c_hand)
        print(f"My choice was {c_hand} {win[0]}")
        if win[1]:
            c_score += 1 
        elif win[1] == None:
            pass
        else:
            p_score += 1
        print(f"Score: me {c_score}, you {p_score}")
        play = input("Continue (y/n)? ")
        if play == "n":
            break
        count += 1



    """
    her kan
    man
    skrive
    på 
    flere
    linjer
    """
#rps()

import matplotlib.pyplot as plt
import numpy as np
import math

v_0 = 20
g = 9.81

## 1
sequence = np.linspace(0.00, 5.00, 101)

## 2
def calc_x(seq, theta):
    return v_0*seq*math.cos(theta)

def calc_y(seq, theta):
    return v_0*seq*math.sin(theta) - 1/2*g*pow(seq, 2)

## 3

if __name__ == "__main__":
    for angle1 in [30, 45, 60]:
        angle = (math.pi/180)*angle1
        xs = calc_x(sequence, angle)
        ys = calc_y(sequence, angle)
        for i, a in enumerate(ys):
            if a < 0:
                ys = ys[:i]
                xs = xs[:i] 
        plt.plot(xs, ys, ".", label=f"{angle1}°")
    ##4
    plt.ylabel("height/m")
    plt.xlabel("distance/m")
    plt.suptitle("Trajectories. v0 = 20 m/s")
    plt.legend()
    plt.savefig("trajectory.png") ##5
    plt.show()




"""
def main():
    pass
main()

Samme som å skrive if __name__ == '__main__'
"""

'''
Hvordan lage dictionary med input()
d = {}
while True:
    key = input("key: ")
    if key == "":
        break
    value = input("value: ")
    d[key] = value
print(d)

'''

'''
map()
b = [8, 9, 10]

print(list(map(lambda x: x*2, b)))
'''


