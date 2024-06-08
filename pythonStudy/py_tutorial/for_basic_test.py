names = ['egoing', 'basta', 'blackdew'] # 1차원 리스트 배열
for name in names:
    print('Hi, ' + name + ' Bye ' + name)

people = [
    ['egoing', 'Seoul', 'Web'],
    ['bast', 'Seoul', 'IOT'],
    ['blackdew', 'Tongyeong', 'ML'],
]
print(people[0][0])

for person in people:
    print(person[0] + ',' + person[1] + ',' + person[2])

person = ['egoing', 'Seoul', 'Web']
name = person[0]
address = person[1]
interest = person[2]
print(name, address, interest)
# 하지만 이 방법은 귀찮다
# 하단의 방법을 참고하자.

name, address, interest = ['egoing', 'Seoul', 'Web']
print(name, address, interest)

# 12행의 반복문을 개선할 순 없을까?
# 하단의 내용을 보자.
for name, address, interest in people:
    print(name + ', ' + address + ', ' + interest)

print('------------')
# 제어문의 반복문 : Dictionary (사전형)
#{'name': 'egoing', 'address':'Seoul', 'interest':'Web'}
# key : value

person = {'name': 'egoing', 'address':'Seoul', 'interest':'Web'}
print(person['name'])

for key in person:
    print(key)
    print(key, person[key])

    people = [
        {'name': 'egoing', 'address':'Seoul', 'interest':'Web'},
        {'name': 'basta', 'address':'Seoul', 'interest':'Iot'},
        {'name': 'blackdew', 'address':'Tongyeong', 'interest':'ML'}
    ]
print('==== people ====')
for person in people:
    for key in person:
        print(key, ':', person[key])
    print(person)
    print('------------')

