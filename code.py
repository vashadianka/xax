from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()
mainline = QVBoxLayout()

window.setLayout(mainline)
window.show()
app.exec()