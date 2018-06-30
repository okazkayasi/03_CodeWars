# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob  to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

#
# ##Examples :
#
# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
#
# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
#

def iq_test(numbers):
    # use modulo for checking
    x = [int(no) % 2 for no in numbers.split()]
    print x
    even = x.index(0) + 1
    odd = x.index(1) + 1
    # remove one from each so only general evenness left
    x.remove(0)
    x.remove(1)
    if x[0] == 0:
        return odd
    return even

print iq_test("2 4 7 8 10")
