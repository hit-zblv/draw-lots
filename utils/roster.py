import time
import math
import random
import pandas as pd
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QMessageBox

ROSTER_DICT = {}
ROSTER_DICT_INIT = {}

def load_excel_info(excel_path: str) -> dict:
    """
    加载Excel配置信息
    :param excel_path: Excel文件路径
    :return: Excel配置信息字典
    """
    try:
        df = pd.read_excel(excel_path, header=0, names=['姓名', '是否请假'])
        roster_list = df.to_dict('records')
        roster_dict = {}
        for item in roster_list:
            roster_dict[item['姓名']] = {}
            roster_dict[item['姓名']]['请假状态'] = item['是否请假']
            roster_dict[item['姓名']]['抽取状态'] = '排除' if item['是否请假'] == '是' else '否'
        return roster_dict
    except FileNotFoundError:
        print(f'Excel文件 {excel_path} 不存在！')
        return {}

def get_leave_roster(total_roster: dict) -> list:
    """
    获取请假人员名单
    :param total_roster: 人员名单字典
    :return: 请假人员名单字典
    """
    leave_roster = []
    for name, info in total_roster.items():
        if info['请假状态'] == '是':
            leave_roster.append(name)
    return leave_roster

def get_wait_roster(total_roster: dict) -> list:
    """
    获取等待抽取人员名单字典
    :param total_roster: 人员名单字典
    :return: 请假人员名单字典
    """
    wait_roster = []
    for name, info in total_roster.items():
        if info['抽取状态'] == '否':
            wait_roster.append(name)
    return wait_roster

def get_complete_roster(total_roster: dict) -> list:
    """
    获取抽取完成人员名单字典
    :param total_roster: 人员名单字典
    :return: 请假人员名单字典
    """
    complete_roster = []
    for name, info in total_roster.items():
        if info['抽取状态'] == '是':
            complete_roster.append(name)
    return complete_roster

def update_roster(total_roster: dict, complete_name: str) -> dict:
    """
    抽取完成后，更新人员名单字典
    :param total_roster: 人员名单字典
    :param name: 人员姓名
    :return: 人员名单字典
    """
    if complete_name != '空':
        total_roster[complete_name]['抽取状态'] = '是'
    return total_roster

def random_name(wait_roster: list) -> str:
    """
    随机抽取人员姓名
    :param wait_roster: 等待抽取人员名单
    :return: 随机抽取人员姓名
    """
    return random.choice(wait_roster) if len(wait_roster) != 0 else '空'

class Thread_RefreshDisplayResult_Once(QThread):
    complete_name = pyqtSignal(str)

    def __init__(self, ui: QMainWindow, total_roster: dict):
        super(Thread_RefreshDisplayResult_Once, self).__init__()
        self.ui = ui
        self.wait_roster = get_wait_roster(total_roster)
        random.shuffle(self.wait_roster)
        self.length = len(self.wait_roster)

    def refresh(self):
        seed = int(time.time())
        random.seed(seed)

        self.ui.label_DisplayResult.setText('---')
        wait_name = '空'
        for i in range(int(math.pow(self.length, 2))):
            wait_name = random_name(self.wait_roster)
        self.ui.label_DisplayResult.setText(wait_name)

        return wait_name

    def run(self):
        self.ui.pushButton_Start.setEnabled(False)
        name = self.refresh()
        self.complete_name.emit(name)
        self.ui.pushButton_Start.setEnabled(True)
