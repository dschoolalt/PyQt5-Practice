import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My second cool GUI")
    self.setGeometry(700, 300, 720, 360)
    self.setWindowIcon(QIcon("image.png"))

def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())
  
if __name__ == "__main__":
  main()