# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#
# Example:
#
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
#
# Notes:
#
#     All numbers are valid Int32, no need to validate them.
#     There will always be at least one number in the input string.
#     Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):
    listed = numbers.split()
    print listed
    int_listed = [int(x) for x in listed]
    sorted_listed = sorted(int_listed)
    return "{} {}".format(sorted_listed[-1], sorted_listed[0])
    # return str(sorted_listed[-1]) + " " + str(sorted_listed[0])

print high_and_low("1 2 3 4 5")  # return "5 1"
