#import statement
from math import sqrt, floor
tiles = int(input())

answer = sqrt(tiles)
answer = floor(answer)
#answer = floor(sqrt(tiles))
print(f"The largest square had a side length {answer}")