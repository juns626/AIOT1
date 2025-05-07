# Pandas 기본 기능 및 대표 기능

<div align="center">
  <button onclick="copyToClipboard()">전체 내용 복사</button>
</div>
<br>

Pandas는 Python에서 데이터 분석 및 조작을 위한 핵심 라이브러리입니다. `Series` (1차원 배열)와 `DataFrame` (2차원 테이블)을 중심으로 다양한 기능을 제공합니다.

### Series

* **생성:**
    ```python
    import pandas as pd; s1 = pd.Series([10, 20, 30]); s2 = pd.Series({'a': 1, 'b': 2})
    ```
* **인덱싱/슬라이싱:** `s1[0]`, `s2['a']`, `s1[0:2]`, `s2['a':'b']`
* **속성:** `.index`, `.values`, `.dtype`, `.name`
* **연산:** `s1 + 10`, `s1 * s2` (인덱스 기반 연산)
* **결측치 처리:** `.isnull()`, `.fillna(0)`, `.dropna()`

### DataFrame

* **생성:**
    ```python
    data = {'col1': [1, 2], 'col2': [3, 4]}; df = pd.DataFrame(data)
    data_list = [{'col1': 1, 'col2': 3}, {'col1': 2, 'col2': 4}]; df_list = pd.DataFrame(data_list)
    ```
* **데이터 접근:**
    * 열: `df['col1']`, `df[['col1', 'col2']]`
    * 행/열 (레이블): `.loc['index_label', 'col_label']`
    * 행/열 (위치): `.iloc[row_index, col_index]`
    * 단일 값 (레이블): `.at['index_label', 'col_label']`
    * 단일 값 (위치): `.iat[row_index, col_index]`
* **선택 및 필터링:** `df[df['col1'] > 1]`, `df.query('col1 > 1')`
* **정보 확인:** `.head()`, `.tail()`, `.info()`, `.describe()`, `.shape`, `.dtypes`, `.index`, `.columns`, `.values`
* **정렬:** `.sort_values(by='col')`, `.sort_index()`
* **그룹화:** `.groupby('col').sum()`, `.mean()`, `.count()`
* **결합:** `pd.merge(df1, df2, on='key')`, `pd.concat([df1, df2])`
* **변환:** `df['new_col'] = ...`, `.apply()`, `.map()` (Series), `.replace()`
* **결측치 처리:** `.isnull()`, `.fillna()`, `.dropna()`
* **파일 입출력:** `pd.read_csv('file.csv')`, `.to_csv('file.csv')`, `pd.read_excel('file.xlsx')`, `.to_excel('file.xlsx')`

<script>
  function copyToClipboard() {
    const text = document.documentElement.innerText;
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('전체 내용이 복사되었습니다.');
  }
</script>
