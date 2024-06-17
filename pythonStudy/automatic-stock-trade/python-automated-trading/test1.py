data = [1, 4, 3, 5, 11]
avg = sum(data) / 5

print(avg)

def ma20(values):
    if len(values) >= 20:
        target_values = values[-20:]
        return sum(target_values) / 20
    else:
        return None

# print(ma20(values))


def ma(values, window_size):
    if len(values) >= window_size:
        target_values = values[-window_size:]
        return sum(target_values) / window_size
    else:
        return None

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
ma5 = []
ma10 = []

for i in range(len(data)):
    ma5.append(ma(data[:i + 1], 5))
    ma10.append(ma(data[:i + 1], 10))
print(ma5)
print(ma10)

# `ma5.append(ma(data[:i + 1], 5))` 구문은 다음과 같은 의미를 가집니다:
#
# 1. `data[:i + 1]`: `data` 리스트의 처음부터 인덱스 `i`까지의 부분 리스트를 만듭니다.
# 즉, `data` 리스트에서 처음부터 현재 인덱스까지의 데이터를 포함한 부분 리스트를 의미합니다.
#
# 2. `ma(data[:i + 1], 5)`: `ma` 함수를 호출하여 인자로 전달합니다.
# 첫 번째 인자로는 `data` 리스트에서 처음부터 현재 인덱스까지의 데이터를 포함한 부분
# 리스트가 전달되고, 두 번째 인자로는 이동평균을 계산할 윈도우 크기인 5를 전달합니다.
#
# 3. `ma5.append(...)`: `ma` 함수의 반환값을 `ma5` 리스트에 추가합니다.
# 따라서 각 인덱스별로 계산된 5일 이동평균 값이 `ma5` 리스트에 순서대로 추가됩니다.
#
# 이 코드는 `data` 리스트의 각 데이터가 추가될 때마다 그 때의 데이터를 포함한
# 부분 리스트를 만들어서 이동평균을 계산하고, 그 값을 `ma5`와 `ma10` 리스트에
# 각각 추가하는 과정을 반복하는 것입니다.
# `ma10`도 마찬가지로 10일 이동평균을 계산하여 저장합니다.