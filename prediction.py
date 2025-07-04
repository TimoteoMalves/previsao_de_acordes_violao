import os
from ultralytics import YOLO

prediction_model = "mymodel.pt"
prediction_source = "16.jpeg"

predict_results = prediction_model.predict(
   source=prediction_source, 
   imgsz=640,       
   show=True,      
)

