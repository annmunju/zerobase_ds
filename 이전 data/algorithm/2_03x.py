#
# ## 1부터 100까지의 정수 중 2의 배수와 3의 배수를 구분해서 출력하지
# n = 1
# while n < 101:
#     if n%2==0 :
#         print('{}은 2의 배수이다.'.format(n))
#     if n % 3 == 0:
#         print('{}은 3의 배수이다.'.format(n))
#     n+=1
#
# ## 자동차 바퀴가 한번 구를 때마다 0.15mm 마모된다.
# # 현재 바퀴 두께 30mm이고 최소 운행 가능 바퀴 두께가 20mm라 할 때 앞으로 구를 수 있는 횟수
#
# carwheel = 30
# num = 0
#
# while carwheel >= 20 :
#     num += 1
#     carwheel -= 0.15
#
# num-=1
# print(num)
#
# ## 하루에 독감으로 병원에 내방하는 환자수가 50~100명일 때, 누적 독감 환자수가 최초 10000명 넘는 날짜 구하기
# import random
#
# sum = 0
# date = 0
# flag = True
#
# while flag:
#     patientCount = random.randint(50,100)
#     sum += patientCount
#     date +=1
#
#     print('날짜: {},\t 오늘 환자 수: {}, \t 누적 환자 수: {}'.format(date, patientCount, sum))
#
#     if sum >= 10000:
#         flag = False
#
# ## 1에서 100 사이 값들 중 공배수와 최소공배수
# minNum = 0
#
# for i in range(1, 101):
#     if i % 3 != 0 or i % 7 != 0:
#         continue
#
#     print('공배수: {}'.format(i))
#
#     if minNum == 0 :
#         minNum = i
#
# else:
#     print('최소 공배수: {}'.format(minNum))
#
# ## 10의 팩토리얼 계산하는 과정에서 결과값이 50이 넘을 때 숫자를 구하지
# result = 1
# num = 0
# for i in range (1, 11):
#     result *= i
#
#     if result > 50:
#         num = i
#         break
#
# print('num: {}, result: {}'.format(num, result))
#
# ## 새끼 강아지 체중이 2.2kg가 넘으면 이유식을 중단하려고 한다.
# # 한번 이유식 먹을 때 체중이 70g 증가한다고 할 때, 예상되는 이유식 날짜를 구하자. (현재 800g)
# date = 1
# weight = 800
#
# for i in range (1, 100):
#     if weight >= 2200:
#         break
#     date += 1
#     weight += 70
#
#
# print("몸무게 : {}, 이유식 날짜 : {}".format(weight, date))
#
# ## 구구단 전체 출력
# for i in range(1, 10):
#     for j in range(2, 10):
#         result=j*i
#         print('{} * {} = {}\t'.format(j, i, result), end=' ')
#     print()