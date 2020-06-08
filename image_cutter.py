import numpy as np
import cv2, os

dataset = "F:\\dataset"
output_folder = "F:\\dataset_cut"

folders = [folder for folder in os.listdir(dataset) if os.path.isdir(folder)]

i = 1
for folder in folders:
    folder_path = os.path.join(dataset, folder)

    for file in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, file), 1)[50:200, 50:200]

        output_path = os.path.join(dataset_path_normal, str(i) + ".jpg")

        cv2.imwrite(output_path, img)
        i += 1 
