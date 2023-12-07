from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import io

def preprocess_image(image_file):
    # Load the image file
    img = image.load_img(io.BytesIO(image_file), target_size=(224, 224))

    # Convert the image to a numpy array
    img_array = img_to_array(img)

    # Expand the dimensions to create a batch size of 1
    # img_array = np.expand_dims(img_array, axis=0)

    # Rescale pixel values to between 0 and 1
    img_array /= 255.0

    return img_array
