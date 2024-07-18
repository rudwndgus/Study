# 문제
# 공백 하나를 포함한 문자열을 입력 받아, 공백 앞의 문자열과 공백 뒤의 문자열로 분리하여 두 줄에 걸쳐 출력하는 프로그램을 작성하라. 

# 예제
# Fun Python

# 출력
# Fun
# Python

# 풀이

# a = []
# a = (input())
# print("\n".join(a))

a = input().split()

print("\n".join(a))

# https://codinglevelup.tistory.com/69
# 자. 리스트가 있으면 각각의 항목을 분리해서 다음줄에 출력하는건 ㅇㅋ
# 이제그럼 입력값을 받을때 리스트로 받아야 뭔가 진행이되는데
# 그 과정이 저시기였다. split으로 