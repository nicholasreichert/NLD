import numpy as np
output = " "
coeff = [3.2, 2, 1]
a = np.roots(coeff)
for root in a:
    output = output + str(root)

print(output)