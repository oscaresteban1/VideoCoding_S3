from os import path, system

# ex1: simple video codec conversion of BBB video
def create_videos(codecs, resolutions):
    for cod in codecs:
        for i in resolutions:
            output = "BBB_" + i + cod +".mkv"
            if not path.exists(output):
                system("ffmpeg -i BBB_" + i + ".mp4 " + "-c:v " + cod + " " + output)

# ex2
#ffmpeg -i BBB_480vp8.mkv -i BBB_480vp9.mkv -i BBB_480hevc.mkv -i BBB_480av1.mkv -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" ex2_480.mkv
#ffmpeg -i BBB_120vp8.mkv -i BBB_120vp9.mkv -i BBB_120hevc.mkv -i BBB_120av1.mkv -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" ex2_120.mkv

# ex4
def stream():
    print("write the video filename to stream!")
    filename = input()
    while not path.exists(filename):
        print("file does not exist, try another one:")
        filename = input()

    print("ctrl+c to stop the stream!")
    system("ffmpeg -re -i " + filename + " -v 0 -vcodec mpeg4 -f mpegts udp://127.0.0.1:23000")


codecs = ["vp8", "vp9", "hevc", "av1"]
resolutions = ["120", "480"]
#create_videos(codecs, resolutions)
#stream()
