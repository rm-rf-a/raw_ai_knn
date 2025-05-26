import random
import numpy as np
import csv
import os
from constants import NUM_POINTS,DOT_RANGE,SEED,X_RANGE,Y_RANGE,NUM_CLASSES

def make_random_points(x_range=X_RANGE, y_range=Y_RANGE, n=NUM_POINTS, dot_range=DOT_RANGE, seed=SEED, num_classes=NUM_CLASSES):
    np.random.seed(seed)
    points = []
    for i in range(num_classes):
        x_basepoint = random.randint(-x_range, x_range) 
        y_basepoint = random.randint(-y_range, y_range)
        for _ in range(n// num_classes):
            x = random.randint(x_basepoint-dot_range, x_basepoint+dot_range) 
            y = random.randint(y_basepoint-dot_range, y_basepoint+dot_range)
            points.append((x, y, i))  # i는 클래스 번호
    return points



def save_points(filepath,points):

    dir_path = os.path.dirname(filepath)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)


    with open(filepath, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y", "class"])
        writer.writerows(points)

if __name__ == "__main__":
    pts = make_random_points()
    filepath = './data/points.csv'
    save_points(filepath,pts)