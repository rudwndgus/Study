# 문제
# 두 이름을 입력받아, 첫 줄에는 띄어쓰기를 넣어서 'and'라는 문자열로 구분하고, 둘째 줄에는 띄어쓰기 없이 '&'를 넣어서 출력 예와 같은 문장처럼 출력하는 프로그램을 작성하시오.​​

# 예제
# Spongebob
# Patrick
# Spongebob and Patrick
# Spongebob&Patrick

# 풀이

a = input()
b = input()

print(a,"and",b)
print(a+"&"+b)
