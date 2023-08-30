"""
INFO
- faster speed dictates
INPUTS
- 2 lists of positive speeds
-- reds
-- blues
ASSUME
-- reds len is blues len
GOAL
-- pair 1 red and 1 blue
FUNCTION
-- returns maximum possible total speed or minimum of all tandem
-- if fastest --> maximum .. else --> minimum
-- totalSpeed is the sum of speeds of all tandem bicycles
-- total speed is the sum of leading speeds
"""


def tandemBicycle(reds, blues, fastest):
    if len(reds) == 0 or len(blues) == 0:
        return 0

    my_sum = 0

    reds.sort()
    blues.sort()

    if fastest:
        red_idx = 0
        blue_idx = len(blues) - 1
        while red_idx < len(reds):
            my_sum += max(reds[red_idx], blues[blue_idx])
            red_idx += 1
            blue_idx -= 1
    else:
        red_idx = 0
        blue_idx = 0
        while red_idx < len(reds):
            my_sum += max(reds[red_idx], blues[blue_idx])
            red_idx += 1
            blue_idx += 1

    return my_sum
