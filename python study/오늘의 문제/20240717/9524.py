# 문제
# 문자열 한 줄을 입력한 후에, 쓸데없는 공백을 제거하여 출력하는 프로그램을 작성하라. (밑줄 친 부분은 공백을 나타낸다.) 

# 예제
# 입력
# _____I like to eat hamburger._____
# 출력
# I like to eat hamburger.

# 힌트
# A = input().strip()
# B = int(input())
# C = float(input())
# 위와 같이 정수나 실수로 변형시키지 않고, 문자열 그대로 사용하는 경우에는 strip()을 사용하여 혹시 모를 공백문자를 제거하고 사용하는 것을 권장한다.

# 풀이

a = input().strip()
print(a)

# a = input()
# str_content = a
# a = ' '.join(str_content.split())
# print(a)

# strip() : 문자열의 앞과 끝의 공백을 없애줌
# replace('앞', '뒤') : 문자열 내부에서 앞의 인자를 뒤의 인자로 바꿔줌
# split() : 문자를 쪼개줌. 인자를 넣어주면 인자를 기준으로 쪼개줌. default값은 공백이다.