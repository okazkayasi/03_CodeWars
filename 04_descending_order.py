# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
#
# Input: 21445 Output: 54421
#
# Input: 145263 Output: 654321
#
# Input: 1254859723 Output: 9875543221

def Descending_Order(num):
    # use char instead of digit
    as_str = str(num)
    as_list = [char for char in as_str]
    as_list.sort(reverse=True)
    ordered = ""
    for number in as_list:
        ordered += number
    return int(ordered)

print Descending_Order(145263)
