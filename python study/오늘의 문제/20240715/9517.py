# 문제
# 3개의 정수 a, b, c를 입력받아서 a와 b, b와 c를 각각 비교하여 같으면 True, 같지 않으면 False를 출력하고, 다음에는 같지 않으면 True, 같으면 False를 출력하는 프로그램을 작성하시오. 

# 예제
# 10
# 20
# 20
# False True True False

# 풀이

a = input()
b = input()
c = input()

a = int(a)
b = int(b)
c = int(c)

if(a==b):
    print("True")
else:
    print("False")

if(b==c):
    print("True")
else:
    print("False")

if(a==b):
    print("False")
else:
    print("True")

if(b==c):
    print("False")
else:
    print("True")