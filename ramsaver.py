import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, 
                            QLineEdit, QAction, QVBoxLayout, QWidget)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Browser")
        self.setGeometry(100, 100, 1024, 768)
        
        # Создаем виджет браузера
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        
        # Панель инструментов
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Кнопка "Назад"
        back_btn = QAction("←", self)
        back_btn.triggered.connect(self.browser.back)
        toolbar.addAction(back_btn)
        
        # Кнопка "Вперед"
        forward_btn = QAction("→", self)
        forward_btn.triggered.connect(self.browser.forward)
        toolbar.addAction(forward_btn)
        
        # Кнопка "Обновить"
        reload_btn = QAction("↻", self)
        reload_btn.triggered.connect(self.browser.reload)
        toolbar.addAction(reload_btn)
        
        # Кнопка "Домой"
        home_btn = QAction("⌂", self)
        home_btn.triggered.connect(self.navigate_home)
        toolbar.addAction(home_btn)
        
        # Адресная строка
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        toolbar.addWidget(self.url_bar)
        
        # Настройки по умолчанию
        self.home_url = 'https://www.google.com'
        
        # Обновляем urlbar при изменении url
        self.browser.urlChanged.connect(self.update_urlbar)
        
        # Обновляем title при изменении
        self.browser.titleChanged.connect(self.update_title)
        
        self.setCentralWidget(self.browser)
    
    def navigate_home(self):
        self.browser.setUrl(QUrl(self.home_url))
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))
    
    def update_urlbar(self, qurl):
        self.url_bar.setText(qurl.toString())
        self.url_bar.setCursorPosition(0)
    
    def update_title(self, title):
        self.setWindowTitle(f"{title} - Python Browser")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Python Browser")
    
    browser = Browser()
    browser.show()
    
    sys.exit(app.exec_())