import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt6.uic import loadUi


class DatabaseViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Загрузка интерфейса из файла .ui
        loadUi("main.ui", self)

        self.setWindowTitle("SQLite Database Viewer")

        # Хардкодим имя базы данных
        file_name = "coffee.sqlite"

        try:
            con = sqlite3.connect(file_name)
            cur = con.cursor()
            cur.execute("SELECT * FROM coffee")  # coffee - имя вашей таблицы
            data = cur.fetchall()

            # Используем первую строку для заголовков столбцов
            columns = [description[0] for description in cur.description]
            self.table.setColumnCount(len(columns))
            self.table.setHorizontalHeaderLabels(columns)

            self.table.setRowCount(len(data))

            for row_num, row_data in enumerate(data):
                for col_num, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.table.setItem(row_num, col_num, item)

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            con.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DatabaseViewer()
    window.show()
    sys.exit(app.exec())