import argparse
from datetime import datetime, timedelta
import subprocess
from time import sleep
import os
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description='')
parser.add_argument('--tstart', type=str, help='Time start in format: %H:%M:%S', required=True)
parser.add_argument('--tstop', type=str, help='Time stop in format: %H:%M:%S', required=True)
args = parser.parse_args()


now = datetime.now()

now_day = now.strftime("%x")

start_date = datetime.strptime(now_day+args.tstart, '%x%H:%M:%S')

end_date = datetime.strptime(now_day+args.tstop, '%x%H:%M:%S')


print("Now ", now)
print("Start ", start_date)
print("End ", end_date)

if end_date < start_date:
    print("end date cannot be lower than start_date")
    exit(1)

if start_date < now:
    print("start_date cannot be lower than now")
    exit(1)

timedelta_to_start = start_date - now
timedelta_to_finish = end_date - start_date

print("Monitoring will start in: ",timedelta_to_start)
print("Monitoring will end in: ",timedelta_to_finish)

while(True):
    sleep(5)
    now = datetime.now()
    if now > start_date:
        break

while(True):

    now = datetime.now()

    if now > end_date:
        break


    print(end_date-now)

    outfile = "./videos/"+"pivideo_"+now.strftime("%H_%M_%S")

    command = "raspivid -t 360000 -w 640 -h 480 -fps 35 -o "+outfile+".h264"

    print("Calling",command)

    pid = subprocess.call(command, shell=True)

    print("raspivid process",pid,"terminated.")



    command = "MP4Box -add "+outfile+".h264 "+outfile+".mp4"

    print("Calling",command)

    pid = subprocess.call(command, shell=True)

    print("MP4Box process",pid,"terminated.")



    os.remove(outfile+".h264")


output_path = "./videos"
onlyfiles = [f for f in listdir(output_path) if isfile(join(output_path, f))]
onlyfiles.sort()

print(onlyfiles)
