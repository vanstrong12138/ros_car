import speech_recognition as sr

def voice_ctrl(text):
    text = str(text)
    if "原神" and "启动" in text:
        print("小车启动")
    else:
        print("未启动")
    
    return 0
    

def listener():
    # 创建一个 Recognizer 对象
    r = sr.Recognizer()

    # 开始监听
    with sr.Microphone() as source:
        print("请开始说话")
        audio = r.listen(source)

    # 调用 recognize_google() 方法进行语音识别
    try:
        text = r.recognize_google(audio, language='zh-CN')
        print(text)
        voice_ctrl(str(text))
        listener()
    except:
        print("没有有效声音")
        listener()


if __name__ == '__main__':
    listener()