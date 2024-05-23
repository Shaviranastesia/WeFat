import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem
from PyQt5.QtCore import Qt

kalori = {'nasi putih':175,
          'nasi merah':110,
          'kentang rebus':87,
          'ubi jalar':86,
          'singkong':160,
          'roti putih':66,
          'roti gandum':67,
          'mie goreng instan':350,
          'dada ayam goreng':216,
          'bebek goreng':286,
          'ikan lele goreng':105,
          'ikan salmon panggang':171,
          'udang goreng tepung':150,
          'bakso sapi':202,
          'chicken nugget':297,
          'telur orak-arik':199,
          'telur rebus':68,
          'telur dadar':93,
          'telur ceplok':92,
          'tempe goreng':118,
          'telur bacem':157,
          'tahu bacem':119,
          'tahu isi':124,
          'tahu bakso':119,
          'tumis kangkung':115,
          'apel':72,
          'pisang':105,
          'jambu biji':37,
          'jambu air':55,
          'semangka':30,
          'melon':34,
          'alpukat':322,
          'anggur':69,
          'jeruk':62,
          'salak':8,
          'manggis':73,
          'mangga':72,
          'buah naga':50}

jumlah_standard = {'nasi putih':100,
          'nasi merah':100,
          'kentang rebus':100,
          'ubi jalar':100,
          'singkong':100,
          'roti putih':1,
          'roti gandum':1,
          'mie goreng instan':80,
          'dada ayam goreng':100,
          'bebek goreng':100,
          'ikan lele goreng':100,
          'ikan salmon panggang':100,
          'udang goreng tepung':100,
          'bakso sapi':100,
          'chicken nugget':100,
          'telur orak-arik':2,
          'telur rebus':1,
          'telur dadar':1,
          'telur ceplok':1,
          'tempe goreng':100,
          'telur bacem':100,
          'tahu bacem':100,
          'tahu isi':100,
          'tahu bakso':100,
          'tumis kangkung':100,
          'apel':100,
          'pisang':100,
          'jambu biji':100,
          'jambu air':100,
          'semangka':100,
          'melon':100,
          'alpukat':100,
          'anggur':100,
          'jeruk':100,
          'salak':100,
          'manggis':100,
          'mangga':100,
          'buah naga':100}

def hitung_kalori(makanan, jumlah):
    try:
        jumlah_kalori = kalori[makanan.lower()] * jumlah / jumlah_standard[makanan.lower()]
    except KeyError:
        jumlah_kalori = 0
    return jumlah_kalori

class WeFatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("We Fat!")
        self.setGeometry(300, 100, 350, 145)
        self.setStyleSheet("background-color: #5c9090")

        self.layout = QVBoxLayout()

        self.greet_label = QLabel("Welcome to WeFat!")
        self.greet_label.setAlignment(Qt.AlignCenter)
        self.greet_label.setStyleSheet("font-size: 16pt; background-color: #5c9090; color: white")
        self.greet_label.setContentsMargins(30, 30, 30, 10)
        self.layout.addWidget(self.greet_label)

        self.total_food_label = QLabel("Jumlah makanan yang Anda makan")
        self.total_food_label.setAlignment(Qt.AlignCenter)
        self.total_food_label.setStyleSheet("color: white; font-size: 10pt")
        self.total_food_label.setContentsMargins(30, 0, 30, 12)
        self.layout.addWidget(self.total_food_label)

        self.layout.addSpacing(-25)

        self.total_food_edit = QLineEdit()
        self.total_food_edit.setStyleSheet("background-color: #bfd0ca")
        self.layout.addWidget(self.total_food_edit)
        self.total_food_edit.textChanged.connect(self.dynamic_food_input)

        self.setLayout(self.layout)

    def dynamic_food_input(self):
        try:
            total_food = int(self.total_food_edit.text())
        except ValueError:
            return

        self.greet_label.setVisible(False)
        self.total_food_label.setVisible(False)
        self.total_food_edit.setVisible(False)

        self.layout.addWidget(QLabel(""))
        self.layout.addWidget(QLabel(""))

        self.food_inputs = []
        for i in range(total_food):
            nama_makanan_label = QLabel(f"Nama Makanan {i + 1}")
            nama_makanan_label.setAlignment(Qt.AlignCenter)
            nama_makanan_label.setStyleSheet("color: white")
            self.layout.addWidget(nama_makanan_label)

            nama_makanan_edit = QLineEdit()
            nama_makanan_edit.setAlignment(Qt.AlignCenter)
            nama_makanan_edit.setStyleSheet("background-color: #bfd0ca")
            self.layout.addWidget(nama_makanan_edit)

            jumlah_label = QLabel(f"Jumlah Makanan {i + 1} (gram/butir/buah)")
            jumlah_label.setAlignment(Qt.AlignCenter)
            jumlah_label.setStyleSheet("color: white")
            self.layout.addWidget(jumlah_label)

            jumlah_edit = QLineEdit()
            jumlah_edit.setAlignment(Qt.AlignCenter)
            jumlah_edit.setStyleSheet("background-color: #bfd0ca")
            self.layout.addWidget(jumlah_edit)

            self.food_inputs.append(nama_makanan_edit)
            self.food_inputs.append(jumlah_edit)

        self.layout.addWidget(QLabel(""))
        calculate_button = QPushButton("Hitung Kalori")
        calculate_button.setStyleSheet("background-color: #ffe166; color: black")
        self.layout.addWidget(calculate_button)
        calculate_button.clicked.connect(self.calculate_calories)

    def calculate_calories(self):
        total_kalori = 0
        total_food = int(self.total_food_edit.text())

        for i in range(total_food):
            try:
                makanan_edit = self.food_inputs[i * 2].text()
                jumlah_edit = float(self.food_inputs[i * 2 + 1].text())
            except ValueError:
                self.warn_label = QLabel("Error: Invalid input!")
                self.warn_label.setAlignment(Qt.AlignCenter)
                self.warn_label.setStyleSheet("font-size: 10pt; color: red")
                self.layout.addWidget(self.warn_label)
                return

            total_kalori += hitung_kalori(makanan_edit, jumlah_edit)

        if hasattr(self, 'result_label'):
            self.warn_label.setVisible(False)

        self.result_label = QLabel(f"Total Kalori: {total_kalori} kkal")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 10pt; color: white")
        self.layout.addWidget(self.result_label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    we_fat = WeFatApp()
    we_fat.show()
    sys.exit(app.exec_())