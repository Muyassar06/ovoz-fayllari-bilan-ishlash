# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ykGSFf5QLPpuAT_tti3Q78UP-wDBmDfz
"""



!pip install gtts

from gtts import gTTS
import os

# Matnni belgilash
text = "Hi everyone. I'm teacher"

# Ovoz yaratish (gTTS - Google Text-to-Speech)
language = 'en'  # Changed to English ('en')
tts = gTTS(text=text, lang=language, slow=False)

# Ovoz faylini saqlash
audio_file = "output.mp3"
tts.save(audio_file)

# Ovoz faylini tinglash (Google Colab-da)
from IPython.display import Audio
Audio(audio_file)