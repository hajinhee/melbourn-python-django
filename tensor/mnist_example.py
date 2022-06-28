import tensorflow as tf


class Solution(object):
    def __init__(self):
        self.mnist = tf.keras.datasets
        self.x_train = None
        self.x_test = None
        self.model = None

    def hook(self):
        # 1~4 전체가 learning 모델을 훈련하고 평가에서 train
        def print_menu():
            print('0. Exit')
            print('1. 데이터로드')
            print('2. 모델생성')
            print('3. 모델을 훈련하고 평가')
            print('4. 손글씨 테스트')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            if menu == '1':
                self.data_load()
            if menu == '2':
                self.create_model()
            if menu == '3':
                self.training_evaluation_model()
            if menu == '4':
                self.teat()
            elif menu == '0':
                break

    def data_load(self):
        mnist = self.mnist
        (x_train, y_train), (x_test,  y_test) = mnist.load_data()
        self.x_train, self.x_test = x_train / 255.0, x_test / 255.0

    def create_model(self):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        self.model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    def training_evaluation_model(self):
        self.model.fit(self.x_train, self.y_train, epochs=5)

    def teat(self):
        pass


if __name__ == '__main__':
    Solution().hook()