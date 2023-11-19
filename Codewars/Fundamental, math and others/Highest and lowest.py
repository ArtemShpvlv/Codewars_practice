# codewars practice Sh.Artem
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
def high_and_low(numbers):
    numbers = numbers.split()
    numbers_len = len(numbers)
    numbers = sorted(numbers, key=int, reverse=True)
    if numbers_len > 1:
        del numbers[1:numbers_len - 1]
        numbers = " ".join(numbers)
    else:
        numbers = numbers + numbers
        numbers = " ".join(numbers)
    return numbers
