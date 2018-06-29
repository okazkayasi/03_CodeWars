# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b.

def array_diff(a, b):
    for element in b:
        # there can be more than one
        while element in a:
            a.remove(element)
    return a


def array_diff_pyt(a,b):
    return [x for x in a if x not in b]

print array_diff([1,2,2,2,3],[2]) == [1,3]
print array_diff_pyt([1,2,2,2,3],[2]) == [1,3]
