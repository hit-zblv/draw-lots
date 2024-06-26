import utils.roster as roster
from PyQt6.QtWidgets import QMainWindow, QMessageBox

def load_config(ui: QMainWindow, total_roster: dict) -> None:
    """
    加载GUI静态配置
    :return: None
    """
    total_num = len(total_roster)
    leave_num = len(roster.get_leave_roster(total_roster))
    complete_num = len(roster.get_complete_roster(total_roster))
    wait_num = len(roster.get_wait_roster(total_roster))
    assert total_num == leave_num + wait_num + complete_num
    ui.label_TotalNum.setText(str(total_num))
    ui.label_LeaveNum.setText(str(leave_num))
    ui.label_CompleteNum.setText(str(complete_num))
    ui.label_WaitNum.setText(str(wait_num))
