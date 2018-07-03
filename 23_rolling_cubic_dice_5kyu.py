# When we throw 2 classical dice (values on each side from 1 to 6) we have 36 (6 * 6) different results.
#
# We want to know the probability of having the sum of the results equals to 11. For that result we have only the combination of 6 and 5. So we will have two events: {5, 6} and {6, 5}
#
# So the probability for that result will be:
#
# P(11, 2) = 2/(6*6) = 1/18    (The two is because we have 2 dice)
#
# Now, we want to calculate the probability of having the sum equals to 8. The combinations for that result will be the following: {4,4}, {3,5}, {5,3}, {2,6}, {6,2} with a total of five combinations.
#
# P(8, 2) = 5/36
#
# Things may be more complicated if we have more dices and sum values higher.
#
# We want to know the probability of having the sum equals to 8 but having 3 dice.
#
# Now the combinations and corresponding events are:
#
# {2,3,3}, {3,2,3}, {3,3,2}
# {2,2,4}, {2,4,2}, {4,2,2}
# {1,3,4}, {1,4,3}, {3,1,4}, {4,1,3}, {3,4,1}, {4,3,1}
# {1,2,5}, {1,5,2}, {2,1,5}, {5,1,2}, {2,5,1}, {5,2,1}
# {1,1,6}, {1,6,1}, {6,1,1}
#
# A total amount of 21 different combinations
#
# So the probability is:
# P(8, 3) = 21/(6*6*6) = 0.09722222222222222
#
# Summarizing the cases we have seen with a function that receives the two arguments

def rolldice_sum_prob(sum_, dice_amount):
    dices = range(1,7)
    print dices
    sols = []
    print sols
    hold = range(1,7)
    each = [0] * dice_amount
    for i in range(6**dice_amount):
        add = 0
        for k in range(len(each)):
            add += dices[each[k]]
        sols.append(add)
        each[0] += 1
        for j in range(len(each)-1):
            if each[j] == 6:
                each[j+1] += 1
                each[j] = 0
    print sols
    return (sols.count(sum_)*1.0 / len(sols))



print rolldice_sum_prob(11,2)
