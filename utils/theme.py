from PyQt6.QtWidgets import QMainWindow

# ==== pushButton样式 ====
pushButton_style_disabled = """
    QPushButton {
        background-color: rgb(236, 236, 236);  /* 设置背景颜色 */
        color: rgb(134, 134, 134);  /* 设置字体颜色 */
        font-size: 12px;  /* 设置字体大小 */
        border: 1px solid rgb(217, 217, 217);  /* 设置边框样式 */
        border-radius: 5px;  /* 设置边框的圆角半径 */
        padding: 5px;  /* 设置内边距 */
    }
"""
pushButton_style_unclicked = """
    QPushButton {
        background-color: rgb(253, 253, 253);  /* 设置背景颜色 */
        color: rgb(0, 0, 0);  /* 设置字体颜色 */
        font-size: 12px;  /* 设置字体大小 */
        border: 1px solid rgb(210, 210, 210);  /* 设置边框样式 */
        border-radius: 5px;  /* 设置边框的圆角半径 */
        padding: 5px;  /* 设置内边距 */
    }
    QPushButton:hover {
        background-color: rgb(245, 245, 245);  /* 设置背景颜色 */
        color: rgb(26, 26, 26);  /* 设置字体颜色 */
    }
"""
pushButton_style_clicked = """
    QPushButton {
        background-color: rgb(0, 66, 153);  /* 设置背景颜色 */
        color: rgb(255, 255, 255);  /* 设置字体颜色 */
        font-size: 12px;  /* 设置字体大小 */
        border: 1px solid rgb(210, 210, 210);  /* 设置边框样式 */
        border-radius: 5px;  /* 设置边框的圆角半径 */
        padding: 5px;  /* 设置内边距 */
    }
    QPushButton:hover {
        background-color: rgb(0, 94, 114);  /* 设置背景颜色 */
        color: rgb(216, 236, 216);  /* 设置字体颜色 */
    }
"""


def set_StaticTheme(ui: QMainWindow):
    # 设置pushButton样式
    ui.pushButton_LeaveNameList.setStyleSheet(pushButton_style_unclicked)
    ui.pushButton_CompleteNameList.setStyleSheet(pushButton_style_unclicked)
    ui.pushButton_WaitNameList.setStyleSheet(pushButton_style_unclicked)
    ui.pushButton_Start.setStyleSheet(pushButton_style_unclicked)
    ui.pushButton_Reset.setStyleSheet(pushButton_style_unclicked)
