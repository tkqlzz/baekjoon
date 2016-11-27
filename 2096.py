n = int(input())
dpMax = [0] * 3
dpMin = [0] * 3

for _ in range(n):
    left, center, right = map(int, input().split())
    dpMax[0], dpMax[1], dpMax[2] = max(dpMax[0], dpMax[1]) + left, max(dpMax) + center, max(dpMax[1], dpMax[2]) + right
    dpMin[0], dpMin[1], dpMin[2] = min(dpMin[0], dpMin[1]) + left, min(dpMin) + center, min(dpMin[1], dpMin[2]) + right

print(max(dpMax), min(dpMin))