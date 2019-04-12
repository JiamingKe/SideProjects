import tensorflow as tf
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.layers import Dense, Flatten, Conv1D, BatchNormalization, Dropout
from tensorflow.keras import Model

EPOCHS = 20
BATCH_SIZE = 1024
TRAIN_SAMPLE = 120
TEST_SAMPLE = 20

print("Start loading data from file ...")
all_data =pd.read_table("index.txt", sep=" ",
                        names=['normalizeddiff_veg-index', 'simple_rat_index', 'diff_veg_index',
                               'soil_reg_veg_index', 'sr', 'nri', 'tpvi', 'norm_red', 'norm_nir', 'norm_green',
                               'cvi', 'green_red_ndvi', 'label'])

LE = LabelEncoder()
labels = LE.fit_transform(all_data['label'])
raw_data = all_data.drop(labels=['normalizeddiff_veg-index', 'label'], axis=1).values

X_train, X_test, y_train, y_test = train_test_split(raw_data, labels, test_size=0.2)

print("Converting data to tensors ...")
X_train = X_train.reshape((len(X_train), 11, 1))
# trainset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
trainset = tf.data.Dataset.from_tensor_slices((X_train[0:TRAIN_SAMPLE], y_train[0:TRAIN_SAMPLE]))
trainset = trainset.shuffle(10000).batch(BATCH_SIZE)
print(trainset)

X_test = X_test.reshape((len(X_test), 11, 1))
# testset = tf.data.Dataset.from_tensor_slices((X_test, y_test))
testset = tf.data.Dataset.from_tensor_slices((X_test[0:TEST_SAMPLE], y_test[0:TEST_SAMPLE]))
testset = testset.shuffle(10000).batch(BATCH_SIZE)
print(testset)


class MyModel(Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = Conv1D(32, 3, activation='relu')
        self.bn1 = BatchNormalization()
        self.conv2 = Conv1D(32, 3, activation='relu')
        self.bn2 = BatchNormalization()
        self.flatten = Flatten()
        self.drop1 = Dropout(0.5)
        self.d1 = Dense(64, activation='relu')
        self.d2 = Dense(64, activation='relu')
        self.drop2 = Dropout(0.2)
        self.end = Dense(2, activation='softmax')

    def call(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.flatten(x)
        x = self.drop1(x)
        x = self.d1(x)
        x = self.d2(x)
        x = self.drop2(x)
        return self.end(x)


model = MyModel()

loss_object = tf.keras.losses.SparseCategoricalCrossentropy()

optimizer = tf.keras.optimizers.Adam()

train_loss = tf.keras.metrics.Mean(name='train_loss')
train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='train_accuracy')

test_loss = tf.keras.metrics.Mean(name='test_loss')
test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name='test_accuracy')


@tf.function
def train_step(feature, label):
    with tf.GradientTape() as tape:
        predictions = model(feature)
        loss = loss_object(label, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    train_loss(loss)
    train_accuracy(label, predictions)


@tf.function
def test_step(feature, label):
    predictions = model(feature)
    t_loss = loss_object(label, predictions)

    test_loss(t_loss)
    test_accuracy(label, predictions)


print("Start training ...")
best_acc = 0
patient = 10
j = 0
while j < patient:
    for epoch in range(EPOCHS):
        for feature, label in trainset:
            train_step(feature, label)

        for test_feature, test_label in testset:
            test_step(test_feature, test_label)

        template = 'Epoch {}, Loss: {}, Accuracy: {}, Test Loss: {}, Test Accuracy: {}'
        print(template.format(epoch + 1,
                            train_loss.result(),
                            train_accuracy.result() * 100,
                            test_loss.result(),
                            test_accuracy.result() * 100))

    if best_acc < test_accuracy.result():
        model.save_weights('VegIndexModel')

        print("Accept the new model, best accuracy is updated ")
        best_acc = test_accuracy.result()
        j = 0
    else:
        print("Reject the new model, best accuracy remained unchanged ")
        j += 1

    print(test_accuracy.result())
    print()
