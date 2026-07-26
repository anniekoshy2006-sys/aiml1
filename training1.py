import tensorflow as tf
from tensorflow.keras import layers
image_size = (160,160)
model = "cat_dog_classification.keras"

train_ds = tf.keras.utils.image_dataset_from_directory("dataset/train",image_size=image_size,label_mode="binary")
testing_ds = tf.keras.utils.image_dataset_from_directory("dataset/validation",image_size=image_size,label_mode="binary")

print("training dataset size:",len(train_ds))
print("testing dataset size:",len(testing_ds))
print("classes:",train_ds.class_names)

base = tf.keras.applications.MobileNetV2(input_shape= (160,160,3),include_top = False, weights = "imagenet")
base.trainable = False

model = tf.keras.Sequential([
    layers.Rescaling(1./127.5,input_shape=(160,160,3)),
    base,
    layers.GlobalAveragePooling2D(),
    layers.Dense(1,activation="sigmoid")  
])
model.compile(optimizer="adam",loss="binary_crossentropy",metrics = ["accuracy"])
model.fit(train_ds,validation_data = testing_ds, epochs = 5)
model.save("cat_dog_classification.keras")
print("model save succesfully")
