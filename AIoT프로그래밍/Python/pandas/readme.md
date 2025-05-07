import pandas as pd

# 리스트로부터 생성
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

# 딕셔너리로부터 생성 (키가 인덱스가 됨)
s2 = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(s2)
