"""
INFO
- Arranging students in two rows before taking photos
- Each row should contain the same number of students
-- reds together
-- blues together
-- back student taller than front student
INPUTS
-- 2 arr of heights > 0 reds and blues
-- same length
RETURN
-- whether complying photo can be taken
"""


def classPhotos(reds, blues):
    reds.sort()
    blues.sort()

    if reds[0] == blues[0]:
        return False

    elif reds[0] > blues[0]:
        for i in range(len(reds)):
            if blues[i] > reds[i]:
                return False

    else:  # reds < blues
        for i in range(len(reds)):
            if blues[i] < reds[i]:
                return False

    return True
