

NumPy는 파이썬에서 과학적 계산을 위한 핵심 라이브러리로, 고성능 다차원 배열 객체와 다양한 수학적 함수들을 제공합니다. NumPy를 사용하면 데이터 분석, 수치 계산 등의 작업을 빠르고 효율적으로 할 수 있습니다.

---

## 1. NumPy 설치

NumPy는 `pip` 명령어로 설치할 수 있습니다.

```bash
pip install numpy
2. NumPy 배열 (ndarray)
NumPy에서 배열을 만들려면 numpy.array()를 사용합니다. 배열은 같은 데이터 타입을 가진 요소들이 일렬로 나열된 자료구조입니다.

배열 생성
python
복사
편집
import numpy as np

# 리스트를 이용해 배열 생성
arr = np.array([1, 2, 3, 4, 5])
print(arr)
다차원 배열
python
복사
편집
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
3. 배열 속성
NumPy 배열은 여러 가지 속성을 가지고 있습니다. 주요 속성은 다음과 같습니다.

.shape: 배열의 차원

.dtype: 배열의 데이터 타입

.ndim: 배열의 차원 수

.size: 배열의 요소 개수

python
복사
편집
arr = np.array([[1, 2], [3, 4], [5, 6]])

print(arr.shape)  # (3, 2)
print(arr.dtype)  # int64
print(arr.ndim)   # 2
print(arr.size)   # 6
4. 배열의 연산
NumPy 배열은 벡터화 연산을 통해 매우 빠른 수치 계산을 할 수 있습니다.

산술 연산
python
복사
편집
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 배열 간 연산
sum_arr = arr1 + arr2
print(sum_arr)  # [5, 7, 9]

difference_arr = arr1 - arr2
print(difference_arr)  # [-3, -3, -3]

product_arr = arr1 * arr2
print(product_arr)  # [4, 10, 18]

quotient_arr = arr1 / arr2
print(quotient_arr)  # [0.25, 0.4, 0.5]
브로드캐스팅 (Broadcasting)
NumPy는 배열의 크기가 다를 때도 자동으로 크기를 맞추어 연산할 수 있습니다.

python
복사
편집
arr = np.array([1, 2, 3])
result = arr + 5  # 배열의 모든 요소에 5를 더함
print(result)  # [6, 7, 8]
5. 배열의 인덱싱 및 슬라이싱
NumPy 배열에서는 다양한 방법으로 인덱싱과 슬라이싱을 할 수 있습니다.

1차원 배열
python
복사
편집
arr = np.array([10, 20, 30, 40, 50])
print(arr[2])   # 30
print(arr[1:4])  # [20 30 40]
2차원 배열
python
복사
편집
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[1, 2])  # 6
print(arr_2d[:2, 1:])  # [[2 3] [5 6]]
6. 배열 생성 함수
NumPy는 배열을 생성하는 다양한 방법을 제공합니다.

np.zeros(), np.ones()
python
복사
편집
zeros_arr = np.zeros((3, 3))  # 3x3 크기의 0으로 채워진 배열
print(zeros_arr)

ones_arr = np.ones((2, 4))    # 2x4 크기의 1로 채워진 배열
print(ones_arr)
np.arange()
python
복사
편집
arr = np.arange(0, 10, 2)  # 0부터 10까지 2씩 증가하는 배열
print(arr)  # [0 2 4 6 8]
np.linspace()
python
복사
편집
arr = np.linspace(0, 1, 5)  # 0과 1 사이를 5개의 값으로 나눈 배열
print(arr)  # [0.   0.25 0.5  0.75 1.  ]
7. 배열의 수학적 함수
NumPy는 다양한 수학적 함수들을 제공합니다.

합, 평균, 표준편차 등
python
복사
편집
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))       # 15
print(np.mean(arr))      # 3.0
print(np.std(arr))       # 1.4142135623730951
print(np.min(arr))       # 1
print(np.max(arr))       # 5
배열의 내적
python
복사
편집
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

dot_product = np.dot(arr1, arr2)
print(dot_product)  # 32
8. 배열의 변형
배열의 모양을 변경할 수 있는 함수들을 제공합니다.

np.reshape()
python
복사
편집
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)
np.flatten()
python
복사
편집
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
flattened_arr = arr_2d.flatten()
print(flattened_arr)  # [1 2 3 4 5 6]
9. 배열 결합과 분할
배열 결합
python
복사
편집
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

concatenated = np.concatenate((arr1, arr2))
print(concatenated)  # [1 2 3 4 5 6]
배열 분할
python
복사
편집
arr = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr, 3)
print(split_arr)  # [array([1, 2]), array([3, 4]), array([5, 6])]
10. 고급 기능
난수 생성
python
복사
편집
random_arr = np.random.rand(3, 3)  # 0부터 1 사이의 난수로 채워진 3x3 배열
print(random_arr)

random_int = np.random.randint(1, 10, size=(2, 3))  # 1에서 10 사이의 정수로 채워진 2x3 배열
print(random_int)
난수 시드 설정
python
복사
편집
np.random.seed(42)  # 동일한 난수 생성 시드를 사용
random_arr = np.random.rand(3, 3)
print(random_arr)

