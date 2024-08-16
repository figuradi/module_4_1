from fake_math import divide as error
from true_math import divide as infinity


result1 = error(69, 3)
result2 = error(3, 0)
result3 = infinity(49, 7)
result4 = infinity(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)

