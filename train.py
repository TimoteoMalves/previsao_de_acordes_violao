import os
from ultralytics import YOLO

dataset_yaml = 'C:\Users\timot\OneDrive\Área de Trabalho\Aulas 2025\inteligencia artificial\g2\mydatag2\data_custom.yaml'


model = YOLO('yolov11m.pt')

results = model.train(
   data=dataset_yaml,
   epochs=100, 
   imgsz=640,
   batch=1,  
)