from PyQt5.Qt import *
from UI.myRegister import Ui_Form


class RegisterClass(QWidget, Ui_Form):
    exit_signal = pyqtSignal()
    register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def show_not_equal(self):
        msg_box = QMessageBox(QMessageBox.Warning, '注册失败', '注册失败，密码输入不一致')
        msg_box.exec_()

    def notNumber(self):
        msg_box = QMessageBox(QMessageBox.Warning, '注册失败', '注册失败，首字母必须不是数字')
        msg_box.exec_()

    def sccess(self):
        msg_box = QMessageBox(QMessageBox.Warning, '注册成功', "注册成功，请牢记密码！")
        msg_box.exec_()

    def alreadyhad(self):
        msg_box = QMessageBox(QMessageBox.Warning, '注册失败', "注册失败，账号存在重复！！")
        msg_box.exec_()

    def notSpace(self):
        msg_box = QMessageBox(QMessageBox.Warning, '注册失败', '注册失败，不能存在空项')
        msg_box.exec_()
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = RegisterClass()
    window.show()
    sys.exit(app.exec_())
