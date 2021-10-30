def getNearNum(an):

    baseScores = [95, 85, 75, 65, 55]
    nearNum = 0
    minNum = 100

    for n in baseScores:
        absNUm = abs(n - an)
        if absNUm < minNum:
            minNum = absNUm
            nearNum = n

    if nearNum == 95:
        return 'A'
    elif nearNum == 85:
        return 'B'
    elif nearNum == 75:
        return 'C'
    elif nearNum == 65:
        return 'D'
    else:
        return 'F'