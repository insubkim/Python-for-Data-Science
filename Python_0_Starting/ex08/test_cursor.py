from time import sleep

for i in range(10):
    for j in range(i):
        if j == 0:
            print('\r', end=" ")
        print('-', end=" ")
    sleep(1)