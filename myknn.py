import csv
import numpy as np
from collections import Counter
from constants import NUM_CLASSES

def read_points(filepath):
    points = []
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            x = int(row["x"])
            y = int(row["y"])
            cls = int(row["class"])
            points.append((x, y, cls))
    return points


def find_k_nearest_classes(points, x, y, k):
    # 각 점까지의 거리와 클래스 정보를 저장할 리스트 생성
    distances = []
    for point in points:
        px, py, cls = point
        # 입력 좌표 (x, y)와 점 (px, py) 사이의 거리 계산
        dx = px - x
        dy = py - y
        dist = (dx ** 2 + dy ** 2) ** 0.5  # 유클리드 거리
        distances.append((dist, cls))      # (거리, 클래스) 형태로 저장

    # 거리를 기준으로 오름차순 정렬
    distances.sort(key=lambda item: item[0])

    # 가까운 k개의 점의 클래스만 추출
    k_classes = []
    for i in range(k):
        k_classes.append(distances[i][1])

    return k_classes

if __name__ == "__main__":
    x = int(input("x 값을 입력하세요: "))
    y = int(input("y 값을 입력하세요: "))
    k = int(input("k 값을 입력하세요: "))

    points = read_points("./data/points.csv")
    k_classes = find_k_nearest_classes(points, x, y, k)
    print(f"k개 이웃의 클래스: {k_classes}")
    print(f"클래스별 개수: {Counter(k_classes)}")
    print(f"주어진점의 예측 클래스: {Counter(k_classes).most_common(1)[0][0]}")