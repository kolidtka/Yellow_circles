import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []  # Список для хранения окружностей в формате (x, y, diameter, color)

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            # Берем координаты, диаметр и цвет из каждого круга
            x, y, diameter, color = circle
            painter.setBrush(color)  # Устанавливаем цвет окружности
            painter.drawEllipse(x, y, diameter, diameter)  # Рисуем окружность

    def add_circle(self):
        # Генерируем случайные координаты и диаметр
        diameter = random.randint(20, 100)  # Случайный диаметр от 20 до 100
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Случайный цвет
        self.circles.append((x, y, diameter, color))  # Добавляем круг с цветом
        self.update()  # Обновление виджета для перерисовки


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Создаем основной layout
        self.layout = QVBoxLayout(self)

        # Создаем объект CircleWidget
        self.circle_widget = CircleWidget()
        self.circle_widget.setMinimumSize(400, 400)  # Установка минимальных размеров виджета кругов
        self.layout.addWidget(self.circle_widget)  # Добавляем circle_widget в layout

        # Создаем кнопку для добавления кругов
        self.pushButton = QPushButton("Добавить круг")
        self.layout.addWidget(self.pushButton)

        # Подключаем кнопку к функции добавления кругов
        self.pushButton.clicked.connect(self.circle_widget.add_circle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle('Circle Drawer')
    mainWindow.resize(400, 400)
    mainWindow.show()
    sys.exit(app.exec())
