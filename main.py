from src.simulation_runner import run_simulations
import numpy as np

NUM_SIMULATIONS = 100
N = 10
K_values = [10, 100, 1000]

if __name__ == "__main__":
    print("Basic Hill Climbing")
    results = run_simulations(NUM_SIMULATIONS, N, np.inf, False, False)
    avg_time, avg_count = results[0], results[1]
    print("Average time: {}".format(avg_time))
    print("Average count: {}".format(avg_count))

    print("Random Restart Hill Climbing")
    results = run_simulations(NUM_SIMULATIONS, N, K_values, True, False)
    avg_time, avg_count = results[0], results[1]
    print("Average time: {}".format(avg_time))
    print("Average count: {}".format(avg_count))

    print("Stochastic Hill Climbing")
    results = run_simulations(NUM_SIMULATIONS, N, np.inf, False, True)
    avg_time, avg_count = results[0], results[1]
    print("Average time: {}".format(avg_time))
    print("Average count: {}".format(avg_count))

    print("Random Restart Stochastic Hill Climbing")
    results = run_simulations(NUM_SIMULATIONS, N, K_values, True, True)
    avg_time, avg_count = results[0], results[1]
    print("Average time: {}".format(avg_time))
    print("Average count: {}".format(avg_count))



