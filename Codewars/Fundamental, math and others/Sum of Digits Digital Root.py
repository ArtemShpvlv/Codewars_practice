# codewars practice Sh.Artem
# Digital root is the recursive sum of all the digits in a number.
def digital_root(n):
    def sum_of_digits(x):
        x = list(map(int, str(x)))
        x_num = 0
        for num in x:
            x_num += num
        return x_num

    while n >= 10:
        n = sum_of_digits(n)
    return n
