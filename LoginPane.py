from PyQt5.Qt import *
from UI.myLogin import Ui_Form


class LoginClass(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def show_error_animation(self):
        msg_box = QMessageBox(QMessageBox.Warning, '登录失败', '登陆失败，请检查账号是否正确填写(首字母必须不是数字)，或者密码是否填写正确！')
        msg_box.exec_()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LoginClass()
    window.show()
    sys.exit(app.exec_())
