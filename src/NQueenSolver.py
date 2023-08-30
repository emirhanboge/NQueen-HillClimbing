import numpy as np
from conflict_calculator import calculateNumberOfConflicts
from neighbor_finder import bestNeighbor, randomNeighbor

def NQueen(N, randomRestart, stochastic, upperBound=np.inf):
    if N in [2, 3]:
        raise ValueError("Failure, no solution exists for given N.")

    solved = False
    current_position = list(np.zeros(N))
    count = 0
    while (calculateNumberOfConflicts(current_position) > 0) and count < upperBound:
        initial_position = [randrange(N) for _ in range(N)]
        current_position = initial_position
        while True:
            if stochastic:
                neighbor = randomNeighbor(current_position)
            else:
                neighbor = bestNeighbor(current_position)

            if calculateNumberOfConflicts(neighbor) >= calculateNumberOfConflicts(current_position):
                if randomRestart:
                    break
                else:
                    if calculateNumberOfConflicts(current_position) != 0:
                        return solved, count
                    else:
                        return True, count

            current_position = neighbor
        count += 1

    if count < upperBound:
        solved = True

    return solved, count
