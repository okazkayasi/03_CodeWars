 # Your task is to escape from the carpark using only the staircases provided to reach the exit. You may not jump over the edge of the levels (youre not Superman) and the exit is always on the far right of the ground floor.

  # 1. You are passed the carpark data as an argument into the function.
  # 2. Free carparking spaces are represented by a 0
  # 3. Staircases are represented by a 1
  # 4. Your parking place (start position) is represented by a 2
  # 5. The exit is always the far right element of the ground floor.
  # 6. You must use the staircases to go down a level.
  # 7. You will never start on a staircase.
  # 8. The start level may be any level of the car park.

#   Returns
# 	Return an array of the quickest route out of the carpark
# R1 = Move Right one parking space.
# L1 = Move Left one parking space.
# D1 = Move Down one level.

# Example
# Initialise
#
# carpark = [[1, 0, 0, 0, 2],
#            [0, 0, 0, 0, 0]]
#
# Working Out
#
#     You start in the most far right position on level 1
#     You have to move Left 4 places to reach the staircase => "L4"
#     You then go down one flight of stairs => "D1"
#     To escape you have to move Right 4 places => "R4"
#
# Result
#
# result = ["L4", "D1", "R4"]
#
# Good luck and enjoy!
def escape(carpark):

    # in case we didnt park the car on top
    for k in range(len(carpark)):
        if 2 in carpark[k]:
            carpark = carpark[k:]

    pos = [0, carpark[0].index(2)]
    ret = []

    for i in range(len(carpark)-1):
        # check where the stair is
        stair = carpark[i].index(1)
        # go to the stair and go down
        if stair < pos[1]:
            ret.append("L" + str(pos[1]-stair))
            ret.append("D1")
        elif stair > pos[1]:
            ret.append("R" + str(stair-pos[1]))
            ret.append("D1")
        # if two stair is same column
        else:
            num = int(ret.pop()[1])+1
            ret.append("D" + str(num))
        pos = [pos[0]+1, stair]
    # go to the rightmost place
    stair = len(carpark[0])-1
    if stair > pos[1]:
        ret.append("R" + str(stair-pos[1]))
    return ret

carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

print escape(carpark)
