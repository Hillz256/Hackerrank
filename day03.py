import math
import os
import random
import re
import sys


n = int(input('enter n: '))
print(n)
if 1<=n<=100:
    if n%2 == 1:
        print('Weird')
    elif n%2 == 0 and 2<=n<=5:
        print('Not Weird')
    elif n%2 == 0 and 6<=n<=20:
        print('Weird')
    elif n%2 == 0 and n>20:
        print('Not Weird')
    else:
        print('unkown')
else:
    print('number out of range!')