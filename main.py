import sys
from utils import MainWindow
from PyQt6.QtWidgets import QApplication

"""
1. 无终端窗口： pyinstaller -F -n 哈工大牌抓阄 -w -i ./resources/软件图标.ico main.py
2. 有终端窗口： pyinstaller -F -n 哈工大牌抓阄 -c -i ./resources/软件图标.ico main.py

pip freeze > requirements.txt
pip install -r requirements.txt
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
