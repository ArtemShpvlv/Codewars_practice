# codewars practice Sh.Artem
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.

def descending_order(num):
    num_list = list(map(int, str(num)))
    num_list = sorted(num_list, key=int, reverse=True)
    num = int(''.join((str(i) for i in num_list)))
    return num
