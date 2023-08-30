from conflict_calculator import calculateNumberOfConflicts
from random import randrange

def bestNeighbor(position):
    min_numberOfConflicts = calculateNumberOfConflicts(position)

    best_position = position
    for i in range(0, len(position)):
        for j in range(0, len(position)):
            if j != position[i]:
                temp = position.copy()
                temp[i] = j
                temp_numberOfConflicts = calculateNumberOfConflicts(temp)
                if temp_numberOfConflicts <= min_numberOfConflicts:
                    min_numberOfConflicts = temp_numberOfConflicts
                    best_position = temp
    return best_position

def randomNeighbor(position):

    candidate_positions = []
    current_numberOfConflicts = calculateNumberOfConflicts(position)

    for i in range(0, len(position)):
      for j in range(0, len(position)):
        if j != position[i]:
          temp = position.copy()
          temp[i] = j
          temp_numberOfConflicts = calculateNumberOfConflicts(temp)
          if temp_numberOfConflicts < current_numberOfConflicts:
            candidate_positions.append(temp)

    if len(candidate_positions) != 0:
      sample_index = randrange(len(candidate_positions))
      return candidate_positions[sample_index]
    else:
      return position
