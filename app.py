import sqlite3
import datetime
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):
    def startup(self):
        # Подключение к базе данных SQLite
        self.conn = sqlite3.connect('C:/Users/Maksz/beeware-tutorial/database.db')
        self.cursor = self.conn.cursor()
        
        # Создание таблиц, если их ещё нет
        self.create_table()

        # Основной контейнер
        main_box = toga.Box(style=Pack(direction=COLUMN))


        # Контейнер для полей ввода и кнопки
        top_container = toga.Box(style=Pack(direction=COLUMN, padding=25))

        # Метка и текстовое поле для ввода логина
        username_label = toga.Label("Username:", 
        style=Pack
        (padding=(5, 5)))
        
        self.username_input = toga.TextInput(readonly=True, style=Pack(flex=1,))

        # Метка и текстовое поле для ввода пароля
        password_label = toga.Label("Password:", style=Pack(padding=(5, 5)))
        self.password_input = toga.PasswordInput(readonly=True, style=Pack(flex=1))


        # Горизонтальные боксы для размещения меток и полей ввода
        username_box = toga.Box(style=Pack(direction=ROW, padding=5))
        username_box.add(username_label)
        username_box.add(self.username_input)

        password_box = toga.Box(style=Pack(direction=ROW, padding=5))
        password_box.add(password_label)
        password_box.add(self.password_input)

        # Кнопка для отправки формы
        submit_button = toga.Button(
            "Submit", on_press=self.submit_form, style=Pack(padding=(10,10))
        )

        # Добавляем элементы в верхний контейнер
        top_container.add(username_box)
        top_container.add(password_box)
        top_container.add(submit_button)

        # Нижний контейнер для кнопок-клавиатуры
        keyboard_container = toga.Box(
            style=
        Pack(direction=COLUMN,
         padding=(1,750)))
        

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

        # Устанавливаем начальное активное поле
        self.username_input.on_gain_focus = self.on_username_focus
        self.password_input.on_gain_focus = self.on_password_focus
        # Устанавливаем начальное активное поле
        self.active_field = self.username_input
    

    def on_username_focus(self, widget):
        self.active_field = self.username_input

    def on_password_focus(self, widget):
        self.active_field = self.password_input

    def button_pressed(self, widget):
        # Добавляем текст кнопки в активное текстовое поле
        self.active_field.value += widget.text


    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                timestamp TEXT,
                login TEXT,
                password TEXT,
                result TEXT
            );
        ''')
        self.conn.commit()



    def backspace_pressed(self, widget):
        # Удаляем последний символ из активного текстового поля
        if self.active_field.value:
            self.active_field.value = self.active_field.value[:-1]

    def submit_form(self, widget):
        # Обработчик события нажатия на кнопку Submit
        login = self.username_input.value
        password = self.password_input.value
        print(f"Login: {login}, Password: {password}")

        # Проверяем, введен ли корректный логин
        if login:
            if login == 'maks':
                greeting = 'GOOD job'
            else:
                greeting = 'idiot'

            # Логируем запись в базу данных
            timestamp = str(datetime.datetime.now())
            self.cursor.execute(
                "INSERT INTO logs (timestamp, login, password, result) VALUES (?, ?, ?, ?)",
                (timestamp, login, password, greeting)
            )

            self.conn.commit()

            # Выводим сообщение
            dialog = toga.InfoDialog(title="Hi there!", message=greeting)
            dialog._show(self.main_window)
        else:
            # Ошибка, если логин пустой
            dialog = toga.InfoDialog(title="Error", message="Please enter your login!")
            dialog._show(self.main_window)


    def on_usernamee_input_changed(self, widget):
        self.username_input.on_gain_focus = lambda w: self.focus_change_handler(w, True)
        pass
    def on_password_input_changed(self, widget):
        self.password_input.on_gain_focus = lambda w: self.focus_change_handler(w, True)
        pass

    def activate_fields(self):
        # Назначаем обработчики смены фокуса
        self.username_input.on_gain_focus = lambda w: self.focus_change_handler(w, True)
        self.password_input.on_gain_focus = lambda w: self.focus_change_handler(w, True)


def main():
    return HelloWorld(formal_name='Hello World')


# Запускаем приложение
if __name__ == '__main__':
    app = main()
    app.activate_fields()  # Активируем отслеживание фокуса
    app.main_loop()