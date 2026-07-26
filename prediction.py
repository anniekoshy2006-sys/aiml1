import tensorflow as tf
model = tf.keras.models.load_model("cat_dog_classification.keras")
image_path = "SAMPLE2.jpg"
img = tf.keras.utils.load_img(image_path,target_size=(160,160))
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array,0)

predictions = model.predict(img_array)
print(predictions[0] [0])

if predictions[0] [0] >0.5:
    print("the image is classified as a dog")
    print("confidence:", predictions[0] [0]*100,"%")
else:
    print("the image is classified as a cat")
    print("confidence:",(1-predictions[0] [0])*100,"%")