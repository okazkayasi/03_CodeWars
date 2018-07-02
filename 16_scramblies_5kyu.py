# # Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
# #
# # Notes:
# #
# #     Only lower case letters will be used (a-z). No punctuation or digits will be included.
# #     Performance needs to be considered
#
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def scramble(s1, s2):
    # your code here
    while len(s1) > 0 and len(s2) > 0:
        # take last char out
        s1, result = s1[:-1], s1[-1]
        # take it out of s2 if exists
        s2 = s2.replace(result, "", 1)
    # return if all of s2 is done
    return len(s2) == 0

def scramble2(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    while len(l1) > 0 and len(l2) > 0:
        res = l1.pop()
        if res in l2:
             l2.remove(res)
    return len(l2) == 0



def scramble3(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    the_list = [w1 for w1 in s2 if w1 not in s1]
    return len(the_list) == 0

def scramble4(s1, s2):
    l1 = list(s1)
    the_list = []
    #the_list = [w1 for w1 in s2 if w1 not in l2]
    for w1 in s2:
        if w1 not in l1:
            return False
        l1.remove(w1)


print scramble2('katas', 'steak')
print scramble2('rkqodlw', 'world')
