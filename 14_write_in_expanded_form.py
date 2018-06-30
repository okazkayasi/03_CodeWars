# Write Number in Expanded Form
#
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
#
# NOTE: All numbers will be whole numbers greater than 0.
#
# If you liked this kata, check out part 2!!

def expanded_form(num):
    aList = []
    digs = len(str(num))
    div = 10 ** (digs-1)
    for i in range(digs):
        x = (num / div) * div
        div /= 10
        num -= x
        if x > 0:
            aList.append(str(x))
    return " + ".join(aList)

print expanded_form(70304)
