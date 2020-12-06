# VideoCoding_S3
## Practice 3 of Video Coding: Python and video

### Parts

**Exercise 1:** Convert existing BBB resolution videos into VP8, VP9, h265 & AV1.

To convert into these codecs we create a function ```create_videos()``` to take previously created videos. We can specify what codecs and resolutions to use using lists and files with a new name will be generated depending on these.

**Exercise 2:** Try to create a new video as the one of the 4 videos at the same time we saw in class, and please analyze by yourself and comment how these codecs work at each bitrate.

To do a 4-videos mashup we use:
```ffmpeg -i BBB_480vp8.mkv -i BBB_480vp9.mkv -i BBB_480h265.mkv -i BBB_480av1.mkv \
-filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" ex2_480.mkv
```
We test the codecs using 480p resolution videos. The order, from left to right and from top to bottom is VP8, VP9, h265, AV1.

We can observe that VP8 is the worst one in terms of compression and framerate preservation. VP9 and h265 are similar and perform better than VP8 in both aspects. AV1 seems to keep a high fidelity image and a smooth framerate, but took the longest to convert in the previous exercise.

**Exercise 3** Try to achieve with FFMpeg or FFServer to create a live streaming of the BBB Video. You should broadcast it into an IP address (locally of course) and open this IP or URL inside VLC Media Player.

To generate the streaming we use:
```ffmpeg -re -i BBB.mp4 -v 0 -vcodec mpeg4 -f mpegts udp://127.0.0.1:23000```
And to receive it we use the online streaming feature from VLC and plug:
```dp://@:23000```

**Exercise 4:** Try to generate a python script that enables/activates the online streaming.

We simply put the commands from the last exercise into a function, so writing the filename automatically starts the streaming and doing a keyboardinterrupt (ctrl-c) shuts it down.

### Code

This code uses the ffmpeg package.
