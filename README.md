# RTSP Stream Recorder (or a homemade NVR for Wi-Fi cameras)

This Python script records an RTSP stream from a Wi-Fi camera, segments the footage into 10-minute files, and stores them in a specified directory. The script automatically deletes the oldest footage when the limit is exceeded, ensuring that the most recent recordings are always retained.

## Features
- **RTSP Stream Capture**: Connects to an RTSP stream using credentials from environment variables.
- **Segmented Recording**: Saves videos in 10-minute segments, making the storage manageable.
- **Automatic Cleanup**: Deletes the oldest video files if the number of segments exceeds a predefined limit.
- **Live Preview**: Displays a real-time preview of the stream (optional).
- **Cross-Platform**: Designed to work on both Windows and Linux systems. Can run on a Raspberry Pi as well.

## Requirements

- Python 3.x
- [OpenCV](https://opencv.org/) library for video capture and processing
- [python-dotenv](https://pypi.org/project/python-dotenv/) for loading environment variables from a `.env` file

Install the required libraries using pip:

```bash
pip install opencv-python python-dotenv
```

## Setup
1. Set Up Environment Variables
You need to create a `.env` file to store your camera credentials. The script will automatically load these values.

Example `.env`:<br>
CAM_USERNAME=your_username<br>
CAM_PASSWORD=your_camera_password<br>
CAM_IP=camera_local_ip_address (e.g. 192.168.1.71) - *good idea to configure your camera to be static<br>
CAM_PORT=your_camera_port (e.g. 554)<br>
CAM_ENDPOINT=your_camera_stream_endpoint (e.g. onvif1)<br>
CAM_DEVICENAME=your_camera_device_name (just for save path and file names)

2. Modify Save Path (Optional)
The default save path for recorded video files is `D:/RTSP_Recordings/`, which can be changed based on your preference or operating system.

3. Run the Script
After setting up the `.env` file and ensuring the required libraries are installed, run the script:
```bash
py -u ./main.py
```

The script will start recording the RTSP stream in 10-minute segments, saving them in the specified directory.

## Tips
- Storage Management: The script will keep only the latest `MAX_SEGMENTS` videos (I set it to 500). If the number of recorded files exceeds this value, the oldest files will be deleted to make space for new ones.
- Running on Raspberry Pi: The script is lightweight and can be easily run on a Raspberry Pi, which makes it suitable for home security systems or similar projects. Ensure you have a reliable power supply and enough storage (e.g., external SSD or HDD) for long-term use.
- Customizing Segment Duration: You can change the segment duration (I set it to 10 minutes) by adjusting the `SEGMENT_DURATION` variable.
- Codec: The script uses the `mp4v` codec for video recording. If you're experiencing issues with playback, you can change the codec to another one like `avc1`, `x264`, `hevc`, etc.

## Additional notes
- To stop the recording manually, press the 'Q' key while the live preview window is open.
