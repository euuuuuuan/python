# 실습 1 설명
# 밑에 나와 있는 chicken.txt 파일을 보세요.
# 제가 운영하는 치킨집 '코딩에빠진닭(이하 코빠닭)'의 12월 매출이 정리되어 있습니다.
# :의 왼쪽에는 해당 월의 며칠인지, 그리고 오른쪽에는 그 날의 매출이 적혀 있습니다.
# data 폴더의 chicken.txt 파일을 읽어 들이고,
# strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 출력하세요.
# 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다.
# 참고로 현재 제공된 파일에는 31일이 있지만, 어떤 달은 31일이 아닐 수도 있습니다.
# 이 점을 고려해서 확장성 있는 코드를 작성해 주시길 바랍니다.
with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    total_revenue = 0  # 총 매출을 누적보관
    total_days = 0  # 총 일수를 누적보관
    average = 0
    for line in f:
        data = line.strip().split(": ")
        total_revenue += int(data[1])
        # print(revenue)
        # total_revenue += total_revenue
        total_days += 1

    average = total_revenue / total_days
    print(average)


# 해설
# 파일 열기
# 파일 여는 건 영상에서 봤었죠?
#
#
# with open('data/chicken.txt', 'r') as f:
# 일별 매출 출력
# 우선 각 날의 매출을 출력하는 것부터 해 봅시다. strip과 split을 적절히 활용하면 되겠죠?
#
#
# for line in f:
#     data = line.strip().split(": ")
#     revenue = int(data[1])  # 그날의 매출
#     print(revenue)
# 평균 일 매출 구하기
# 우리는 한 달 동안의 평균 일매출을 구하려고 하는데요. 이를 계산하기 위해서 한 달 동안의 총 매출과 한 달 동안의 총 일수를 알아야 합니다. 총 매출과 총 일수를 어떻게 구할 수 있을까요? 총 매출을 누적으로 보관하는 변수 total_revenue를 만듭시다. 마찬가지로 총 일수를 누적으로 보관하는 변수 total_days도 만들겠습니다.
#
#
# total_revenue = 0
# total_days = 0
# 이제 for 반복문의 수행 부분에 들어갈 때마다, 두 값을 업데이트해야겠죠? 그리고 반복문이 끝나고 나서 print(total_revenue / total_days)를 하면 평균 일매출을 출력할 수 있습니다.
#
# 모범 답안
#
# with open('data/chicken.txt', 'r') as f:
#     total_revenue = 0
#     total_days = 0
#
#     for line in f:
#         data = line.strip().split(": ")
#         revenue = int(data[1])  # 그날의 매출
#
#         total_revenue += revenue
#         total_days += 1
#
#     print(total_revenue / total_days)