from pathlib import Path
from typing import List
import imageio 
import os
from os import listdir
import numpy as np

def read_images(image_names, folder_name, limit):
    
    images = np.array([[],[]])
    for image in image_names:
        image_data = imageio.imread(f"{folder_name}/{image}")
        image_np = np.array(image_data)
        dim2, dim3, dim4 = image_np.shape
        print("dimension 2")
        print(dim2)
        print("dimension 3")
        print(dim3)
        print("dimension 4")
        print(dim4)
        print("mulitplying dimensions")
        print(dim4*dim2*dim3)
        image_np = image_np.reshape(dim2, dim3*dim4)
        images = np.append(images, [image_np])
    print("test images")    
    print(images)
    
    return images


def get_image_names(folder_name, limit):
    image_names = []
    for image in listdir(f"{folder_name}"):
        image_names.append(image)
    return image_names[0:limit]
    

def get_training_data(limit):
    folder = "jpeg/train"
  
    image_names = get_image_names(folder, limit)
   

    images = read_images(image_names, folder, len(image_names))
    print("Successful reading")

    return [image_names, images]