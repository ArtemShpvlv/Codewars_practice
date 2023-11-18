# codewars practice Sh.Artem
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.

def solution(number):
    if number == 0 or number < 0:
        print(0)
    number = number - 1
    answer = 0
    while number != 0:
        if number % 3 == 0 or number % 5 == 0:
            answer += number
        number -= 1
    return answer
