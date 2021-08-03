from PyQt5.Qt import *
from UI.game import Ui_Form


class Game(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def right(self):
        msg_box = QMessageBox(QMessageBox.Warning, '正确', '恭喜回答正确！')
        msg_box.exec_()

    def wrong(self, ans):
        msg_box = QMessageBox(QMessageBox.Warning, '错误', '回答错误！！正确答案是{}'.format(ans))
        msg_box.exec_()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Game()
    window.show()
    sys.exit(app.exec_())
