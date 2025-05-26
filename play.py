import subprocess
import os

base_dir = r"C:주소는 여기에"

file_list = [
    os.path.join(base_dir, "points_make.py"),
    os.path.join(base_dir, "MeanAndMedian.py"),
    os.path.join(base_dir, "myknn.py")
]

for file in file_list:
    print(f"실행 중: {file}")
    subprocess.run(["python", file], check=True)
print("모든 파일 실행 완료!")