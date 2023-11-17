# codewars practice Sh.Artem
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)


num = 765
num_list = list(map(int, str(num)))
num_len = len(num_list)
double_num_list = []
var1 = 0
while num_len != 0:
    qnum = num_list[var1] ** 2
    num_len -= 1
    var1 += 1
    double_num_list.append(qnum)
var2 = 0
counter = 0
for current_digit in double_num_list:
    current_digits = current_digit
    while current_digits != 0:
        current_digits = current_digits // 10
        counter += 1
    var2 = var2 * (10 ** counter) + current_digit
    if current_digits == 0:
        counter = 0
print(var2)
