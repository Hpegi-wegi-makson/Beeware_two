import sqlite3
import datetime
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):
    def startup(self):
        # Подключаемся к базе данных SQLite
        self.conn = sqlite3.connect('C://Users//Maksz//beeware-tutorial//database.db')  # создаем/открываем базу данных  # создаем/открываем базу данных
        self.cursor = self.conn.cursor()  # создаем курсор для выполнения запросов

        # Создаем таблицы, если их еще нет
        self.create_tables()

        # Остальная часть кода остается без изменений...
        # Создаем основной контейнер
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Верхний контейнер для полей ввода и кнопки Say Hello!
        top_container = toga.Box(style=Pack(direction=COLUMN, padding=25))

        # Добавляем метку и текстовое поле для ввода имени
        name_label = toga.Label("Login:", style=Pack(padding=(5, 5)))
        self.name_input = toga.TextInput(readonly=True, style=Pack(flex=1))
        pasword_label = toga.Label("Pasword:", style=Pack(padding=(-5, -0)))
        self.pasword_input = toga.TextInput(readonly=True, style=Pack(flex=1))  # Поле только для чтения

        # Горизонтальный бокс для размещения метки и поля ввода
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        pasword_box = toga.Box(style=Pack(direction=ROW, padding=5))
        pasword_box.add( pasword_label)
        pasword_box.add( self.pasword_input)

        # Кнопка для вывода приветствия
        hello_button = toga.Button(
            "go", on_press=self.say_hello, style=Pack(padding=50)
        )

        # Добавляем элементы в верхний контейнер
        top_container.add(name_box)
        top_container.add(hello_button)
        top_container.add(pasword_box)

        # Нижний контейнер для кнопок-клавиатуры
        keyboard_container = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Количество кнопок в одном ряду
        buttons_per_row = 8  # уменьшаем количество кнопок в ряду, чтобы вместить Backspace

        # Английский алфавит
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        # Создаем ряды кнопок
        for row_index in range(len(alphabet) // buttons_per_row + 1):
            row_box = toga.Box(style=Pack(direction=ROW))
            for col_index in range(min(buttons_per_row, len(alphabet) - row_index * buttons_per_row)):
                letter = alphabet[row_index * buttons_per_row + col_index]
                button = toga.Button(letter, on_press=self.button_pressed)
                button.style.update(width=50, height=50)
                row_box.add(button)
            keyboard_container.add(row_box)

        # Добавляем кнопку Backspace
        backspace_button = toga.Button('⌫', on_press=self.backspace_pressed)
        backspace_button.style.update(width=50, height=50)
        keyboard_container.add(backspace_button)

        # Добавляем оба контейнера в основной бокс
        main_box.add(top_container)
        main_box.add(keyboard_container)

        # Создаем главное окно приложения
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def create_tables(self):
        # Создаем таблицу logs, если ее еще нет
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                input_text TEXT,
                result TEXT
            );
        ''')
        self.conn.commit()

    def log_entry(self, input_text, result):
        # Логируем запись в базу данных
        timestamp = str(datetime.datetime.now())
        self.cursor.execute("INSERT INTO logs (timestamp, input_text, result) VALUES (?, ?, ?)", (timestamp, input_text, result))
        self.conn.commit()
        self.cursor.execute('SELECT timestamp, input_text, result FROM logs')
        results = self.cursor.fetchall()
        print(results)


    def button_pressed(self, widget):
        # Добавляем текст кнопки в текстовое поле
        self.name_input.value += widget.text
        self.pasword_input.value += widget.text

    def backspace_pressed(self, widget):
        # Удаляем последний символ из текстового поля
        current_text = self.name_input.value
        if current_text:
            self.name_input.value = current_text[:-1]

    def backspace_pressed_two(self, widget):
        # Удаляем последний символ из текстового поля
        current_text = self.pasword_input.value
        if current_text:
            self.pasword_input.value = current_text[:-1]

    def say_hello(self, widget):
        # Получаем значение из текстового поля
        name = self.name_input.value.strip()
        pasword = self.pasword_input.value.strip()

        # Проверяем, введен ли корректный имя
        if name:
            if name == 'maks':
                greeting = 'GOOD job'
            else:
                greeting = 'idiot'

            # Логируем запись
            self.log_entry(name, greeting)

            # Выводим сообщение
            dialog = toga.InfoDialog(title="Hi there!", message=greeting)
            dialog._show(self.main_window)
        else:
            # Ошибка, если имя пустое
            dialog = toga.InfoDialog(title="Error", message="Please enter your name!")
            dialog._show(self.main_window)


def main():
    return HelloWorld(formal_name='Hello World')


# Запускаем приложение
if __name__ == '__main__':
    app = main()
    app.main_loop()