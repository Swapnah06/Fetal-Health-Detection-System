import os
import shutil
from pathlib import Path
import torch
from yolov5.models.common import DetectMultiBackend
from yolov5.utils.general import check_img_size, non_max_suppression, scale_coords
from yolov5.utils.torch_utils import select_device
from yolov5.utils.datasets import LoadImages
from yolov5.utils.plots import Annotator

# Parameters
source = './test'  # Path to test folder
detected_dir = './detected'  # Path to save detected images
weights = 'rust.pt'  # Path to your YOLOv5 weights
img_size = 640  # Image size
conf_thres = 0.25  # Confidence threshold
iou_thres = 0.45  # IoU threshold
device = '0'  # GPU id, 'cpu' for CPU usage

# Ensure detected folder exists
Path(detected_dir).mkdir(parents=True, exist_ok=True)

# Load model
device = select_device(device)
model = DetectMultiBackend(weights, device=device)
stride, names, pt = model.stride, model.names, model.pt
img_size = check_img_size(img_size, s=stride)

# Load images
dataset = LoadImages(source, img_size=img_size, stride=stride, auto=pt)

for path, img, im0s, vid_cap, s in dataset:
    img = torch.from_numpy(img).to(device)
    img = img.float() / 255.0  # Normalize
    img = img[None]  # Add batch dimension

    # Inference
    pred = model(img)
    pred = non_max_suppression(pred, conf_thres, iou_thres)

    for det in pred:  # Per image
        if len(det):  # Only process images with detections
            # Save detected image
            detected_save_path = Path(detected_dir) / Path(path).name
            annotator = Annotator(im0s, line_width=3, example=str(names))
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0s.shape).round()
            for *xyxy, conf, cls in reversed(det):
                label = f'{names[int(cls)]} {conf:.2f}'
                annotator.box_label(xyxy, label)
            im0s = annotator.result()
            cv2.imwrite(str(detected_save_path), im0s)
