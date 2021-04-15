from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Loading(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(350, 350)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.label_animation = QLabel(self)
        self.movie = QMovie('Mr bean.gif')
        self.label_animation.setMovie(self.movie)
        counter =QTimer(self)
        self.Animation()
        counter.singleShot(1500, self.EndAnimation)
        self.show()

    def Animation(self):
        self.movie.start()

    def EndAnimation(self):
        self.movie.stop()
        self.close()

class Tab(QMainWindow):
    def __init__(self):

        super().__init__()
        self.setStyleSheet("background-color: powderblue ;")
        self.loading_screen = Loading()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://127.0.0.1:5000'))
        self.setCentralWidget(self.browser)

        #self.setFixedWidth(1200)

        self.showMaximized()


        # navbar
        buttons = QToolBar()
        self.addToolBar(buttons)

        backbutton = QAction('Previous Tab', self)
        backbutton.triggered.connect(self.browser.back)
        buttons.addAction(backbutton)

        forwardbutton = QAction('Next Tab', self)
        forwardbutton.triggered.connect(self.browser.forward)
        buttons.addAction(forwardbutton)

        reloadbutton = QAction('Refresh', self)
        reloadbutton.triggered.connect(self.browser.reload)
        buttons.addAction(reloadbutton)

        Homebutton =QAction('Home', self)
        Homebutton.triggered.connect(self.navigate)
        buttons.addAction(Homebutton)

        self.URL = QLineEdit()
        self.URL.returnPressed.connect(self.to_url)
        buttons.addWidget(self.URL)
        self.browser.urlChanged.connect(self.new_url)


    def navigate(self):
        self.browser.setUrl(QUrl("https://www.google.com/"))

    def to_url(self):
        url = self.URL.text()
        self.browser.setUrl(QUrl(url))

    def new_url(self, Link):
        self.URL.setText(Link.toString())


target = QApplication(sys.argv)
QApplication.setApplicationName('Chrome Killer')
window = Tab()
target.exec_()