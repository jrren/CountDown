import time  
import os  
  
def focus_clock(minutes):  
    while minutes > 0:  
        print(time.strftime('%H:%M:%S'), end='')  
        time.sleep(1)  
        minutes -= 1  
    print("Time's up!")  
    os.system('play beep.wav')  # 如果想要播放提示音，需要有一个名为beep.wav的文件  
  
if __name__ == "__main__":  
    focus_clock(60)  # 设定60分钟的专注时间
