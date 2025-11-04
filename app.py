import sqlite3
import datetime
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):
    def __init__(self):
        super().__init__(
            formal_name='Hello World',
            app_id='com.example.helloworld'
        )

    def startup(self, widget=None):
        self.create_element_interface()
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.sqsl()
        self.account()

        # Создаем главное окно
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Создаем главный контейнер
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Создаем контейнеры для клавиатур
        self.keyboard_container = toga.Box(style=Pack(direction=COLUMN, padding=5))
        self.keyboard_container_qwe = toga.Box(style=Pack(direction=COLUMN, padding=5))

        # Генерируем клавиатуры
        self.generate_keyboard()
        self.generate_keyboard_qwe()

        # Показываем начальный экран
        self.login_scrin()

        # Устанавливаем содержимое окна
        self.main_window.content = self.main_box
        self.main_window.show()

    def show_keyboard(self):
        if self.keyboard_container not in self.main_box.children:
            self.main_box.add(self.keyboard_container)

    def show_keyboard_qwe(self):
        if self.keyboard_container_qwe not in self.main_box.children:
            self.main_box.add(self.keyboard_container_qwe)

    def hide_keyboard(self):
        if self.keyboard_container in self.main_box.children:
            self.main_box.remove(self.keyboard_container)

    def hide_keyboard_qwe(self):
        if self.keyboard_container_qwe in self.main_box.children:
            self.main_box.remove(self.keyboard_container_qwe)

    def generate_keyboard(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        buttons_per_row = 8
        for row_index in range(len(alphabet) // buttons_per_row + 1):
            row_box = toga.Box(style=Pack(direction=ROW))
            for col_index in range(min(buttons_per_row, len(alphabet) - row_index * buttons_per_row)):
                letter = alphabet[row_index * buttons_per_row + col_index]
                button = toga.Button(
                    letter,
                    on_press=self.button_pressed,
                    style=Pack(width=25, height=25)
                )
                row_box.add(button)
            self.keyboard_container.add(row_box)

        self.keyboard_container.add(self.backspace_button)

    def backspace_pressed(self, widget):
        if self.active_field and self.active_field.value:
            self.active_field.value = self.active_field.value[:-1]

    def button_pressed(self, widget):
        if self.active_field:
            self.active_field.value += widget.text

    def on_username_focus(self, widget):
        self.active_field = self.username_input

    def on_password_focus(self, widget):
        self.active_field = self.password_input

    def generate_keyboard_qwe(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        buttons_per_row = 8
        for row_index in range(len(alphabet) // buttons_per_row + 1):
            row_box = toga.Box(style=Pack(direction=ROW))
            for col_index in range(min(buttons_per_row, len(alphabet) - row_index * buttons_per_row)):
                letter = alphabet[row_index * buttons_per_row + col_index]
                button = toga.Button(
                    letter,
                    on_press=self.button_pressed_qwe,
                    style=Pack(width=25, height=25)
                )
                row_box.add(button)
            self.keyboard_container_qwe.add(row_box)

        self.keyboard_container_qwe.add(self.backspace_button_qwe)

    def backspace_pressed_qwe(self, widget):
        if self.active_field_qwe and self.active_field_qwe.value:
            self.active_field_qwe.value = self.active_field_qwe.value[:-1]

    def button_pressed_qwe(self, widget):
        if self.active_field_qwe:
            self.active_field_qwe.value += widget.text

    def on_username_focus_qwe(self, widget):
        self.active_field_qwe = self.username_input_login_regis

    def on_password_focus_qwe(self, widget):
        self.active_field_qwe = self.password_input_login_regis

    def create_element_interface(self):
        self.start_button = toga.Button("GO?: ", on_press=self.login_scrin)
        self.scrin_button = toga.Button("Login in: ", on_press=self.main_screen)
        self.login_button = toga.Button("Registration: ", on_press=self.login_screen)
        self.back_button = toga.Button("← login_screen", on_press=self.login_scrin)
        self.back_two_button = toga.Button("← main_screen", on_press=self.main_screen)
        self.login_print_button = toga.Button("Login inQ: ", on_press=self.сheck_to_register)

        # Исправлено: padding заменен на margin
        self.username_label = toga.Label("Username:", style=Pack(margin=(10, 10)))
        self.username_input = toga.TextInput(style=Pack(flex=1))
        self.password_label = toga.Label("Password:", style=Pack(margin=(10, 10)))
        self.password_input = toga.PasswordInput(style=Pack(flex=1))

        self.backspace_button = toga.Button('⌫', on_press=self.backspace_pressed)
        self.backspace_button.style.update(width=25, height=25)

        self.backspace_button_qwe = toga.Button('⌫', on_press=self.backspace_pressed_qwe)
        self.backspace_button_qwe.style.update(width=25, height=25)

        self.username_input_login_regis = toga.TextInput(style=Pack(flex=1))
        self.username_label_login = toga.Label("Username:", style=Pack(margin=(10, 10)))
        self.password_label_login = toga.Label("Password:", style=Pack(margin=(10, 10)))
        self.password_input_login_regis = toga.PasswordInput(style=Pack(flex=1))
        self.log_button = toga.Button("Ok: ", on_press=self.qget_account)

        self.active_field = self.username_input
        self.active_field_qwe = self.username_input_login_regis

        self.username_input.on_gain_focus = self.on_username_focus
        self.password_input.on_gain_focus = self.on_password_focus
        self.username_input_login_regis.on_gain_focus = self.on_username_focus_qwe
        self.password_input_login_regis.on_gain_focus = self.on_password_focus_qwe

    def sqsl(self):
        self.cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Log ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        timestamp TEXT, 
        login TEXT, 
        password TEXT, 
        result TEXT 
        ) 
        ''')
        self.conn.commit()

    def account(self):
        self.cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS account ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        timestamp TEXT, 
        login TEXT, 
        password TEXT 
        ) 
        ''')
        self.conn.commit()

    def get_account(self, username):
        self.cursor.execute('SELECT login, password FROM account WHERE login=?', (username,))
        return self.cursor.fetchone()

    def qget_account(self, widget=None):
        try:
            self.cursor.execute(
                "INSERT INTO account (timestamp, login, password) VALUES (?, ?, ?)",
                (str(datetime.datetime.now()), self.username_input_login_regis.value,
                 self.password_input_login_regis.value)
            )
            self.conn.commit()
            print("Аккаунт зарегистрирован")
            # Исправленный вызов диалога
            self.main_window.info_dialog("Success", "Account registered successfully!")
        except Exception as e:
            print(f"Ошибка при регистрации: {e}")
            self.main_window.error_dialog("Error", f"Registration failed: {e}")

    def clear_main_box(self):
        while len(self.main_box.children) > 0:
            self.main_box.remove(self.main_box.children[0])

    def login_scrin(self, widget=None):
        self.clear_main_box()
        self.main_box.add(self.login_button)
        self.main_box.add(self.scrin_button)
        self.hide_keyboard()
        self.hide_keyboard_qwe()

    def main_screen(self, widget=None):
        self.clear_main_box()
        self.main_box.add(self.username_label)
        self.main_box.add(self.username_input)
        self.main_box.add(self.password_label)
        self.main_box.add(self.password_input)
        self.main_box.add(self.login_print_button)
        self.main_box.add(self.back_button)
        self.show_keyboard()

    def login_screen(self, widget=None):
        self.clear_main_box()
        self.main_box.add(self.username_label_login)
        self.main_box.add(self.username_input_login_regis)
        self.main_box.add(self.password_label_login)
        self.main_box.add(self.password_input_login_regis)
        self.main_box.add(self.log_button)
        self.main_box.add(self.back_two_button)
        self.show_keyboard_qwe()

    def сheck_to_register(self, widget=None):
        username = self.username_input.value
        password = self.password_input.value

        if not username:
            self.main_window.error_dialog("Error", "Please enter your login!")
            return

        if not password:
            self.main_window.error_dialog("Error", "Please enter your Password!")
            return

        acc_data = self.get_account(username)
        print("acc_data", acc_data)

        if not acc_data:
            self.result = "User not found"
        else:
            current_login, current_password = acc_data

            if username == current_login and password == current_password:
                self.result = "Nice"
            elif username == current_login and password != current_password:
                self.result = 'Invalid Password'
            elif username != current_login and password == current_password:
                self.result = 'Invalid Login'
            else:
                self.result = 'All Invalid Login'

        if self.result == "Nice":
            self.main_window.info_dialog("Hi there!", self.result)
        else:
            self.main_window.error_dialog("Error", self.result)

        timestamp = str(datetime.datetime.now())
        self.cursor.execute(
            "INSERT INTO Log (timestamp, login, password, result) VALUES (?, ?, ?, ?)",
            (timestamp, username, password, self.result)
        )
        self.conn.commit()


def main():
    return HelloWorld()


if __name__ == '__main__':
    app = main()
    app.main_loop()
