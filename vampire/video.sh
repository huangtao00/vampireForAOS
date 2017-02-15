ffmpeg -loop 1 -r 50  -start_number 0 -i precession%3d.png -vframes 600 -c:v libx264 output.mp4

# -vframes :we get 1800 frames in the video
# -r 100: means we display 100 frames persecond
# -loop 1 : means loop forever
