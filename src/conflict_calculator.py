def calculateNumberOfConflicts(position):
    numberOfConflicts = 0

    for i in range(0, len(position)):
        for j in range(i + 1, len(position)):
            if position[i] == position[j]:
                numberOfConflicts += 1
            elif abs(i - j) == abs(position[i] - position[j]):
                numberOfConflicts += 1

    return numberOfConflicts
