def boussole(maxPlayer, position, antiHoraire, userPos):
    if maxPlayer == 4:
        if antiHoraire:
            position += 3
            cycle = (3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0)
        else:
            cycle = (0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3)
    else:
        if antiHoraire:
            position += 4
            cycle = (4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0)
        else:
            cycle = (0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4)

    returnList = []

    init = position

    for f in range(maxPlayer):
        playerPos = init + 1
        returnList.append(cycle[playerPos]+1)
        init = playerPos

    return returnList


print(boussole(4, 0, True, 1))
