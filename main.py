from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

import sys, time, os


class WebCharts(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("PyQt5 Web Charts")
        self.setGeometry(10, 40, 940, 620)
        self.base = r'file:///d:/charts/echarts/'  # 默认的路径
        self.url = r""  # 默认render.html
        self.num = len(self.getHtmlFile())
        self.combo = QComboBox(self)
        self.combo.addItems(self.getHtmlFile())
        self.combo.currentIndexChanged.connect(self.changeUrl)
        self.url = self.combo.currentText()
        self.refreshTime = 10000  # 初始刷新秒数

        self.browser = QWebEngineView(self)
        self.browser.setGeometry(0, 0, self.width(), self.height() - 50)
        self.browser.load(QUrl(self.base + self.url))

        self.btn = QPushButton("手动刷新网页")
        self.btn.clicked.connect(lambda: self.loadweb(self.base + self.url))

        self.btn_auto = QPushButton('自动刷新网页')
        self.btn_auto.clicked.connect(self.autoload)

        self.timer = QTimer(self)  # 根据self.refresh设置的秒数刷新计时器
        self.timer.timeout.connect(lambda: self.loadweb(self.base + self.url))
        self.btn_data = QPushButton('刷新数据')
        self.btn_data.clicked.connect(self.reloadData)

        self.lineEdit=QLineEdit()
        #https://www.makeapie.com/preview.html?c=x-tlZUDQhT&v=3
        #https://www.makeapie.com/preview.html?c=xTGZitHiBB&v=10
        self.lineEdit.setText(r'https://www.makeapie.com/preview.html?c=x_kEnG-Ggq&v=2')
        #self.lineEdit.setPlaceholderText("请输入一个外部网址！格式http://www...")
        self.btn_line=QPushButton("载入外部图表")
        self.btn_line.clicked.connect(lambda:self.loadweb(self.lineEdit.text()))

        hbox = QHBoxLayout()
        hbox.addWidget(self.combo)
        hbox.addWidget(self.btn)
        hbox.addWidget(self.btn_auto)
        hbox.addWidget(self.btn_data)

        hbox2 = QHBoxLayout()  #增加一个新的水平布局
        hbox2.addWidget(self.lineEdit)
        hbox2.addWidget(self.btn_line)


        hboxweb = QHBoxLayout()
        hboxweb.addWidget(self.browser)

        vbox = QVBoxLayout()
        vbox.addLayout(hboxweb)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def loadweb(self, url):
        '''载入传入的本地html文件的url'''
        # 启动窗口时自动载入下拉框中的当前html文件
        self.browser.load(QUrl(url))

    def changeUrl(self):
        '''改变下拉框中的html文件名称'''
        # 设置类属性self.url的值为下拉框的当前值
        self.url = self.combo.currentText()
        # 发射按钮的clicked信号
        self.btn.clicked.emit()

    # TODO(zhou):实现按钮的停止刷新文字倒计时5秒
    def autoload(self):
        '''每隔5秒 ，自动更新当前页面的数据'''
        # 获取当前信号发送者
        sender = self.sender()
        if sender.text() == '自动刷新网页':
            self.btn_auto.setText('停止刷新')
            self.timer.start(self.refreshTime)
        elif sender.text() == '停止刷新':
            self.timer.stop()
            self.btn_auto.setText('自动刷新网页')

    def getHtmlFile(self):
        '''获取当前echarts文件夹中的所有html文件名'''
        fileList = os.listdir('./echarts/')
        return fileList  # 返回获得的当前文件夹中的文件名列表

    def reloadData(self):
        '''手动刷新下拉列表中的文件名'''
        file = self.getHtmlFile()  # 获取./echarts目录下的所有html文件名列表
        currentText = self.combo.currentText()  # 用currentText记录原下拉框的当前项文本值

        self.combo.clear()
        self.combo.addItems(file)

        c_index = self.combo.findText(currentText)  # c_index 当能查到加载前的下拉项文本，ok ；若不能查询到原先相同文件名则设置c_index为默认0值，及显示新内容的首条记录
        if c_index == -1:
            c_index = 0
        self.combo.setCurrentIndex(c_index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = WebCharts()
    demo.show()
    sys.exit(app.exec_())
