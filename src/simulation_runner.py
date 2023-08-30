import time
from NQueenSolver import NQueen

def run_simulations(NUM_SIMULATIONS, N, K_values, randomRestart, stochastic):
    results = []
    for K in K_values:
        print("K = {}".format(K))
        total_time = 0
        total_count = 0
        for _ in range(NUM_SIMULATIONS):
            start_time = time.time()
            solved, count = NQueen(N, randomRestart, stochastic, K)
            end_time = time.time()
            total_time += end_time - start_time
            total_count += count
        avg_time = total_time / NUM_SIMULATIONS
        avg_count = total_count / NUM_SIMULATIONS
        results.append((avg_time, avg_count))
    return results
