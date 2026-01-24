import zipfile
from pathlib import Path

ZIP_PATH = r"dataset/cpted.v1.yolov8.zip"
DATASET_PATH = Path("/dataset/yolov8_dataset")

with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
    zip_ref.extractall(DATASET_PATH)

print("Dataset estratto in:", DATASET_PATH)

import cv2
import numpy as np
import pandas as pd
import yaml
from pathlib import Path
from ultralytics import YOLO
import shutil
import os

DATASET_PATH = Path("/dataset/yolov8_dataset")
SPLITS = ["train", "valid"]
OUTPUT_CSV = r"output/dataset_summary.csv"

# Legge data.yaml
with open(DATASET_PATH / "data.yaml", "r") as f:
    data_yaml = yaml.safe_load(f)

class_names = data_yaml["names"]
print("Classi:", class_names)

data_yaml_path = DATASET_PATH / "data.yaml"

model = YOLO("yolov8s-seg.pt")  # modello pre-addestrato

model.train(
    data=str(data_yaml_path),
    epochs=100,
    patience=50,
    save_period=20,
    imgsz=640,
    batch=8,          # su Colab puoi aumentare
    optimizer="auto",
    plots=True,
    device=0,         # GPU
    workers=2
)

best_src = Path("runs/segment/train/weights/best.pt")
best_dst = Path("/content/drive/MyDrive/models/best_yolo8.pt")

best_dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copy(best_src, best_dst)

print("Modello salvato in:", best_dst)
