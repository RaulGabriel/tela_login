import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFrame
)
from PyQt6.QtGui import QFont, QPalette, QColor, QIcon
from PyQt6.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - PyQt6")
        self.setFixedSize(400, 300)
        self.setStyle()
        self.init_ui()

    def setStyle(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                font-family: 'Segoe UI';
            }
            QLabel {
                color: #ffffff;
            }
            QLineEdit {
                padding: 8px;
                border-radius: 5px;
                border: 1px solid #555;
                background-color: #1e1e1e;
                color: #ddd;
            }
            QPushButton {
                padding: 10px;
                background-color: #58a6ff;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #409eff;
            }
        """)

    def init_ui(self):
        title = QLabel("Bem-vindo de volta")
        title.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        user_label = QLabel("Usuário:")
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Digite seu usuário")

        pass_label = QLabel("Senha:")
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Digite sua senha")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)

        login_button = QPushButton("Entrar")
        login_button.clicked.connect(self.check_login)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(user_label)
        layout.addWidget(self.user_input)
        layout.addWidget(pass_label)
        layout.addWidget(self.pass_input)
        layout.addSpacing(20)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.user_input.text()
        password = self.pass_input.text()
        if username == "admin" and password == "cusão":
            QMessageBox.information(self, "Sucesso", "✅ Login realizado com sucesso!")
        else:
            QMessageBox.critical(self, "Erro", "❌ Usuário ou senha incorretos.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
