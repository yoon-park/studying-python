# 변수
a = b = [1, 2, 3]
a[1] = 4
print(b)  # a와 b는 동일한 객체를 참조하고 있으므로 a의 값을 바꾸면 b도 변한다 -> id(a) == id(b)
