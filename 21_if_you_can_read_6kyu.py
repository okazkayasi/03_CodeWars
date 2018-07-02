# The idea for this Kata came from 9gag today.here
#
# You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet) wiki.
#
# Like this:
#
# Input: If you can read
#
# Output: India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta
#
# Some notes  Some notes
#
#     Keep the punctuation, and remove the spaces.
#     Use Xray without dash or space.

import string
def to_nato(words):
    listed = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
    lowered = [i[0].lower() for i in listed]
    dicted = dict(zip(lowered, listed))
    ret_str = ""
    for each in words:
        if each != " ":
            if each.lower() in dicted:
                ret_str += dicted[each.lower()] + " "
            else:
                ret_str += each + " "
    return ret_str[:len(ret_str)]

print to_nato('If you can read')
