# 문제
# 세 개의 리스트를 만들어 아래 순서대로 합병하여 출력하는 프로그램을 작성하라.

# [첫 번째 리스트][세 번째 리스트][세 번째 리스트][세 번째 리스트][두 번째 리스트]

# 첫 번째 리스트:[1, 2, 3]

# 두 번째 리스트:[2, 4, 6]

# 세 번째 리스트:[3, 6, 9] 

# 예제
# [1, 2, 3, 3, 6, 9, 3, 6, 9, 3, 6, 9, 2, 4, 6]


list_1 = [1, 2, 3]
list_2 = [2, 4, 6]
list_3 = [3, 6, 9]

result = list_1 + list_3 * 3 + list_2
a = list_1 , list_2 
print(result)
print(list_1,list_2)
print(a)
print(type(a))