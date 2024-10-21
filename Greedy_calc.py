import numpy as np  
# Provided values of V and execution times for the greedy algorithm
v_values = np.array([100, 250, 500, 1000, 2000, 4000, 8000, 16000])
execution_times_greedy = np.array([0.0023, 0.0128, 0.0557, 0.2277, 0.8677, 3.3662, 13.4078, 55.7777])

# Fit a curve (exponential growth) to the data to estimate time complexity
greedy_fit = np.polyfit(v_values, np.log(execution_times_greedy), 1)
greedy_model = np.poly1d(greedy_fit)

# Predict the value of V that can be solved in 30 minutes (1800 seconds)
time_limit_seconds = 30 * 60  # 30 minutes in seconds

# Solve for V where the predicted time = 1800 seconds
predicted_v_30mins_log = (np.log(time_limit_seconds) - greedy_fit[1]) / greedy_fit[0]
predicted_v_30mins = np.exp(predicted_v_30mins_log)
predicted_v_30mins