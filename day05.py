import math
import os
import random
import re
import sys

try:
    N = int(input())
except EOFError:
    print("error")

for i in range(1, 11):
    print(str(N) + " x " + str(i) + " = " + str(N * i))


if __name__ == '__main__':
    try:
        n = int(input().strip())
    except EOFError:
        print(end="")