#WIWIK PUTRI (F1D02310096) - C

import sys
# import widget dari PySide6 buat bikin tampilan GUI
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QComboBox, QMessageBox
)

# class utama buat form biodata mahasiswa (turunan dari QWidget)
class FormBiodata(QWidget):
    def __init__(self):
        super().__init__()
        # set judul window
        self.setWindowTitle("Form Biodata Mahasiswa")
        # set ukuran + posisi awal window
        self.setGeometry(100, 100, 300, 300)

        # styling biar tampilannya pink soft aesthetic
        self.setStyleSheet("""
            QWidget {
                background-color: #ffe4ec;
                font-family: Segoe UI;
            }
            QLabel {
                color: #7a3b5c;
                font-weight: 500;
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
            QComboBox {
                background-color: #fff0f5;
                border: 2px solid #f8b6cc;
                border-radius: 10px;
                padding: 5px;
                color: #7a3b5c;
            }

            QComboBox:hover {
                border: 2px solid #f48fb1;
            }

            QComboBox QAbstractItemView {
                background-color: #fff0f5;
                border: 2px solid #f8b6cc;
                selection-background-color: #f8b6cc;
                selection-color: white;
                color: #7a3b5c;
            }
            QPushButton {
                background-color: #f8b6cc;
                border-radius: 12px;
                padding: 7px;
                font-weight: bold;
                color: white;
            }
            QPushButton:hover {
                background-color: #f48fb1;
            }
        """)

        # layout utama (vertical)
        layout = QVBoxLayout()

        # Nama
        # label + input buat isi nama lengkap
        self.nama_label = QLabel("Nama Lengkap:")
        self.nama_input = QLineEdit()

        # NIM
        # label + input buat isi NIM
        self.nim_label = QLabel("NIM:")
        self.nim_input = QLineEdit()
        self.nim_input.setPlaceholderText("Masukkan NIM")

        # Kelas
        # label + input buat isi kelas
        self.kelas_label = QLabel("Kelas:")
        self.kelas_input = QLineEdit()
        self.kelas_input.setPlaceholderText("Contoh: TI-2A")

        # Jenis Kelamin
        # combobox buat milih jenis kelamin
        self.jk_label = QLabel("Jenis Kelamin:")
        self.jk_combo = QComboBox()
        self.jk_combo.addItems(["Laki-laki", "Perempuan"])

        # Tombol
        # tombol buat nampilin data + reset form
        self.tampil_btn = QPushButton("Tampilkan")
        self.reset_btn = QPushButton("Reset")

        # Hasil
        # label buat nampilin hasil biodata
        self.hasil_label = QLabel("DATA BIODATA")

        # Event
        # hubungkan tombol ke function masing-masing
        self.tampil_btn.clicked.connect(self.tampilkan_data)
        self.reset_btn.clicked.connect(self.reset_data)

        # Layout
        # masukin semua komponen ke layout
        layout.addWidget(self.nama_label)
        layout.addWidget(self.nama_input)

        layout.addWidget(self.nim_label)
        layout.addWidget(self.nim_input)

        layout.addWidget(self.kelas_label)
        layout.addWidget(self.kelas_input)

        layout.addWidget(self.jk_label)
        layout.addWidget(self.jk_combo)

        layout.addWidget(self.tampil_btn)
        layout.addWidget(self.reset_btn)
        layout.addWidget(self.hasil_label)

        self.setLayout(layout)

    # function buat nampilin data dari input user
    def tampilkan_data(self):
        nama = self.nama_input.text()
        nim = self.nim_input.text()
        kelas = self.kelas_input.text()
        jk = self.jk_combo.currentText()

        # validasi biar ga ada yang kosong
        if not nama or not nim or not kelas:
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        # format output biodata
        hasil = f"""
DATA BIODATA

Nama: {nama}
NIM: {nim}
Kelas: {kelas}
Jenis Kelamin: {jk}
"""
        self.hasil_label.setText(hasil)

    # function buat reset semua input
    def reset_data(self):
        self.nama_input.clear()
        self.nim_input.clear()
        self.kelas_input.clear()
        self.jk_combo.setCurrentIndex(0)
        self.hasil_label.setText("DATA BIODATA")


# bagian main biar program bisa dijalankan
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())