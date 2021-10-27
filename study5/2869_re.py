import sys
sys.stdin = open('2869_input.txt')
import math

day, night, end = map(int, input().split())
print(math.ceil((end-night)/(day-night)))