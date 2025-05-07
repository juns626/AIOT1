# 파이썬 기본 문법

파이썬은 배우기 쉽고 강력한 프로그래밍 언어로, 다양한 데이터 구조와 기능을 제공합니다. 아래는 파이썬의 기본 문법을 설명한 내용입니다.

---

## 1. 주석 (Comments)

주석은 코드에서 설명을 추가하여 코드의 가독성을 높이는 데 사용됩니다. 파이썬에서는 `#`을 이용하여 한 줄 주석을 작성할 수 있습니다. 여러 줄 주석을 작성하려면 `"""` 또는 `'''`을 사용합니다.

### 한 줄 주석

```python
# 이것은 한 줄 주석입니다.
print("Hello, World!")  # 이 부분도 주석입니다.
여러 줄 주석
python
복사
편집
"""
이것은 여러 줄 주석입니다.
두 번째 줄
세 번째 줄
"""
print("Hello, World!")
2. 변수 (Variables)
파이썬에서 변수는 값을 저장하는데 사용됩니다. 변수의 타입을 명시하지 않고, 값에 따라 타입이 자동으로 결정됩니다.

python
복사
편집
x = 10      # 정수형 변수
y = 3.14    # 실수형 변수
name = "Alice"  # 문자열형 변수
3. 데이터 타입 (Data Types)
파이썬에서 사용되는 주요 데이터 타입은 다음과 같습니다.

정수 (Integer)
python
복사
편집
age = 25
실수 (Float)
python
복사
편집
pi = 3.14159
문자열 (String)
python
복사
편집
greeting = "Hello"
불리언 (Boolean)
python
복사
편집
is_active = True
is_false = False
리스트 (List)
python
복사
편집
fruits = ["apple", "banana", "cherry"]
튜플 (Tuple)
python
복사
편집
coordinates = (10, 20)
딕셔너리 (Dictionary)
python
복사
편집
person = {"name": "John", "age": 30}
집합 (Set)
python
복사
편집
unique_numbers = {1, 2, 3}
4. 연산자 (Operators)
파이썬에서 사용되는 다양한 연산자는 다음과 같습니다.

산술 연산자
python
복사
편집
a = 10
b = 5
print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
print(a / b)  # 나눗셈
print(a % b)  # 나머지
print(a ** b) # 거듭제곱
print(a // b) # 몫
비교 연산자
python
복사
편집
print(a == b)  # 같음
print(a != b)  # 다름
print(a > b)   # 크다
print(a < b)   # 작다
print(a >= b)  # 크거나 같다
print(a <= b)  # 작거나 같다
논리 연산자
python
복사
편집
print(True and False)  # 논리적 AND
print(True or False)   # 논리적 OR
print(not True)        # 논리적 NOT
5. 조건문 (Conditionals)
조건문은 주어진 조건에 따라 코드의 흐름을 제어합니다. if, elif, else를 사용하여 다양한 조건을 처리할 수 있습니다.

python
복사
편집
x = 10
if x > 5:
    print("x는 5보다 큽니다.")
elif x == 5:
    print("x는 5입니다.")
else:
    print("x는 5보다 작습니다.")
6. 반복문 (Loops)
반복문은 주어진 조건이나 범위에 따라 코드를 반복 실행합니다.

for 문
python
복사
편집
for i in range(5):  # 0부터 4까지
    print(i)
while 문
python
복사
편집
i = 0
while i < 5:
    print(i)
    i += 1
7. 함수 (Functions)
함수는 특정 작업을 수행하는 코드 블록입니다. def 키워드를 사용하여 함수를 정의합니다.

python
복사
편집
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
매개변수와 리턴값
python
복사
편집
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
8. 리스트 컴프리헨션 (List Comprehension)
리스트 컴프리헨션을 사용하면 더 간결하게 리스트를 생성할 수 있습니다.

python
복사
편집
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)  # [1, 4, 9, 16, 25]
9. 클래스 (Classes)
파이썬은 객체 지향 프로그래밍을 지원합니다. 클래스는 객체를 정의하는 틀로 사용됩니다.

python
복사
편집
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, 저는 {self.name}이고, {self.age}살입니다.")

person1 = Person("Alice", 25)
person1.introduce()
10. 예외 처리 (Exception Handling)
예외 처리기법은 코드 실행 중에 발생할 수 있는 오류를 처리합니다.

python
복사
편집
try:
    x = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
11. 파일 입출력 (File I/O)
파일을 열고 읽거나 쓸 수 있습니다.

파일 열기
python
복사
편집
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()
파일 읽기
python
복사
편집
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
12. 모듈과 패키지 (Modules and Packages)
파이썬에서는 다양한 외부 모듈을 import하여 사용할 수 있습니다. 예를 들어, math 모듈을 사용하여 수학 관련 기능을 추가할 수 있습니다.

python
복사
편집
import math
print(math.sqrt(16))  # 제곱근 구하기
