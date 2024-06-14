import numpy as np
from scipy import stats
purchase_amounts = [23.50, 45.00, 23.50, 67.20, 23.50, 89.99, 23.50, 150.00, 23-.50, 200.00, 50.00, 75.00, 23.50, 30.00, 45.00]
m = np.mean(purchase_amounts)
print("Mean of the purchase ammounts is ",m)
mode_result = stats.mode(purchase_amounts, keepdims=False)
mode_purchase_amount = mode_result.mode
mode_count = mode_result.count
print(f"Mode of purchase amounts:",mode_purchase_amount," occurs in ",mode_count,"times")
