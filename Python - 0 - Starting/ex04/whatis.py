import sys

count = 0
for argv in sys.argv:
    count = count + 1
    print(count)

assert count != 2, 'ARGUMENT IS NOT ONE'

print('hi')