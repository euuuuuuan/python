students = ["egoing", "sori", "maru"]
grades = [2, 1, 4]
print("students[1] = ",students[1])
print("len(students) = ", len(students)) # length 원소가 몇개로 이루어져 있는가
print("min(grades) = ", min(grades)) # 가장 작은 값은?
print("max(grades) = ", max(grades)) # 가장 큰 값은?

import statistics # 통계와 관련된 도구
print("statistics.mean(grades) = ",statistics.mean(grades)) # 평균값 구하기

import random
print("random.choice(students)", random.choice(students)) # 리스트를 랜덤하게 뽑아준다.
