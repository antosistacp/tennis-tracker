from ultralytics import YOLO 

model = YOLO('yolov9e.pt')

result = model.track('input_videos/input_video7.mp4',conf=0.2, save=True)


# print(result)
# print("boxes:")
# for box in result[0].boxes:
#     print(box)