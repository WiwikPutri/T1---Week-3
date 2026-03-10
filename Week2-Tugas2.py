#WIWIK PUTRI (F1D02310096) - C

import sys
# import widget dari PySide6 buat bikin tampilan GUI
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
)

# class utama buat program konversi suhu (turunan dari QWidget)
class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()
        # set judul window
        self.setWindowTitle("Konversi Suhu")
        # set ukuran + posisi awal window
        self.setGeometry(100, 100, 320, 250)

        # styling biar tampilannya pink soft aesthetic (warna kesukaan saya)
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
                selection-background-color: #f8b6cc;
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
        """)

        # layout utama (vertikal)
        layout = QVBoxLayout()

        # Judul
        # label judul program
        self.judul = QLabel("KONVERSI SUHU")
        self.judul.setStyleSheet("font-size:16px; font-weight:bold; text-align:center;")

        # Input
        # label + input buat masukin suhu dalam celsius
        self.label_input = QLabel("Masukkan Suhu (Celsius):")
        self.input_suhu = QLineEdit()

        # Tombol
        # layout horizontal buat tombol pilihan konversi
        btn_layout = QHBoxLayout()
        self.btn_f = QPushButton("Fahrenheit")
        self.btn_k = QPushButton("Kelvin")
        self.btn_r = QPushButton("Reamur")

        btn_layout.addWidget(self.btn_f)
        btn_layout.addWidget(self.btn_k)
        btn_layout.addWidget(self.btn_r)

        # Hasil
        # label buat nampilin hasil konversi
        self.label_hasil = QLabel("Hasil Konversi:\n")

        # Event tombol
        # hubungkan tombol ke function masing-masing
        self.btn_f.clicked.connect(self.ke_fahrenheit)
        self.btn_k.clicked.connect(self.ke_kelvin)
        self.btn_r.clicked.connect(self.ke_reamur)

        # Layout
        # masukin semua komponen ke layout
        layout.addWidget(self.judul)
        layout.addWidget(self.label_input)
        layout.addWidget(self.input_suhu)
        layout.addLayout(btn_layout)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

    # Validasi angka
    # ambil input dari user terus dicek apakah angka
    def ambil_input(self):
        try:
            return float(self.input_suhu.text())
        except:
            QMessageBox.warning(self, "Error", "Input harus berupa angka!")
            return None

    # Konversi ke Fahrenheit
    def ke_fahrenheit(self):
        c = self.ambil_input()
        if c is not None:
            f = (c * 9/5) + 32
            self.label_hasil.setText(f"Hasil Konversi:\n{c:.2f} Celsius = {f:.2f} Fahrenheit")

    # Konversi ke Kelvin
    def ke_kelvin(self):
        c = self.ambil_input()
        if c is not None:
            k = c + 273.15
            self.label_hasil.setText(f"Hasil Konversi:\n{c:.2f} Celsius = {k:.2f} Kelvin")

    # Konversi ke Reamur
    def ke_reamur(self):
        c = self.ambil_input()
        if c is not None:
            r = c * 4/5
            self.label_hasil.setText(f"Hasil Konversi:\n{c:.2f} Celsius = {r:.2f} Reamur")


# bagian main biar program bisa dijalankan
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())