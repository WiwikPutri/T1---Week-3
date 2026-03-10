#WIWIK PUTRI (F1D02310096) - C

import sys
# import library widget dari PySide6 buat bikin tampilan GUI
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox
)
# import Qt buat align dll
from PySide6.QtCore import Qt

# class utama buat tampilan login (turunan dari QWidget)
class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        # set judul window
        self.setWindowTitle("Login")
        # set ukuran + posisi window pas muncul
        self.setGeometry(100, 100, 330, 330)

        # styling semua komponen biar tampilannya pink aesthetic
        self.setStyleSheet("""
        QWidget {
            background-color: #ffe4ec;
            font-family: Segoe UI;
        }

        QLabel {
            color: #7a3b5c;
        }

        QLineEdit {
            background-color: #fff0f5;
            border: 2px solid #f8b6cc;
            border-radius: 10px;
            padding: 6px;
            color: #7a3b5c;
        }

        QLineEdit:focus {
            border: 2px solid #f48fb1;
        }

        QPushButton {
            background-color: #f8b6cc;
            border-radius: 10px;
            padding: 6px;
            font-weight: bold;
            color: white;
        }

        QPushButton:hover {
            background-color: #f48fb1;
        }

        QCheckBox {
            color: #7a3b5c;
            spacing: 6px;
        }

        QCheckBox::indicator {
            width: 18px;
            height: 18px;
        }

        QCheckBox::indicator:unchecked {
            border: 2px solid #f48fb1;
            background: white;
            border-radius: 4px;
        }

        QCheckBox::indicator:checked {
            border: 2px solid #f48fb1;
            background: #f48fb1;
            border-radius: 4px;
        }
        """)

        # layout utama (vertical, jadi komponen ke bawah semua)
        layout = QVBoxLayout()

        # JUDUL
        # label judul login di tengah
        self.judul = QLabel("LOGIN")
        self.judul.setAlignment(Qt.AlignCenter)
        self.judul.setStyleSheet("font-size:18px; font-weight:bold;")
        layout.addWidget(self.judul)

        # USERNAME
        # label + input buat username
        layout.addWidget(QLabel("Username:"))
        self.input_username = QLineEdit()
        layout.addWidget(self.input_username)

        # PASSWORD
        # label + input password (default disembunyiin)
        layout.addWidget(QLabel("Password:"))
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_password)

        # CHECKBOX
        # checkbox buat nampilin / nyembunyiin password
        self.checkbox = QCheckBox("Tampilkan Password")
        self.checkbox.stateChanged.connect(self.toggle_password)
        layout.addWidget(self.checkbox)

        # TOMBOL
        # layout horizontal buat tombol login + reset
        btn_layout = QHBoxLayout()
        self.btn_login = QPushButton("Login")
        self.btn_reset = QPushButton("Reset")

        # connect tombol ke function masing-masing
        self.btn_login.clicked.connect(self.login)
        self.btn_reset.clicked.connect(self.reset_form)

        btn_layout.addWidget(self.btn_login)
        btn_layout.addWidget(self.btn_reset)
        layout.addLayout(btn_layout)

        # HASIL
        # label buat nampilin hasil login
        self.label_hasil = QLabel("")
        self.label_hasil.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label_hasil)

        # set layout ke window
        self.setLayout(layout)

    # function buat toggle tampil / sembunyi password
    def toggle_password(self):
        if self.checkbox.isChecked():
            self.input_password.setEchoMode(QLineEdit.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.Password)

    # function buat ngecek username + password
    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        # validasi sederhana (hardcode)
        if username == "admin" and password == "12345":
            self.label_hasil.setText("Login berhasil! Selamat datang, admin.")
            self.label_hasil.setStyleSheet("""
                background:#d4edda;
                color:#155724;
                padding:8px;
                border-radius:8px;
            """)
        else:
            self.label_hasil.setText("Login gagal! Username atau password salah.")
            self.label_hasil.setStyleSheet("""
                background:#f8d7da;
                color:#721c24;
                padding:8px;
                border-radius:8px;
            """)

    # function buat kosongin semua input
    def reset_form(self):
        self.input_username.clear()
        self.input_password.clear()
        self.checkbox.setChecked(False)
        self.label_hasil.setText("")


# bagian main (biar program bisa jalan)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())