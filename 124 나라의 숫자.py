def change124(n):
    return '' if n == 0 else change124((n - 1) // 3) + "412"[n % 3]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(10))
