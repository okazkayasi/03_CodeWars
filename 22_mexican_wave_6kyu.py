# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.
#
# 1.  The input string will always be lower case but maybe empty.
#
# 2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
import string
import time
def wave(str, always = False):
    listed = []
    for i in range(len(str)):
        if str[i] in list(string.ascii_lowercase):
            listed.append(str[:i] + str[i].upper() + str[i+1:])
    j = 0
    # always do
    while always:
        time.sleep(0.15)
        print listed[j]
        j += 1
        if j == (len(str) - 1):
            j = 0
    return listed

print wave("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
