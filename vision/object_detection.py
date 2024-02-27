from ultralytics import YOLO

# Load a model
model = YOLO("best.pt")
model.to("cuda")

results = model.predict(source=0, show=True, conf=0.6)
