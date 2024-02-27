from ultralytics import YOLO

# Load a model
model = YOLO("yolov8m.pt")  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
results = model.train(data="custom.yaml", epochs=3, imgsz=960, device=0)
