import itertools
import subprocess
import time
import datetime
import sys

times = 0  # 重置尝试次数

user_agreement_Chinese = """
用户协议 v1.0.0
1. 用户应当详细阅读本须知，确认同意后方可使用本程序 
2. 本程序所有代码完全开源至github：https://github.com/CH3Hg/bilibili-teenager_mode-code_breaker，但需遵守其相关开源协议
3. 本程序需要获取手机的ADB权限，需要打开开发者模式后启用，我们不会用此权限收集您的任何数据或破坏设备
4. 使用本程序即代表您知晓并确认使用此程序带来的一切法律后果，与本程序作者和代码托管平台（github）无关
5. 请在程序运行期间保持手机屏幕常亮，并不要切换至其它页面，以免造成意外
6. 本程序需要其他第三方运行库，运行库缺失会导致程序运行失败
7. 关于本程序的详细使用说明，请参考github：https://github.com/CH3Hg/bilibili-teenager_mode-code_breaker/blob/main/README.md
8. 作者保留该用户协议法律范围内的最终解释权
"""

user_agreement_English = """
User Agreement v1.0.0
1. Users should read this notice carefully and agree before using this program.
2. All code of this program is fully open source on GitHub: https://github.com/CH3Hg/bilibili-teenager_mode-code_breaker, but it must comply with the relevant open source license.
3. This program requires ADB permissions on the phone, which need to be enabled after opening developer mode. We will not use this permission to collect any data or damage the device.
4. By using this program, you acknowledge and confirm that all legal consequences arising from the use of this program have nothing to do with the author of this program and the code hosting platform (GitHub).
5. Please keep the phone screen on during the program's operation, and do not switch to other pages to avoid accidents.
6. This program requires other third-party libraries. Missing libraries will cause the program to fail.
7. For detailed instructions on using this program, please refer to GitHub: https://github.com/CH3Hg/bilibili-teenager_mode-code_breaker/blob/main/README.md
8. The author reserves the right of final interpretation of this user agreement within the scope of the law.
"""

print('==========BiliTeenModeCracker v1.0.0==========')
print('by CH3Hg')
print('https://github.com/CH3Hg/')
print('Copyright (C) <2024>  <Ruan Yichen>')

language = input('Please select the language / 请选择语言 (1-English, 2-中文): ')

if language == '1':
    print(user_agreement_English)
    is_agree = input('Do you confirm that you have read and agree to the above terms? (Y/N): ')
    if is_agree == 'Y':
        def adb_input_text(text):
            try:
                subprocess.run(['adb', 'shell', 'input', 'text', text], check=True)
            except subprocess.CalledProcessError:
                print(f"ERROR: Unable to input text '{text}', please check if ADB is working properly.")

        def wait_until_next_day():
            while True:
                now = datetime.datetime.now()
                next_day = datetime.datetime.combine(now + datetime.timedelta(days=1), datetime.time.min)
                seconds_until_next_day = (next_day - now).total_seconds()

                hours, remainder = divmod(seconds_until_next_day, 3600)
                minutes, seconds = divmod(remainder, 60)
                sys.stdout.write(f"\rReached attempt limit, time remaining to reset: {int(hours):02}:{int(minutes):02}:{int(seconds):02} ")
                sys.stdout.flush()
                time.sleep(1)

                if seconds_until_next_day <= 0:
                    break

        print('INFO: Program initialization complete')

        combinations = itertools.product('0123456789', repeat=4)
        for combination in combinations:
            if times >= 4:
                wait_until_next_day()
                times = 0  # 重置尝试次数

            password = ''.join(combination)
            print('try:', password)
            adb_input_text(password)
            time.sleep(0.1)  # 根据需要调整输入间隔
            times += 1  # 记录尝试次数

    else:
        print('Sorry, as you did not agree to the user agreement, we cannot provide you with service.')
        exit()
elif language == '2':
    print(user_agreement_Chinese)
    is_agree = input('是否确认详细阅读以上条款并同意？（Y/N）')
    if is_agree == 'Y':
        def adb_input_text(text):
            try:
                subprocess.run(['adb', 'shell', 'input', 'text', text], check=True)
            except subprocess.CalledProcessError:
                print(f"错误：无法输入文本 '{text}'，请检查 ADB 是否正常工作。")

        def wait_until_next_day():
            while True:
                now = datetime.datetime.now()
                next_day = datetime.datetime.combine(now + datetime.timedelta(days=1), datetime.time.min)
                seconds_until_next_day = (next_day - now).total_seconds()

                hours, remainder = divmod(seconds_until_next_day, 3600)
                minutes, seconds = divmod(remainder, 60)
                sys.stdout.write(f"\r已达到尝试限额，恢复剩余时间：{int(hours):02}:{int(minutes):02}:{int(seconds):02} ")
                sys.stdout.flush()
                time.sleep(1)

                if seconds_until_next_day <= 0:
                    break

        print('信息：程序初始化完成')

        combinations = itertools.product('0123456789', repeat=4)
        for combination in combinations:
            if times >= 4:
                wait_until_next_day()
                times = 0  # 重置尝试次数

            password = ''.join(combination)
            print('尝试：', password)
            adb_input_text(password)
            time.sleep(0.1)  # 请根据需要调整输入间隔
            times += 1  # 记录尝试次数

    else:
        print('对不起，由于您不同意用户须知，我们无法为您提供服务！')
        exit()
else:
    print("Invalid selection. Please restart the program and select a valid language.")
