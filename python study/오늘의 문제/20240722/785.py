# 문제
# 문자열을 하나 입력받아서 그 문자열의 맨 앞에 있는 문자를 출력한 후, 그 문자열을 리스트로 변환한 후에 해당 리스트의 앞에서부터 세 번째 문자를 출력하는 프로그램을 작성하라. 

# (입력되는 문자열은 항상 길이가 3 이상이라고 가정한다.)​

# 예제
# Eagle
# E
# g

# 풀이 

a = input()
print(a[0])
print(list(a)[2])