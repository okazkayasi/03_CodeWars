# In this kata, you must create a digital root function.
#
# A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.


def digital_root(n):
    as_string = str(n)
    summed = 0
    for char in as_string:
        summed += int(char)

    # it can be more than one digit again
    str_again = str(summed)
    if len(str_again) < 2:
        return summed
    else:
        return digital_root(summed)

print  digital_root(156)
