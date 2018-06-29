# Given the triangle of consecutive odd numbers:
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
#
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:
#
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8

def row_sum_odd_numbers(n):
    if n == 0:
        return 0
    n = float(n)
    many = (n/2) * (n+1)
    b = n-1
    before = b/2 * (b+1)
    row = many - before
    start_number = before * 2 + 1
    summed = 0
    for i in range(int(row)):
        summed += start_number
        start_number += 2
    return int(summed)

def no_fucking_way(n):
    return n ** 3

print row_sum_odd_numbers(1) #1
print row_sum_odd_numbers(2) #8
print row_sum_odd_numbers(13) # 2197
print row_sum_odd_numbers(19) #6859
print row_sum_odd_numbers(41) #68921
print no_fucking_way(1) #1
print no_fucking_way(2) #8
print no_fucking_way(13) # 2197
print no_fucking_way(19) #6859
print no_fucking_way(41) #68921

print range(1,10,2)
