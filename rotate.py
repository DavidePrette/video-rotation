import asyncio, glob, os, ffmpeg

#-vf "vflip,hflip" -r 60 -qscale 0 -acodec copy

os.chdir(".")
for file in glob.glob("*.MP4"):
    stream = ffmpeg.input(str(file))
    stream = ffmpeg.vflip(stream)
    stream = ffmpeg.hflip(stream)
    stream = ffmpeg.filter(stream, 'fps', fps=60, round='up')
    stream = ffmpeg.output(stream, 'output.mp4', acodec="copy")
    ffmpeg.run(stream)