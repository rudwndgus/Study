# 문제
# 네 단어로 된 문장을 한 줄에 입력받아, 순서를 거꾸로 출력하는 프로그램을 작성하라.​

# 예제
# beauty and the beast

# 출력
# beast the and beauty

# 풀이

sentence = input().split()
reversed_sentence = ' '.join(sentence[::-1])
print(reversed_sentence)