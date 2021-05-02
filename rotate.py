import asyncio, glob, os, ffmpeg
#-vf "vflip,hflip" -r 60 -qscale 0 -acodec copy

if not os.path.isdir('rotated'):
    os.mkdir('rotated')
if not os.path.isdir('input'):
    os.mkdir('input')
os.chdir("./input")
for file in glob.glob("*.MP4"):
    stream = ffmpeg.input(str(file))
    audio1 = stream.audio
    stream = ffmpeg.vflip(stream)
    stream = ffmpeg.hflip(stream)
    stream = ffmpeg.filter(stream, 'fps', fps=60, round='up')
    stream = ffmpeg.output(stream, audio1, str('../rotated/' + file), acodec="copy")
    ffmpeg.run(stream)