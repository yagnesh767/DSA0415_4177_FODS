import numpy as np
recovery_times = [5, 7, 8, 10, 12, 14, 15, 17, 20, 22, 25, 28, 30, 35, 40]
percentiles1 = np.percentile(recovery_times,[10])
percentiles2 = np.percentile(recovery_times,[50])
percentiles3 = np.percentile(recovery_times,[90])
print("10th percentile: ",percentiles1)
print("50th percentile: ",percentiles2)
print("90th percentile: ",percentiles3)