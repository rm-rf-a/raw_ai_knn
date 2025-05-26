import matplotlib.pyplot as plt
import csv

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

def plot_points(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    classes = [p[2] for p in points]
    plt.scatter(xs, ys, c=classes, cmap='tab10', s=30)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Points Visualization")
    plt.show()

if __name__ == "__main__":
    points = read_points("./data/points.csv")
    plot_points(points)