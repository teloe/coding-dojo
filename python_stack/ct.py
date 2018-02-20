import random

def toss(i):
    head_count = 0
    tail_count = 0

    for x in range(1, i):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            head_count += 1
            result = "head"
        else:
            tail_count += 1
            result = "tail"
        print "Attempt #", x, ": Throwing a coin... It's a ", result, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"

toss(5001)
