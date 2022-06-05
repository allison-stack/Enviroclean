import numpy as np
from tensorflow.keras import models
from keras.preprocessing import image

model = models.load_model("classified model")

img = image.load_img('bottle.jpg', target_size=(150,150))

x = image.img_to_array(img)
x /= 255
x = np.expand_dims(x, axis=0)
images = np.vstack([x])

classes = model.predict(images, batch_size=10)

print(classes[0])

if classes[0] > 0.5:
    print("Recycle")
else:
    print ("Organic")
