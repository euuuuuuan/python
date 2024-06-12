list1 = [1, 2, 3, 4, 5, 8, 9]
list2 = [3, 4, 6, 7]

common_values = []
for item in list1:
    if item in list2:
        common_values.append(item)

print("공통된 값:", common_values)

# 단계별 동작 원리:
# 리스트 초기화
#
# list1 = [1, 2, 3, 4, 5, 8, 9]
# list2 = [3, 4, 6, 7]
# list1과 list2라는 두 개의 리스트가 초기화됩니다.
# 각각의 리스트에는 숫자들이 들어 있습니다.
# 공통 값을 저장할 리스트 초기화
#
# common_values = []
# common_values라는 빈 리스트가 초기화됩니다.
# 이 리스트는 두 리스트에서 공통된 값을 저장하는 데 사용됩니다.
# 첫 번째 리스트를 순회하며 공통 값 찾기
#

# for item in list1:
#     if item in list2:
#         common_values.append(item)
# list1의 각 요소를 순회합니다.
# item이 list2에 있는지 확인합니다.
# item이 list2에 있으면, common_values 리스트에 추가합니다.


# 각 반복의 동작을 단계별로 설명하면:
#
# 첫 번째 반복 (item = 1):
# 1이 list2에 있는지 확인합니다. (1은 list2에 없습니다.)
# 따라서 common_values에는 추가되지 않습니다.


# 두 번째 반복 (item = 2):
# 2가 list2에 있는지 확인합니다. (2는 list2에 없습니다.)
# 따라서 common_values에는 추가되지 않습니다.


# 세 번째 반복 (item = 3):
# 3이 list2에 있는지 확인합니다. (3은 list2에 있습니다.)
# 3을 common_values에 추가합니다.
# common_values는 이제 [3]입니다.


# 네 번째 반복 (item = 4):
# 4가 list2에 있는지 확인합니다. (4는 list2에 있습니다.)
# 4를 common_values에 추가합니다.
# common_values는 이제 [3, 4]입니다.


# 다섯 번째 반복 (item = 5):
# 5가 list2에 있는지 확인합니다. (5는 list2에 없습니다.)
# 따라서 common_values에는 추가되지 않습니다.


# 여섯 번째 반복 (item = 8):
# 8이 list2에 있는지 확인합니다. (8은 list2에 없습니다.)
# 따라서 common_values에는 추가되지 않습니다.


# 일곱 번째 반복 (item = 9):
# 9가 list2에 있는지 확인합니다. (9는 list2에 없습니다.)
# 따라서 common_values에는 추가되지 않습니다.


# 결과 출력
#
# print("공통된 값:", common_values)
# common_values 리스트를 출력합니다.

# 출력 결과는 공통된 값: [3, 4]입니다.

# 요약
# 이 코드는 두 리스트 list1과 list2를 비교하여
# 공통된 값만 common_values 리스트에 추가합니다.
# 각 요소를 차례대로 비교하며,
# 공통된 요소가 발견되면 common_values에 추가하고,
# 최종적으로 common_values를 출력합니다.



# random 모듈에서 제공하는 기본 기능을 활용하자.
#
# random.sample를 활용하면 중복없이 원하는 수만큼 뽑아낼 수 있다.
# 코드도 간결하고 오류가 날 가능성이 가장 낮기 때문에 이 방법이 가장 좋다고 할 수 있겠다.
import random

a = random.sample(range(1,101),10)
# 1부터 100까지의 범위중에 10개를 중복없이 뽑겠다.
print(a)
