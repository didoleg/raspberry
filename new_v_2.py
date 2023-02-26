import picamera 
import time
import os

"""Функция проверки наличия пути для сохранения файлов, если он отсутствует, то путь создается"""
def check_file_path():
    year = time.strftime('%Y', time.localtime())
    month = time.strftime('%m', time.localtime())
    day = time.strftime('%d', time.localtime())
    if not os.path.exists(f'{year}/{month}/{day}'):
        os.makedirs(f'{year}/{month}/{day}')
    file_path = os.path.join(os.getcwd(), f'{year}/{month}/{day}')
    return file_path

"""Функция осуществляющая запись видео, она принимает в качестве аргумента длину видео в секундах"""
def record_file(recording_time):
	camera.resolution = (1920, 1080)
	current_time = time.strftime('%d.%m.%Y-%H:%M:%S', time.localtime())
	file_path = check_file_path()
	camera.start_recording(f'{file_path}/{current_time}.h264')
	camera.wait_recording(recording_time)
	camera.stop_recording

raspivid -o - -t 0 -hf -w 800 -h 400 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264
camera = picamera.PiCamera()
recording_time = 10
record_file(recording_time)

