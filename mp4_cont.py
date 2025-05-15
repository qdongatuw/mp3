from tkinter.filedialog import askopenfilenames
import moviepy
# from moviepy import editor

# 读取所有视频
clips = askopenfilenames(defaultextension='.mp4')

# 拼接视频
final_clip = moviepy.concatenate_videoclips(clips)

# 导出结果
final_clip.write_videofile("output.mp4")
