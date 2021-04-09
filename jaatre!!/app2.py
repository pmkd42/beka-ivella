from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='black')

f = open('enresult.txt', 'r', encoding='utf-8')
Lines = f.readlines()

subs = []
count = 0
for line in Lines:
    subs.append(((count, count + 10), line))
    count+=10

subtitles = SubtitlesClip(subs, generator)

video = VideoFileClip("demo.mp4")
result = CompositeVideoClip([video, subtitles.set_pos(('center','bottom'))])

result.write_videofile("output.mp4")
