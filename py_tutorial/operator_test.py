print(-1)
print(0)
print(1)
print(1.1)
print("1+1 =", 1+1)
print('4-2 = ', 4-2)
print("2*2 =", 2*2)
print("4/2 =", 4/2)

import math
print("math.sqrt(4)",math.sqrt(4)) # 2로 제곱한 것이 4
print('math.pow(4,2)', math.pow(4,2)) #  4로 제곱한 것이 16
print('math.pow(4,2)', math.pow(4,3)) #  4로 삼제곱한 것이 64

import random
print('random.random()', random.random())

print(True)
print(False)
print("1 == 1 = ",1 == 1)
print("1 >= 2 = ", 1 >= 2)
print("1 != 2 = ", 1 != 2)

# 012
print(0)
if True:
    print(1)
print(2)

print('----')

# 02
print(0)
if False:
    print(1)
print(2)

print('----')
# 013
print(0)
if True:
    print(1)
else:
    print(2)
print(3)

print('----')
# 023
print(0)
if False:
    print(1)
else:
    print(2)
print(3)

print('----')
print(0)
if True:
    print(1)
elif True:
    print(2)
else:
    print(3)
print(4)

print('----')
print(0)
if False:
    print(1)
elif True:
    print(2)
else:
    print(3)
print(4)

print('----')
print(0)
if False:
    print(1)
elif False:
    print(2)
else:
    print(3)
print(4)


input_id = input('id : ')
id1 = 'egoing'
id2 = 'basta'
if input_id == id:
    print('Welcome')
elif input_id == id2:
    print("Welcome")
#if input_id != id:
else:
    print('Who are you?')

