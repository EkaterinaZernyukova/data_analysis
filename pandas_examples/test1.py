
import numpy as np
A = np.random.normal(5, 2.5, (10, 5))
# matrica = np.random.normal(5, 2.5, (10, 5))
# print(matrica)

sumM=np.sum(A, axis=1)
print(sumM)
mean=np.mean(sumM)
print(mean)

a=sumM[sumM < mean]
print(a)
kol=a.shape[0]
print(kol)

# ##########################################

sum_middle_line = np.sum(A, axis=1)
print(sum_middle_line)
mean_sum_middle_line = np.mean(sum_middle_line)
print(mean_sum_middle_line)

list_sum = sum_middle_line[sum_middle_line < mean_sum_middle_line]
print(list_sum)