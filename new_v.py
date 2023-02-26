import picamera 
import time
import os

def record_file(current_time, recording_time):
	camera.start_recording(f'{current_time}.h264')
	camera.wait_recording(recording_time)
	camera.stop_recording

def search_path(current_path):
	if not os.path.exists(current_path):
		os.makedirs(f'{}')
	
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
recording_time = 10
current_path = 
current_time = time.strftime('%d.%m.%Y-%H:%M:%S', time.localtime())

record_file(current_time, recording_time)

