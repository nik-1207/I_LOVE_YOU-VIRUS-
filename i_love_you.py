def i_love_you():
    from gtts import gTTS
    speech=gTTS("I love you",'en','slow')
    speech.save("sample.mp3")
    return
i_love_you()
