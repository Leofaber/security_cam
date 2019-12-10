# Raspberry surveillance cam

## Using rapistill

## Using raspivid
MP4 Video Format

The Pi captures video as a raw H264 video stream. Many media players will refuse to play it, or play it at an incorrect speed, unless it is "wrapped" in a suitable container format like MP4. The easiest way to obtain an MP4 file from the raspivid command is using MP4Box.

Install MP4Box with this command:

sudo apt install -y gpac

Capture 30 seconds of raw video at 640x480 and 150kB/s bit rate into a pivideo.h264 file:
raspivid -t 10000 -w 640 -h 480 -fps 25 -o pivideo.h264

Wrap the raw video with an MP4 container:

MP4Box -add pivideo.h264 pivideo.mp4

Remove the source raw file, leaving the remaining pivideo.mp4 file to play
rm pivideo.h264

## Using motion
sudo apt-get install motion -y

v4l2-ctl -V

sudo nano /etc/motion/motion.conf


sudo nano /etc/default/motion

* start_motion_daemon=yes

mkdir /home/pi/Projects/security_cam/videos
sudo chgrp motion /home/pi/Projects/security_cam/videos
chmod g+rwx /home/pi/Projects/security_cam/videos


sudo service motion start

Go to http:192.168.1.77:8081
