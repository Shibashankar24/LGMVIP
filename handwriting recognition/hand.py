from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt

(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = mnist.load_data()
train = mnist_train_images.reshape(60000, 784)
test = mnist_test_images.reshape(10000, 784)
train = train.astype('float32')
test = test.astype('float32')
train /= 255
test /= 255
train_labels = keras.utils.to_categorical(mnist_train_labels, 10)
test_labels = keras.utils.to_categorical(mnist_test_labels, 10)

def display(num):
    print(train_labels[num])
    label = train_labels[num].argmax(axis=0)
    image = train[num].reshape([28, 28])
    plt.title('sample: %d, Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()

display(1000)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))
model.summary()
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])
history = model.fit(train, train_labels, batch_size=100, epochs=10, verbose=2, validation_data=(test, test_labels))

score = model.evaluate(test, test_labels, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

for x in range(1000):
    test_image = test[x, :].reshape(1, 784)
    predicted_cat = model.predict(test_image).argmax()
    label = test_labels[x].argmax()
    if predicted_cat != label:
        plt.title('prediction: %d, Label: %d' % (predicted_cat, label))
        plt.imshow(test_image.reshape([28, 28]), cmap=plt.get_cmap('gray_r'))
        plt.show()