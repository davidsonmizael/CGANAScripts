import cv2
import numpy as np
import os

dataset_path_edges = "F:\\dataset"
dataset = "F:\\dataset"

for file in os.listdir(dataset):
    img = cv2.imread(os.path.join(dataset_path_normal, file), 1)
    edges = cv2.Canny(img, 80, 150)

    edges = (255 - edges)

    save_path_edges = os.path.join(dataset_path_edges, file)

    cv2.imwrite(save_path_edges, edges)
