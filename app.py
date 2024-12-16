class HelloWorld(toga.App):
    def startup(self):
        # Подключаемся к базе данных SQLite
        self.conn = sqlite3.connect('C://Users//Maksz//beeware-tutorial//database.db')  # создаем/открываем базу данных  # создаем/открываем базу данных
        self.cursor = self.conn.cursor()  # создаем курсор для выполнения запросов
        # Создаем таблицы, если их еще нет
        # Подключение к базе данных SQLite
        self.conn = sqlite3.connect('C:/Users/Maksz/beeware-tutorial/database.db')
        self.cursor = self.conn.cursor()
        
        # Создание таблиц, если их ещё нет
        self.create_tables()

        # Остальная часть кода остается без изменений...
        # Создаем основной контейнер
        # Основной контейнер
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Верхний контейнер для полей ввода и кнопки Say Hello!
        # Контейнер для полей ввода и кнопки
        top_container = toga.Box(style=Pack(direction=COLUMN, padding=25))

        # Добавляем метку и текстовое поле для ввода имени
        name_label = toga.Label("Login:", style=Pack(padding=(5, 5)))
        self.name_input = toga.TextInput(readonly=True, style=Pack(flex=1))
        pasword_label = toga.Label("Pasword:", style=Pack(padding=(-5, -0)))
        self.pasword_input = toga.TextInput(readonly=True, style=Pack(flex=1))  # Поле только для чтения
        # Метка и текстовое поле для ввода логина
        username_label = toga.Label("Username:", style=Pack(padding=(5, 5)))
        self.username_input = toga.TextInput(readonly=True, style=Pack(flex=1))
        # Метка и текстовое поле для ввода пароля
        password_label = toga.Label("Password:", style=Pack(padding=(5, 5)))
        self.password_input = toga.PasswordInput(readonly=True, style=Pack(flex=1))

        # Горизонтальный бокс для размещения метки и поля ввода
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        pasword_box = toga.Box(style=Pack(direction=ROW, padding=5))
        pasword_box.add( pasword_label)
        pasword_box.add( self.pasword_input)
        # Горизонтальные боксы для размещения меток и полей ввода
        username_box = toga.Box(style=Pack(direction=ROW, padding=5))
        username_box.add(username_label)
        username_box.add(self.username_input)

        # Кнопка для вывода приветствия
        hello_button = toga.Button(
            "go", on_press=self.say_hello, style=Pack(padding=50)
        password_box = toga.Box(style=Pack(direction=ROW, padding=5))
        password_box.add(password_label)
        password_box.add(self.password_input)
        # Кнопка для отправки формы
        submit_button = toga.Button(
            "Submit", on_press=self.submit_form, style=Pack(padding=50)
        )

        # Добавляем элементы в верхний контейнер
        top_container.add(name_box)
        top_container.add(hello_button)
        top_container.add(pasword_box)
        top_container.add(username_box)
        top_container.add(password_box)
        top_container.add(submit_button)

        # Нижний контейнер для кнопок-клавиатуры
        keyboard_container = toga.Box(style=Pack(direction=COLUMN, padding=10))
@@ -79,6 +81,23 @@ def startup(self):
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
    def create_tables(self):
        # Создаем таблицу logs, если ее еще нет
        self.cursor.execute('''
@@ -101,46 +120,49 @@ def log_entry(self, input_text, result):
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

            # Логируем запись
            self.log_entry(name, greeting)
            self.log_entry(login, greeting)

            # Выводим сообщение
            dialog = toga.InfoDialog(title="Hi there!", message=greeting)
            dialog._show(self.main_window)
        else:
            # Ошибка, если имя пустое
            dialog = toga.InfoDialog(title="Error", message="Please enter your name!")
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
@@ -149,4 +171,5 @@ def main():
# Запускаем приложение
if __name__ == '__main__':
    app = main()
    app.activate_fields()  # Активируем отслеживание фокуса
    app.main_loop()