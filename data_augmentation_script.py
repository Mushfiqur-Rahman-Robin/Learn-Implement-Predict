# pip install tensorflow and then run this code

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
import os

def augment_images_keras_recursive(input_directory, output_folder, num_augmented_images):
    datagen = ImageDataGenerator(
        rotation_range=5,
        width_shift_range=0.05,
        height_shift_range=0.1,
        # shear_range=0.2,
        # zoom_range=0.2,
        # horizontal_flip=True,
        fill_mode='nearest'
    )

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_directory):
        if "accepted" in dirs:
            input_folder = os.path.join(root, "accepted")

            for _, _, files in os.walk(input_folder):
                for file in files:
                    img_path = os.path.join(input_folder, file)
                    img = image.load_img(img_path)
                    x = image.img_to_array(img)
                    x = x.reshape((1,) + x.shape)

                    # Generate augmented images
                    i = 0
                    for batch in datagen.flow(x, 
                                              batch_size=1, 
                                              save_to_dir=output_folder, 
                                              save_prefix='aug', 
                                              save_format='jpg'):
                        i += 1
                        if i >= num_augmented_images:
                            break


input_directory = "../mch-dataset-intermediate/3231"
output_folder = "../augmented"
num_augmented_images = 100 
augment_images_keras_recursive(input_directory, output_folder, num_augmented_images)
