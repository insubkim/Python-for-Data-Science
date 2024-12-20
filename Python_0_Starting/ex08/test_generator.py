from time import sleep


def yield_test():
    for i in range(5):
        yield i
        sleep(1)
        print(i,'번째 호출!')

print(type(yield_test())) # <class 'generator'>

#CaseA. __next__() 함수를 통해 출력
t = yield_test()
print(t.__next__()) # 0
print(t.__next__()) # 0 번째 호출! 1
print(t.__next__()) # 1 번째 호출! 2
print(t.__next__()) # 2 번째 호출! 3
print(t.__next__()) # 3 번째 호출! 4
print(t.__next__()) #Error

# #for문을 이용하여 출력
# print("<-->")
# for k in yield_test():
#     print(k, 'for 문 호출')
