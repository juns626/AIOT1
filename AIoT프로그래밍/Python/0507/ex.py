import numpy as np
import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# 1. 데이터 불러오기
digits = load_digits()
X = digits.data  # (1797, 64)
y = digits.target  # (1797,)

# 2. 정규화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. 학습/테스트 분리
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# 4. SVM 모델 정의 및 학습
svm_model = SVC(kernel='rbf', C=10, gamma=0.01, probability=True)
svm_model.fit(X_train, y_train)

# 5. TensorFlow로 입력 하나 예측
def tf_predict(input_array):
    input_tensor = tf.convert_to_tensor(input_array.reshape(1, -1), dtype=tf.float32)
    numpy_input = input_tensor.numpy()
    prediction = svm_model.predict(numpy_input)
    return prediction[0]

# 예시: 테스트 셋 첫 번째 숫자 예측
index = 0
predicted = tf_predict(X_test[index])
print(f"예측 결과: {predicted}, 실제 값: {y_test[index]}")
