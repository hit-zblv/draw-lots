import utils.theme as theme
import utils.config as config
import utils.roster as roster
import utils.define as define
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QLabel, QMessageBox, QFileDialog

# from PyQt6 import uic
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         uic.loadUi('./ui/ui_main.ui', self)

from ui.ui_main import Ui_MainWindow
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        print('正在初始化软件界面')
        # 设置软件标题
        self.setWindowTitle("姓名抽取软件 V1.0")
        # 设置软件图标
        self.setWindowIcon(QIcon(define.IMAGE_SOFTWARE_ICON))
        self.label_Logo.setPixmap(QPixmap(define.IMAGE_SCHOOL_LOGO))
        # 设置初始化软件主题
        theme.set_StaticTheme(self)
        print('初始化成功')

        print('正在绑定控件操作事件')
        self.pushButton_LeaveNameList.clicked.connect(self.pushButton_LeaveNameList_Clicked)
        self.pushButton_CompleteNameList.clicked.connect(self.pushButton_CompleteNameList_Clicked)
        self.pushButton_WaitNameList.clicked.connect(self.pushButton_WaitNameList_Clicked)
        self.pushButton_Start.clicked.connect(self.pushButton_Start_Clicked)
        self.pushButton_Reset.clicked.connect(self.pushButton_Reset_Clicked)
        print('绑定成功')

        print('正在载入静态配置信息')
        roster.ROSTER_DICT = roster.load_excel_info('./resources/人员名单.xlsx')
        roster.ROSTER_DICT_INIT = roster.ROSTER_DICT
        config.load_config(self, roster.ROSTER_DICT)
        print('载入成功')

        # 显示欢迎信息
        for key, value in define.WELCOME_MESSAGE.items():
            print(value)

    def pushButton_LeaveNameList_Clicked(self) -> None:
        """
        弹出提示框，显示当前请假人员名单
        :return: None
        """
        leave_name_list = roster.get_leave_roster(roster.ROSTER_DICT)
        QMessageBox.information(self, "请假人员名单", '\n'.join(leave_name_list))

    def pushButton_CompleteNameList_Clicked(self) -> None:
        """
        弹出提示框，显示当前已完成人员名单
        :return: None
        """
        complete_name_list = roster.get_complete_roster(roster.ROSTER_DICT)
        QMessageBox.information(self, "已抽完人员名单", '\n'.join(complete_name_list))

    def pushButton_WaitNameList_Clicked(self) -> None:
        """
        弹出提示框，显示当前等待人员名单
        :return: None
        """
        wait_name_list = roster.get_wait_roster(roster.ROSTER_DICT)
        QMessageBox.information(self, "待抽人员名单", '\n'.join(wait_name_list))

    def pushButton_Start_Clicked(self) -> None:
        """
        开始抽取等待人员名单
        :return: None
        """
        self.thread_RefreshDisplayResult = roster.Thread_RefreshDisplayResult_Once(self, roster.ROSTER_DICT)
        self.thread_RefreshDisplayResult.complete_name.connect(self.roster_refresh)
        self.thread_RefreshDisplayResult.start()

    def pushButton_Reset_Clicked(self) -> None:
        """
        将当前已完成人员名单移回等待人员名单
        :return: None
        """
        QMessageBox.warning(self, "", "功能暂未开放")

    def roster_refresh(self, complete_name: str) -> None:
        """
        刷新人员名单显示
        :param complete_name: 已完成人员姓名
        :return: None
        """
        roster.update_roster(roster.ROSTER_DICT, complete_name)
        config.load_config(self, roster.ROSTER_DICT)
