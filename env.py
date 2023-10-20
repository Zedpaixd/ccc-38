LEVEL = 6
LEVEL_STAGE = 5
LEVEL_IN = "level{}_{}.in".format(LEVEL,LEVEL_STAGE)
LEVEL_OUT = "output{}.out{}".format(LEVEL,LEVEL_STAGE)

## Level 1

# def same_island(matrix, coord1, coord2):
#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
#     def is_valid(x, y, visited):
#         return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 'L' and not visited[x][y]
    
#     def dfs(x, y, target_x, target_y, visited):
#         if (x, y) == (target_x, target_y):
#             return True
#         visited[x][y] = True
#         for dx, dy in directions:
#             new_x, new_y = x + dx, y + dy
#             if is_valid(new_x, new_y, visited) and dfs(new_x, new_y, target_x, target_y, visited):
#                 return True
#         return False

#     visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
#     return dfs(coord1[1], coord1[0], coord2[1], coord2[0], visited)

## Level 2

# import matplotlib.pyplot as plt

# fileLevel = "5"

# with open(f"level3_{fileLevel}.in") as f:
#     lines = [line.strip() for line in f.readlines()]
    
# mapSize = int(lines[0])
# spots = [spots.split(" ") for spots in lines[mapSize + 2:]]
# results = []

# def is_diagonal(previous, current):
#     prev = [int(a) for a in previous.split(",")]
#     curr = [int(a) for a in current.split(",")]
    
#     diffA = abs(prev[0] - curr[0])
#     diffB = abs(prev[1] - curr[1])
        
#     return diffA == diffB

# def getAdjacentCoords(coord):
#     x, y = coord
#     adjacent_coords = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
#     return adjacent_coords

# ii = 1
# for route in spots:
#     seen = []
#     invalid = False
    
#     for i in range(len(route)):
#         previousSpot = route[i - 1] if i - 1 >= 0 else None
#         spot = route[i]
        
#         if spot in seen and not invalid:
#             results.append("INVALID")
#             invalid = True
#             break
        
#         if previousSpot is not None and is_diagonal(previousSpot, spot):
#             prev = [int(a) for a in previousSpot.split(",")]
#             curr = [int(a) for a in spot.split(",")]
#             prevAdj = getAdjacentCoords(prev)
#             currAdj = getAdjacentCoords(curr)
        
#             adjacents = [value for value in prevAdj if value in currAdj]
        
#             if ",".join([str(a) for a in adjacents[0]]) in seen and ",".join([str(a) for a in adjacents[1]]) in seen and not invalid:
#                 invalid = True
#                 results.append("INVALID")
                
#         seen.append(spot)
        
#     if not invalid:
#         results.append("VALID")
        
#     ii += 1

# with open(LEVEL_OUT, "w") as f:
#     for result in results:
#         f.write(result + "\n")

## Input reading 

# with open(LEVEL_IN, "r") as file:
#     matrix_size = int(file.readline().strip())
    
#     matrix = [file.readline().strip() for _ in range(matrix_size)]
    
#     # coordinate_number = int(file.readline().strip())
    
#     # coordinates = [tuple(map(lambda pair: tuple(map(int, pair.split(','))), file.readline().strip().split(' '))) for _ in range(coordinate_number)]

#     path_number = int(file.readline().strip())
    
#     paths = [[tuple(map(int, pair.split(','))) for pair in file.readline().strip().split(' ')] for _ in range(path_number)]

    ## Level 2

    # with open(LEVEL_OUT,"w") as outputFile:
    #     pass

    # for coord_pair in coordinates:
    #     with open(LEVEL_OUT,"a") as outputFile:
    #         coordY,coordX = coord_pair
    #         if (same_island(matrix,coordY,coordX)):
    #             print("SAME", file=outputFile)
    #         else:
    #             print("DIFFERENT", file=outputFile)


# with open(LEVEL_IN) as f:
#     lines = [line.strip() for line in f.readlines()]
    
# mapSize = int(lines[0])
# map = lines[1:mapSize + 1]
# spots = [spots.split(" ") for spots in lines[mapSize + 2:]]

# def exists(a, b):
#     try:
#         map[a][b]
#         return True
#     except:
#         return False
    
# results = []

# def pathFinding(startY, startX, board, targetY, targetX):
#     steps = []
#     seen = []
#     neighbours = [ [-1,0,"U"], [1,0,"D"], [0,-1,"L"], [0,1,"R"], [1,1,"DR"], [1,-1,"DL"], [-1,1,"UR"], [-1,-1,"UL"] ]
    
#     for n in neighbours:
#         newY = startY + n[0]
#         newX = startX + n[1]
#         step = n[2]

#         if exists(newY, newX) and board[newY][newX] == "W":
#             g = {
#                 "steps": [step],
#                 "Y": newY,
#                 "X": newX
#             }

#             steps.append(g)
#             if newY == targetY and newX == targetX:
#                 return g

#             seen.append(str(newY) + "," + str(newX))
    
#     while True:
#         tempSteps = []
#         for step in steps:
#             for n in neighbours:
#                 newY = step["Y"] + n[0]
#                 newX = step["X"] + n[1]
#                 stepHuh = n[2]

#                 sstep = str(newY) + "," + str(newX)
#                 if exists(newY, newX) and board[newY][newX] == "W" and sstep not in seen:
#                     g = {
#                         "steps": step["steps"] + [stepHuh],
#                         "Y": newY,
#                         "X": newX
#                     }

#                     tempSteps.append(g)
#                     seen.append(sstep)

#                     if newY == targetY and newX == targetX:
#                         return g

#         steps = tempSteps

## Level 4 5 6

with open(LEVEL_IN) as f:
    lines = [line.strip() for line in f.readlines()]
    
mapSize = int(lines[0])
map = lines[1:mapSize + 1]
spots = [spots for spots in lines[mapSize + 2:]]

def findFullIsland(spotX, spotY):
    dimensions = [[1,0],[-1,0],[0,1],[0,-1]]
    seen = [[spotX, spotY]]
    
    while True:
        c = len(seen)
        
        for spot in seen:
            for dim in dimensions:
                nSpotX = spot[0] + dim[0]
                nSpotY = spot[1] + dim[1]
                
                if [nSpotX, nSpotY] not in seen and map[nSpotY][nSpotX] == "L":
                    seen.append([nSpotX, nSpotY])
                    
        if len(seen) == c:
            break
        
    return seen

def findIslandSpotsToGo(fullIsland):
    lowestX = [99999, 0]
    lowestY = [0, 99999]
    highestX = [0, 0]
    highestY = [0, 0]
    
    for point in fullIsland:
        if point[0] < lowestX[0]:
            lowestX = point
        if point[0] > highestX[0]:
            highestX = point
        if point[1] < lowestY[1]:
            lowestY = point
        if point[1] > highestY[1]:
            highestY = point
            
    return [[lowestY[0], lowestY[1] - 1], [highestX[0] + 1, highestX[1]], [highestY[0], highestY[1] + 1], [lowestX[0] - 1, lowestX[1]]]

def exists(a, b):
    try:
        map[a][b]
        return True
    except:
        return False

def showBoard(board, currentY, currentX, targetY, targetX):
    return
    print("")
    time.sleep(0.1)
    for y in range(len(board)):
        newX = []
        for x in range(len(board[y])):
            if y == currentY and x == currentX:
                newX.append("⛵")
            elif y == targetY and x == targetX:
                newX.append("❌")
            elif board[y][x] == "L":
                newX.append("🟨")
            else:
                newX.append("🟦")
            
        print("".join(newX))

def pathFinding(startY, startX, board, targetY, targetX):
    steps = []
    seen = []
    neighbours = [ [-1,0,"U"], [1,0,"D"], [0,-1,"L"], [0,1,"R"], [1,1,"DR"], [1,-1,"DL"], [-1,1,"UR"], [-1,-1,"UL"] ]
    
    for n in neighbours:
        newY = startY + n[0]
        newX = startX + n[1]
        step = n[2]

        if exists(newY, newX) and board[newY][newX] == "W":
            g = {
                "steps": [step],
                "Y": newY,
                "X": newX
            }

            steps.append(g)
            if newY == targetY and newX == targetX:
                return g

            seen.append(str(newY) + "," + str(newX))
    
    while True:
        tempSteps = []
        for step in steps:
            for n in neighbours:
                newY = step["Y"] + n[0]
                newX = step["X"] + n[1]
                stepHuh = n[2]

                sstep = str(newY) + "," + str(newX)
                if exists(newY, newX) and board[newY][newX] == "W" and sstep not in seen:
                    g = {
                        "steps": step["steps"] + [stepHuh],
                        "Y": newY,
                        "X": newX
                    }

                    tempSteps.append(g)
                    seen.append(sstep)

                    if newY == targetY and newX == targetX:
                        return g

        steps = tempSteps

def findBeginningSpot(fullIsland):
    lowestPos = [0,0]
    lowest = 9999999
    for pos in fullIsland:
        if sum(pos) < lowest:
            lowest = sum(pos)
            lowestPos = pos
            
    if map[lowestPos[1] - 1][lowestPos[0] - 1] == "W":
        return [lowestPos[0] - 1, lowestPos[1] - 1]
    elif map[lowestPos[1] - 1][lowestPos[0]] == "W":
        return [lowestPos[0], lowestPos[1] - 1]
    elif map[lowestPos[1]][lowestPos[0] - 1] == "W":
        return [lowestPos[0] - 1, lowestPos[1]]

results = []

for spot in spots:
    spot = [int(a) for a in spot.split(",")]
    fullIsland = findFullIsland(spot[0], spot[1])
    beginningSpot = findBeginningSpot(fullIsland)
    POI = findIslandSpotsToGo(fullIsland)
    # POI.append(beginningSpot)
    
    currentSpot = [POI[0][0], POI[0][1]]
    POI.append(POI[0])
    POI = POI[1:]
    
    fullPath = f"{currentSpot[0]},{currentSpot[1]} "
    for poi in POI:
        showBoard(map, currentSpot[1], currentSpot[0], poi[1], poi[0])
        path = pathFinding(currentSpot[1], currentSpot[0], map, poi[1], poi[0])
        
        for step in path["steps"]:
            if step == "U":
                currentSpot[1] -= 1
            elif step == "R":
                currentSpot[0] += 1
            elif step == "D":
                currentSpot[1] += 1
            elif step == "L":
                currentSpot[0] -= 1
            elif step == "DR":
                currentSpot[1] += 1
                currentSpot[0] += 1
            elif step == "DL":
                currentSpot[1] += 1
                currentSpot[0] -= 1
            elif step == "UR":
                currentSpot[1] -= 1
                currentSpot[0] += 1
            elif step == "UL":
                currentSpot[1] -= 1
                currentSpot[0] -= 1
                
            fullPath += f"{currentSpot[0]},{currentSpot[1]} "
            showBoard(map, currentSpot[1], currentSpot[0], poi[1], poi[0])
    
    results.append(" ".join(fullPath.split(" ")[:-2]))

with open(LEVEL_OUT, "w") as f:
    for result in results:
        f.write(result + "\n")