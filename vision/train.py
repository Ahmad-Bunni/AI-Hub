from ultralytics import YOLO

# Load a model
model = YOLO("yolov9n.pt")

results = model.train(data="custom.yaml", epochs=3, imgsz=960, device=0)
