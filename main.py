import cv2
import os
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

RTSP_URL = "rtsp://" + f"{os.getenv('CAM_USERNAME')}" + ":" + f"{os.getenv('CAM_PASSWORD')}" + "@" + f"{os.getenv('CAM_IP')}" + ":" + f"{os.getenv('CAM_PORT')}" + "/" + f"{os.getenv('CAM_ENDPOINT')}"
DEVICE = os.getenv('CAM_DEVICENAME')
SAVE_PATH = "D:/RTSP_Recordings/" + DEVICE
SEGMENT_DURATION = 10 * 60 # 10 minutes - ~700Mb @1080p
MAX_SEGMENTS = 500 # 500 videos - 500 * 10 mins (approx. 350Gb of footage)

# save dir
os.makedirs(SAVE_PATH, exist_ok=True)

recorded_files = sorted(os.listdir(SAVE_PATH))  # sort by name - oldest first
while len(recorded_files) > MAX_SEGMENTS:
    os.remove(os.path.join(SAVE_PATH, recorded_files.pop(0)))  # delete oldest files if over MAX_SEGMENTS

cap = cv2.VideoCapture(RTSP_URL)
if not cap.isOpened():
    print("Error: Could not open RTSP stream")
    exit()

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS) or 30)  # default to 30FPS if unknown

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    video_filename = os.path.join(SAVE_PATH, f"{DEVICE}_{timestamp}.mp4")

    # video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec
    out = cv2.VideoWriter(video_filename, fourcc, fps, (frame_width, frame_height))

    start_time = time.time()

    while (time.time() - start_time) < SEGMENT_DURATION:
        ret, frame = cap.read()
        if not ret:
            print("Failed to retrieve frame")
            break

        # write frame to file
        out.write(frame)

        # display live footage (optional)
        cv2.imshow(f"{DEVICE}_RTSP_STREAM", frame)

        # exit on 'Q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            exit()

    # release current video file
    out.release()