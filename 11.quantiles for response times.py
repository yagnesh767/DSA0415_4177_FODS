import numpy as np
response_times = [120, 150, 180, 200, 220, 250, 300, 350, 400, 450, 500]
percentiles1 = np.percentile(response_times,[25])
percentiles2 = np.percentile(response_times,[50])
percentiles3 = np.percentile(response_times,[75])
print("25th percentile: ",percentiles1)
print("50th percentile: ",percentiles2)
print("75th percentile: ",percentiles3)