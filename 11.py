from PIL import Image
import sys
from PyQt4.QtGui import *

class App(QDialog):
    def __init__(self,parent=None):
        super(App,self).__init__(parent)
        window = QGridLayout()

        im = Image.open(path).convert('RGBA')
        data = im.tobytes('raw', 'BGRA')
        image = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
        pix = QPixmap.fromImage(image)
        lbl = QLabel()
        lbl.setPixmap(pix)
        window.addWidget(lbl,0,0)

        self.setLayout(window)

Application = QApplication(sys.argv)
app = App()
app.show()
Application.exec_()
