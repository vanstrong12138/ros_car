# import pyttsx3

# # 初始化
# engine = pyttsx3.init()

# # # 调整语速
# # rate = engine.getProperty('rate')
# # engine.setProperty('rate', rate-50)

# # # 调整音量
# # volume = engine.getProperty('volume')
# # engine.setProperty('volume', volume+25)

# # # 调整语音类型
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice', voices[1].id)

# # 设置要播报的文本
# engine.say("我是傻逼")

# # 运行
# engine.runAndWait()

import pyttsx3

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
    
    def adjust(self, rate=None, volume=None, voices=None):
        self.engine.setProperty('rate', rate-50)
        self.engine.setProperty('volume', volume+25)
        self.engine.setProperty('voice', voices[1].id)
    
    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        


if __name__ == '__main__':
    speaker = Speaker()
    speaker.say("Hello, I am a speaker")


