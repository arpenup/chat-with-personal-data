import webbrowser
import os
from flask import Flask

browser_opened = False  # 全局标志，记录浏览器是否已打开

# 实现项目启动自动打开 Chrome 浏览器
def open_browser(app: Flask):
    global browser_opened
    if browser_opened:
        return

    os_platform = os.name
    browser_path = None

    if os_platform == 'nt':  # Windows
        chrome_paths = [
            "C:/Program Files/Google/Chrome/Application/chrome.exe",
            "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        ]
        for path in chrome_paths:
            if os.path.exists(path):
                browser_path = path
                break
    elif os_platform == 'posix':  # Linux / macOS
        chrome_names = ["google-chrome", "chromium"]
        for name in chrome_names:
            try:
                import subprocess
                process = subprocess.Popen(["which", name], stdout=subprocess.PIPE)
                output, error = process.communicate()
                if output:
                    browser_path = output.decode('utf-8').strip()
                    break
            except FileNotFoundError:
                pass

    if browser_path:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
        webbrowser.get('chrome').open_new("%s:%d" % (app.config['HOST'], app.config['PORT']))
    else:
        webbrowser.open_new("%s:%d" % (app.config['HOST'], app.config['PORT']))

    browser_opened = True
