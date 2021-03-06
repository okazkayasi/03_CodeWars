# A freak power outage at the zoo has caused all of the electric cage doors to malfunction and swing open...
#
# All the animals are out and some of them are eating each other!
# It's a Zoo Disaster!
#
# Here is a list of zoo animals, and what they can eat
#
#     antelope eats grass
#     big-fish eats little-fish
#     bug eats leaves
#     bear eats big-fish
#     bear eats bug
#     bear eats chicken
#     bear eats cow
#     bear eats leaves
#     bear eats sheep
#     chicken eats bug
#     cow eats grass
#     fox eats chicken
#     fox eats sheep
#     giraffe eats leaves
#     lion eats antelope
#     lion eats cow
#     panda eats leaves
#     sheep eats grass
#
# Kata Task
# INPUT
#
# A comma-separated string representing all the things at the zoo
# TASK
#
# Figure out who eats who until no more eating is possible.
# OUTPUT
#
# A list of strings (refer to the example below) where:
#
#     The first element is the initial zoo (same as INPUT)
#     The last element is a comma-separated string of what the zoo looks like when all the eating has finished
#     All other elements (2nd to last-1) are of the form X eats Y describing what happened
#
# Notes
#
#     Animals can only eat things beside them
#
#     Animals always eat to their LEFT before eating to their RIGHT
#
#     Always the LEFTMOST animal capable of eating will eat before any others
#
#     Any other things you may find at the zoo (which are not listed above) do not eat anything and are not edible
#
# Example
# 	INPUT
# "fox,bug,chicken,grass,sheep"
# 1	fox can't eat bug
# "fox,bug,chicken,grass,sheep"
# 2	bug can't eat anything
# "fox,bug,chicken,grass,sheep"
# 3	chicken eats bug
# "fox,chicken,grass,sheep"
# 4	fox eats chicken
# "fox,grass,sheep"
# 5	fox can't eat grass
# "fox,grass,sheep"
# 6	grass can't eat anything
# "fox,grass,sheep"
# 7	sheep eats grass
# "fox,sheep"
# 8	fox eats sheep
# "fox"
# 	OUTPUT
# ["fox,bug,chicken,grass,sheep", "chicken eats bug", "fox eats chicken", "sheep eats grass", "fox eats sheep", "fox"]

def who_eats_who(zoo):
    eating = ["antelope eats grass", "big-fish eats little-fish", "bug eats leaves",
              "bear eats big-fish", "bear eats bug", "bear eats chicken",
              "bear eats cow", "bear eats leaves", "bear eats sheep",
              "chicken eats bug", "cow eats grass", "fox eats chicken",
              "fox eats sheep", "giraffe eats leaves", "lion eats antelope"
              "lion eats cow", "panda eats leaves", "sheep eats grass"]
    eater = [sent.split()[0] for sent in eating]
    eaten = [sent.split()[2] for sent in eating]
    new_zoo = zoo[:]
    ended = False
    while not ended:
        for i in range(len(new_zoo)-1):
            if new_zoo[i] in eater and new_zoo[i+1] in eaten:
                for j in eater:
                    if eater[j] == new_zoo[i] and eaten[j] == new_zoo[i+1]:
                        new_zoo

    print eater
    print eaten
    # Your code here
    return [zoo, zoo]


input = "fox,bug,chicken,grass,sheep"
who_eats_who(input)
