# codewars practice Sh.Artem
# Given an array of integers, find the one that appears an odd number of times.
def find_it(seq):
    for number in seq:
        seq_count = seq.count(number)
        if seq_count % 2 != 0:
            answ = number
            break
    return (answ)
