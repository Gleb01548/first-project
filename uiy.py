from collections import Counter
from re import I
import pandas as pd
# qw = input()
# print(dict(Counter(list(qw))).items())
# for key, num in dict(Counter(list(qw))).items():
#      print(f"В этом числе цифра {key} встречается {num} раз")
      #dfdfdf
# qw = list(input()) dfdfdf
# st = ''
# for i in qw:
#     st += str((9 - int(i))) 
# print(int(st))
# print(''.join(['12', '234']))

# for i in [12, 3, 456, 78]: 
#     print()
    
# print(''.join([str(i) for i in [12, 3, 456, 78]]))

# list_1 = [1, 1]
# list_2 = [1, 1]
# if len(list_1) == len(list_2):
#     if all([list_1[i] == list_2[i] for i in range(len(list_1))]):
#         print('Екгу')
        
#     else:
#         print('ni')

# for x, y in list_1, list_2: 
#     print(x, y)

# list_1 = [1, 2]
# list_2 = [1, 1]

# if len(list_1) == len(list_2):
    
#     if all(
#         [x == y for x in list_1 for y in list_2]
#            ):
#         print('Екгу')
        
#     else: 
#         print('no')
# else:       
#     print('no_1')
# qw = []    
# for i in range(3): 
#     qw.append(int(input()))

# qw_1 = [1 for i in qw if (sum(qw) - i) > i]
# print(len(qw) == len(qw_1))

# qw = []    
# for i in range(3): 
#     qw.append(int(input()))
# qw_1 = [
#     qw[i] - qw[i-1] for i in range(1, len(qw))
#     ]
# print(len(set(qw_1)) == 1)

# qw = []    
# for i in range(2): 
#     qw.append(int(input()))

# print(qw[0] if qw[0] > qw[1] else qw[1])

# qw = (1, 2)
# print(qw)

# c =("A","B")
# c = c +c[3:]

# print(c)

df = pd.DataFrame([[2, 3, 4], 
                   [4, 5, 8]])
print(df)

ser = pd.Series([23, 34, -3, -4, -5])
print(ser[ser<0])