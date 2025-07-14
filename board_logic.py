import random

def print_board(setup):
    print(f"""\n      P2\n\n      {setup[13]}  
A | {setup[0]}   {setup[12]}
B | {setup[1]}   {setup[11]}
C | {setup[2]}   {setup[10]}
D | {setup[3]}   {setup[9]}
E | {setup[4]}   {setup[8]}
F | {setup[5]}   {setup[7]}
      {setup[6]}  

      P1\n""")

def get_setup(isRandom):
    default = [4]*6 + [0] + [4]*6 + [0]
    if isRandom:
        nums = [random.randint(1, 4) for _ in range(6)]
        for i in range(6): default[i], default[i+7] = nums[i], nums[i]
    return default
