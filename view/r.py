import numpy as np

from scipy.stats import anderson

rng = np.random.default_rng()

data = rng.random(size=35)

res = anderson(data)

print(res.statistic)

print(res.critical_values)

print(res.significance_level)

cvalor = int(np.where(res.significance_level==1.)[0])

print(res.critical_values[cvalor])
#print(cvalor)
