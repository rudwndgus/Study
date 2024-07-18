# 문제
# 3개의 정수 a, b, c를 입력받아서 a가 b보다 큰지, b가 c보다 크거나 같은지, a가 b보다 작거나 같은지, b가 c보다 작은지를 비교하여 참이면 True, 거짓이면 False을 각각 출력하는 프로그램을 작성하시오. 

# 예제
# 1
# 2
# 2
# False True True False

# 풀이

a = input()
b = input()
c = input()

a = int(a)
b = int(b)
c = int(c)

print(a > b)
print(b >= c)
print(a <= b)
print(b < c)

#프린트 문 안에 "조건문"을 적어두었기 때문에 사실상 질문 같은 느낌이기 때문에 따로 불리언을 적지 않아도 질문에 대답하는 느낌으로 불리언 트루펄스가 나온다.