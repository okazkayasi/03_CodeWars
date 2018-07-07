# Given an array arr of strings complete the function landPerimeter by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1piece of land. Some examples for better visualization:
# ['XOOXO',
#  'XOOXO',
#  'OOOXO',
#  'XXOXO',
#  'OXOOO']
#
# should return: "Total land perimeter: 24",

def land_perimeter(arr):
    # first add 0's around
    arounded = []
    length = len(arr[0]) + 2
    arounded.append('O' * length)
    for i in arr:
        s = 'O'+ i + 'O'
        arounded.append(s)
    arounded.append('O' * length)

    # moves
    moves = [[0,1], #right
             [1,0], #down
             [0,-1], #left
             [-1,0]] #up
    count = 0
    for i in range(1, len(arounded)-1):
        for j in range(1, len(arounded[0])-1):
            if arounded[i][j] == 'X':
                for move in moves:
                    x = i + move[0]
                    y = j + move[1]
                    if arounded[x][y] == 'O':
                        count += 1



    for i in arounded:
        print i
    return 'Total land perimeter: {}'.format(count)

land =  ["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]

print land_perimeter(land)
