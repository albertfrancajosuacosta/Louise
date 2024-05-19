from scipy.stats import friedmanchisquare

before = [72, 96, 88, 92, 74, 76, 82]

immediately_after = [120, 120, 132, 120, 101, 96, 112]

five_min_after = [76, 95, 104, 96, 84, 72, 76]

res = friedmanchisquare(before, immediately_after, five_min_after)

print(res)
print(res[0],res[1])