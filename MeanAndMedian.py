import csv
import numpy as np

def get_points(filepath):
    points = []
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            x = int(row["x"])
            y = int(row["y"])
            points.append((x, y))
    return points

def get_median_xy(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    median_x = np.median(x)
    median_y = np.median(y)
    return median_x, median_y

def get_mean_xy(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    return mean_x, mean_y


if __name__ == "__main__":
    filepath = "./data/points.csv"
    points = get_points(filepath)
    median_x, median_y = get_median_xy(points)
    mean_x, mean_y = get_mean_xy(points)
    print(f"중앙값 x: {median_x}, 중앙값 y: {median_y}")
    print(f"평균값 x: {mean_x}, 평균값 y: {mean_y}")