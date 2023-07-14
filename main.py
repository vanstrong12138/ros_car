import _thread
from audio.audio_detection import listener
import threading
import time



if __name__ =='__main__':

    # 创建一个线程对象，指定目标函数为my_function
    my_thread = threading.Thread(target=listener)

    # 开启线程
    my_thread.start()

    # 等待线程结束
    my_thread.join()