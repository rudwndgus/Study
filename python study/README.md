# 파이썬

> ## 목차 - 나만의 파이썬 정리노트
1. [출력](#출력)
2. [변수와 입력](#변수와-입력)
3. [연산자](#연산자)

---

## 출력
[목차로 돌아가기](#파이썬)
- 출력을 할때 기본적으로
`print("~~")`
	의 형태를 가지고 사용한다.
- **줄바꿈**을 원할때에는 

   1.  `print("하나쓰고")`<br>
    `print("그리고 하나쓰고")`

	이렇게 프린트문을 두번사용가능하지만



   2.  `print("하나쓰고 \n그리고 하나쓰고")`
   
   이렇게 **\n**을 사용하면 줄바꿈을 편하게 사용할 수 있다.

- print문 안에서 "," 쉼표 사용가능하다!<br>
예를 들어서 "오늘의 문제"를 출력하고 싶을때<br>
  
  ```
  print("오늘의 문제")
  ```
    로 보통 출력하지만

  ```
  print("오늘의","문제")
  ```

    으로 ','를 사용해서 출력이 가능하다.<br>
>  이때 *<u>주의</u>*해야 할 점은 ``','``를 사용하면 자동적으로 **띄어쓰기가 적용**되니 그점 주의 하자!<br>
<br>
>  이때 **띄어쓰고 싶지 않다면** ``"+"``를 사용해보자.

---

 ## 변수와 입력
[목차로 돌아가기](#파이썬)
- 변수를 입력할때 기본적으로

```
변수명 = 값
```
의 형태로 변수를 지정해준다.

```
예시문제

두 개의 변수에 각각 10과 20을 대입한 후 아래와 같이 숫자를 바꾸어 출력하는 프로그램을 작성하시오.

예제 : 20 10
```

```
풀이
a = 10
b = 20

a, b = b, a

print(a, b)
```
>  이때 우선 변수 선언을 해주고 숫자를 바꾸어 출력하는 부분을 ``a, b = b, a``으로 해주었는데, 이 과정은 파이썬이기에 가능한 간단한 과정이다. 만약에 자바, c 였다면 ``temp``라는 잠시 저장할 공간을 만들어서 값을 바꾸기를 해야하지만 파이썬은 그러지 않아도 간단하게 해결이 가능하다.<br>
[예시문제 출처 정올 9507번](https://www.jungol.co.kr/problem/9507?cursor=eyJwcm9ibGVtc2V0IjozLCJmaWVsZCI6MSwiaWR4IjoyfQ==)   

- 두 개의 변수에 각각 10 과 20을 대입하여 그 합을 나타내는 색
```
a = 10
b = 20
print(a, "+", b, "=", a + b)
```
> 위에서 진행했던 방식대로 두개의 변수를 지정해 준 다음, [출력](#출력)부분에서 공부했던 내용처럼 ``print(a, "+", b, "=", a + b)`` 하나의 ``print()``문 안에서 
``a``라는 변수 먼저 출력, 그리고 기호인 ``+``를 넣기 위해 ``"+"``로 넣어준 후 맨뒤에 더한값이 출력될 수 있도록 ``a + b``를 해준다. 그러면 ``10 + 20 = 30``이런 결과가 출력이 된다.

input() 함수로 입력되는 값은 모두 "문자열"이다.
input() 함수를 통해 어떠한 값을 입력받으면 모두 문자열의 형태로 저장되게 됩니다. **이때** 모든 값이 문자열로 저장된다면 생기는 문제점이 있는데 문제점은 

```
문자열로 받으면 생기는 문제

a = input("a의 값을 입력하세요 : ")
b = input("b의 값을 입력하세요 : ")

print(a+b)
```

```
a의 값을 입력하세요 : 10
b의 값을 입력하세요 : 20
1020
```
이런 문제가 발생한다.

그래서 이때는 형 변환을 통해 원하는 형태의 자료형으로 변경을 해주어야 한다.

```
#자료저장 형태 변경하기
a = input("a의 값을 입력하세요 : ")
b = input("b의 값을 입력하세요 : ")
c = bool(input("c의 값을 입력하세요 : "))
print(type(a))
print(type(b))
print(type(c))
a = int(a)
b = float(b)
print(type(a))
print(type(b))
print(type(c))
```

```
b의 값을 입력하세요 : 10.11
c의 값을 입력하세요 : True
<class 'str'>
<class 'str'>
<class 'bool'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

이 방식으로 위의 문제를 올바르게 고쳐보면,
```
문자열로 받으면 생기는 문제

a = input("a의 값을 입력하세요 : ")
b = input("b의 값을 입력하세요 : ")

a = int(a)
b = int(b)

print(a+b)
```
```
a의 값을 입력하세요 : 10
b의 값을 입력하세요 : 20
30
```


> 이렇게 형 변환을 한 상태에서의 주의점은 지정한 형식에 맞게 입력을 해줘야한다는 것이다. 지정한 형식에 어긋나는 형식의 수를 입력시키면?! 오류가 나기 때문이지.

<br>

## 연산자
<br>
연산자의 종류

- 산술 연산자 : [+](#덧셈),[-](#뺄셈),[*](#곱셈),[/](#나눗셈), [%](#나머지-몫-연산), [//](#나머지-몫-연산), [**](#거듭제곱)
- 복합 연산자 : =, +=, -=, *=, /=, %=, //=
- 비교 연산자 : >, >=, <, <=, ==, !=
- 논리 연산 : and, or, not

#### 덧셈
정수, 실수 덧셈


```
num1 = 9; num2 = 3
result = num1 + num2
print(f'result : {result}')

fNum1 = 1.3; fNum2 = 3.14
result = fNum1 + fNum2
print(f'result : {result}')

result = fNum1 + num1
print(f'result : {result}')
```

- 문자(열) 덧셈 : 각 문자를 연결(나열)

```
str1 = 'Good'; str2 = ' '; str3 = 'morning'
result = str1 + str2 + str3
print(f'result : {result}')
```

- 숫자와 문자(열) 덧셈 => 연산이 일어날 수 없는 자료형간에는 오류 발생

```
num1 = 15; str1 = 'hello'
result = num1 + result
```

#### 뺄셈
#### 곱셈
#### 나눗셈
#### 나머지, 몫 연산
#### 거듭제곱



