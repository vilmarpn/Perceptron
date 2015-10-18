from tempfile import NamedTemporaryFile
import matplotlib.pyplot as plt

VIDEO_TAG = \
"""
<video controls>
 <source src = "data:video/x-m4v;base64,{0}" type="video/mp4">
 Your browser does not support the video tag.
</video>
"""

def anim_to_html(anim):
    if not hasattr(anim, '_encoded_video'):
        with NamedTemporaryFile(suffix='.mp4') as f:
            anim.save(f.name, fps = 30, extra_args = ['-vcodec', 'libx264'])
            video = open(f.name, "rb").read()
        anim._encoded_video = video.encode("base64")
    
    return VIDEO_TAG.format(anim._encoded_video)

from IPython.display import HTML
def display_animation(anim):
    plt.close(anim._fig)
    return HTML(anim_to_html(anim))


