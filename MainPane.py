from PyQt5.Qt import *
from UI.MainScreen import Ui_Form


class MainClass(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


    def notNumber(self):
        msg_box = QMessageBox(QMessageBox.Warning, '提交失败', '请输入1-20内的数字！')
        msg_box.exec_()

    def success(self):
        msg_box = QMessageBox(QMessageBox.Warning, '提交成功', '提交成功，马上进入游戏！')
        msg_box.exec_()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainClass()
    window.show()
    sys.exit(app.exec_())
