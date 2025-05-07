## Pandas 핵심 기능 요약 (마크다운)

Pandas는 Python 데이터 분석의 핵심 라이브러리로, 강력한 데이터 구조와 분석 도구를 제공합니다.

### 1. Series (1차원 데이터)

* **정의:** 인덱싱된 1차원 배열입니다. 다양한 데이터 타입 저장 가능.
* **생성:**
    ```python
    import pandas as pd
    s = pd.Series([10, 20, 30, 40, 50])
    s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    s = pd.Series({'a': 10, 'b': 20, 'c': 30})
    ```
* **인덱싱/슬라이싱:**
    * 위치 기반: `s[0]`, `s[1:3]`
    * 레이블 기반: `s['a']`, `s['b':'c']`
* **주요 속성:**
    * `.index`: 인덱스 객체
    * `.values`: 값 (NumPy 배열)
    * `.dtype`: 데이터 타입
    * `.name`: Series 이름
* **기본 연산:** 스칼라 연산, 벡터 연산 (같은 인덱스끼리 연산)
* **결측치 처리:** `.isnull()`, `.fillna()`, `.dropna()`

### 2. DataFrame (2차원 데이터)

* **정의:** 행과 열로 이루어진 테이블 형태의 데이터 구조입니다. 각 열은 서로 다른 데이터 타입을 가질 수 있습니다.
* **생성:**
    ```python
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data)

    data = [{'col1': 1, 'col2': 3}, {'col1': 2, 'col2': 4}]
    df = pd.DataFrame(data)

    data = [[1, 3], [2, 4]], columns=['col1', 'col2'], index=['row1', 'row2']
    df = pd.DataFrame(data)
    ```
* **데이터 접근:**
    * 열 선택: `df['col_name']`, `df[['col1', 'col2']]`
    * 행 선택 (레이블 기반): `df.loc['row_label']`, `df.loc[['row1', 'row2']]`, `df.loc['row1':'row2']`
    * 행 선택 (위치 기반): `df.iloc[row_index]`, `df.iloc[[0, 1]]`, `df.iloc[0:2]`
    * 특정 값 접근: `df.loc['row_label', 'col_label']`, `df.iloc[row_index, col_index]`, `df.at['row_label', 'col_label']`, `df.iat[row_index, col_index]`
* **데이터 필터링:**
    ```python
    df[df['col1'] > 1]
    df.query('col2 == 4')
    ```
* **주요 속성:**
    * `.index`: 행 인덱스
    * `.columns`: 열 이름
    * `.values`: 데이터 (NumPy 배열)
    * `.dtypes`: 열별 데이터 타입
    * `.shape`: (행, 열) 크기
    * `.info()`: DataFrame 요약 정보
    * `.describe()`: 통계 정보 요약
* **데이터 정렬:**
    * `.sort_values(by='col_name')`: 특정 열 기준 정렬
    * `.sort_index()`: 인덱스 기준 정렬
* **그룹화 (`groupby()`):** 특정 열을 기준으로 데이터를 그룹화하여 통계 연산 적용
    ```python
    df.groupby('col1').sum()
    df.groupby(['col1', 'col2']).mean()
    ```
* **데이터 결합:**
    * `pd.merge()`: 공통 열 기준으로 병합 (SQL JOIN 유사)
    * `pd.concat()`: 행 또는 열 방향으로 연결
* **데이터 변환:**
    * 새로운 열 추가/수정
    * `.apply()`: 함수를 행 또는 열에 적용
    * `.map()` (Series): 값을 매핑
    * `.replace()`: 값 치환
* **결측치 처리:** `.isnull()`, `.fillna()`, `.dropna()`
* **파일 입출력:**
    * `pd.read_csv()`, `.to_csv()`
    * `pd.read_excel()`, `.to_excel()`
    * 기타 (JSON, SQL 등)

Pandas는 데이터 분석 워크플로우의 핵심 도구이며, 위 기능들을 숙지하는 것은 효율적인 데이터 처리 및 분석의 첫걸음입니다.
