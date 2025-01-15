import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []  # Список для хранения окружностей

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            # Установим цвет окружности
            painter.setBrush(QColor(255, 255, 0))  # Желтый цвет
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])  # Рисуем окружность

    def add_circle(self):
        # Генерируем случайные координаты и диаметр
        if self.width() <= 0 or self.height() <= 0:
            return  # Убедимся, что размеры положительные

        diameter = random.randint(20, 100)  # Случайный диаметр от 20 до 100
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()  # Обновление виджета для перерисовки


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('UI.ui', self)  # Загружаем интерфейс из UI.u

        # Создаем объект CircleWidget
        self.circle_widget = CircleWidget()

        # Убедитесь, что `circle_widget` добавляется в layout
        self.layout.addWidget(self.circle_widget)

        # Устанавливаем минимальные размеры для circle_widget
        self.circle_widget.setMinimumSize(400, 400)  # Установка минимальных размеров виджета кругов

        # Подключаем кнопку к функции добавления кругов
        self.pushButton.clicked.connect(self.circle_widget.add_circle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle('Circle Drawer')
    mainWindow.resize(400, 400)
    mainWindow.show()
    sys.exit(app.exec())
