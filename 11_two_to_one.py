# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters,
#
#     each taken only once - coming from s1 or s2. #Examples: ```
#a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ```

def longest(s1, s2):
    list1 = sorted(list(s1))
    list2 = sorted(list(s2))
    list3 = []

    while len(list1) > 0 or len(list2) > 0:
        if len(list1) > 0 and len(list2) == 0:
            choose = list1[0]
        elif len(list1) == 0 and len(list2) > 0:
            choose = list2[0]
        else:
            choose = min(list1[0], list2[0])
        if choose not in list3:
            list3.append(choose)
        if choose in list1:
            list1.remove(choose)
        if choose in list2:
            list2.remove(choose)
    return "".join(list3)

def new_one(s1,s2):

    the_list = list(s1)
    the_list.extend(list(s2))
    return "".join(sorted(list(set(the_list))))


print new_one("aretheyhere", "yestheyarehere")
print longest("loopingisfunbutdangerous", "lessdangerousthancoding")
