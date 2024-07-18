
# 문제
# 민수의 키, 민수의 몸무게, 기영이의 키, 기영이의 몸무게를 순서대로 입력받아 민수가 키도 크고 몸무게도 크면 True, 그렇지 않으면 False를출력하는 프로그램을 작성하시오.​​

# 예제
# 150 
# 35
# 145
# 35

# 풀이


False
a = input()
b = input()
c = input()
d = input()

if (a > c and b > d):
    print(True)
else:
    print(False)