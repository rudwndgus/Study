# 문제
# 두 개의 문자열과 한 개의 정수를 입력 받아서, 뒤의 문자열을 입력받은 수만큼, 연속해서 출력하고, 앞의 문자열을 이어서 출력하는 프로그램을 작성하시오.​ 

# 예제
# Wolf
# Sheep
# 3
# SheepSheepSheepWolf

# 풀이

a = input()
b = input()
n = int(input())

print(b*n+a)