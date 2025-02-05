import sqlite3 
import datetime 
import toga 
from toga.style import Pack 
from toga.style.pack import COLUMN, ROW 
 
 
class HelloWorld(toga.App): 
    def startup(self, widget=None): 
        self.create_element_interface() 
        self.conn = sqlite3.connect('C://Users//Maksz//beeware-tutorial//database.db')  # таблицыC:\Users\PC-4\beeware-tutorial\database.db 
        self.cursor = self.conn.cursor() 
        self.sqsl() 
        self.account() 
        self.main_box = toga.Box()  # окна 
        self.main_window = toga.MainWindow(title=self.formal_name) 
        self.top_container = toga.Box(style=Pack(direction=COLUMN, padding=20, width=70, height=28)) 
 
 
        self.keyboard_container = toga.Box(style=Pack(direction=COLUMN, padding=(150, 1))) 
        self.keyboard_container_qwe = toga.Box(style=Pack(direction=COLUMN, padding=(150, 1))) 
        self.generate_keyboard() 
        self.generate_keyboard_qwe() 
        self.main_window.content = self.main_box 
        self.main_window.show() 
        self.main_box.add(self.start_button) 
        self.username_input.on_gain_focus = self.on_username_focus 
        self.password_input.on_gain_focus = self.on_password_focus 
 
        self.username_input_login_regis.on_gain_focus = self.on_username_focus_qwe 
        self.password_input_login_regis.on_gain_focus = self.on_password_focus_qwe 
        # Устанавливаем начальное активное поле 
        self.active_field = self.username_input 
        self.active_field_qwe = self.username_input 
 
    def show_keyboard(self): 
        self.main_box.add(self.keyboard_container) 
    def show_keyboard_qwe(self): 
        self.main_box.add(self.keyboard_container_qwe) 
 
    def hide_keyboard(self): 
        if self.keyboard_container in self.main_box.children: 
            self.main_box.remove(self.keyboard_container) 
    def hide_keyboard(self): 
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
                    style=Pack(width=25, height=25,) 
                ) 
                row_box.add(button) 
            self.keyboard_container.add(row_box) 
 
    def backspace_pressed(self, widget): 
        if self.active_field.value: 
            self.active_field.value = self.active_field.value[:-1] 
 
    def button_pressed(self, widget=None): 
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
                    style=Pack(width=25, height=25,) 
                ) 
                row_box.add(button) 
            self.keyboard_container_qwe.add(row_box) 
    def backspace_pressed_qwe(self, widget): 
        if self.active_field_qwe.value: 
            self.active_field_qwe.value = self.active_field_qwe.value[:-1] 
 
    def button_pressed_qwe(self, widget=None):
        self.active_field_qwe.value += widget.text 
 
    def on_username_focus_qwe(self, widget): 
        self.active_field_qwe = self.username_input_login_regis 
 
    def on_password_focus_qwe(self, widget): 
        self.active_field_qwe = self.password_input_login_regis 
 
 
    def create_element_interface(self): 
        self.start_button = toga.Button("GO?: ", on_press=self.login_scrin)  # startup 
        self.scrin_button = toga.Button("Login in: ", on_press=self.main_screen)  # login_scrin 
        self.login_button = toga.Button("Registration: ", on_press=self.login_screen)  # login_scrin 
        self.back_button = toga.Button("← login_screen", on_press=self.login_scrin)  # main_screen 
        self.back_two_button = toga.Button("← main_screen", on_press=self.main_screen) 
        self.login_print_button = toga.Button("Login inQ: ", on_press=self.сheck_to_register)  # main_screen 
        self.username_label = toga.Label("Username:", style=Pack(padding=(10, 10), flex=1, )) 
        self.username_input = toga.TextInput(readonly=True, style=Pack(flex=1, )) 
        self.password_label = toga.Label("Password:", style=Pack(padding=(10, 10), flex=1)) 
        self.password_input = toga.PasswordInput(readonly=True, style=Pack(flex=1)) 
        self.backspace_button = toga.Button('⌫', on_press=self.backspace_pressed) 
        self.backspace_button.style.update(width=25, height=25) 
        self.timestamp = str(datetime.datetime.now()) 
        self.login = self.username_input.value 
        self.password = self.password_input.value 
        self.result = '' 
        self.username_input_login_regis = toga.TextInput(readonly=True, style=Pack(flex=1, )) 
        self.username_label_login = toga.Label("Username:", style=Pack(padding=(10, 10), flex=1, )) 
        self.password_label_login = toga.Label("Password:", style=Pack(padding=(10, 10), flex=1)) 
        self.password_input_login_regis = toga.PasswordInput(readonly=True, style=Pack(flex=1)) 
        self.log_button = toga.Button("Ok: ", on_press=self.qget_account) 
         
  
         
 
 
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
        id INTEGER PRIMARY KEY, 
        id_log INTEGER, 
        timestamp TEXT, 
        login TEXT, 
        password TEXT, 
        FOREIGN KEY (id_log) REFERENCES Log (id) 
        ) 
        ''') 
        self.conn.commit() 
     
    def get_account(self): 
        print(self.username_input) 
        data = self.cursor.execute(f''' 
                                   SELECT login, password FROM account  
                                   WHERE login="{self.username_input.value}" 
                                    ''') 
        return data 
     
    def qget_account(self,widget=None): 
        self.cursor.execute( 
            "INSERT INTO account (login, password) VALUES (?, ?)", 
            (self.username_input_login_regis.value, self.password_input_login_regis.value) 
        ) 
        self.conn.commit() 
 
 
    def login_scrin(self, widget=None): 
        self.main_box.remove(self.start_button) 
        self.main_box.add(self.login_button) 
        self.main_box.add(self.scrin_button) 
        if self.back_button in self.main_box.children: 
            self.main_box.remove(self.back_button) 
 
        if self.login_print_button in self.top_container.children: 
            self.top_container.remove(self.login_print_button) 
 
        if self.username_input in self.top_container.children: 
            self.top_container.remove(self.username_input) 
 
        if self.username_label in self.top_container.children: 
            self.top_container.remove(self.username_label) 
 
        if self.password_input in self.top_container.children: 
            self.top_container.remove(self.password_input) 
        
        if self.password_label in self.top_container.children: 
            self.top_container.remove(self.password_label) 
        self.main_box.remove(self.username_input_login_regis) 
        self.main_box.remove(self.username_label_login) 
        self.main_box.remove(self.password_input_login_regis) 
        self.main_box.remove(self.password_label_login) 
        self.main_box.remove(self.log_button) 
        self.main_box.remove(self.keyboard_container) 
 
        self.hide_keyboard() 
 
    def main_screen(self, widget=None): 
        self.top_container.add(self.username_input) 
        self.top_container.add(self.username_label) 
        self.top_container.add(self.password_input) 
        self.top_container.add(self.password_label) 
        self.top_container.add(self.login_print_button) 
        self.main_box.add(self.top_container) 
        self.keyboard_container.add(self.backspace_button) 
        self.show_keyboard() 
        self.main_box.add(self.back_button) 
        self.main_box.remove(self.login_button) 
        self.main_box.remove(self.scrin_button) 
 
    def login_screen(self, widget=None): 
        self.main_box.add(self.username_input_login_regis) 
        self.main_box.add(self.username_label_login) 
        self.main_box.add(self.password_input_login_regis) 
        self.main_box.add(self.password_label_login) 
        self.main_box.add(self.back_button) 
        self.main_box.add(self.log_button) 
        self.show_keyboard_qwe() 
        self.main_box.remove(self.scrin_button) 
        self.main_box.remove(self.login_button) 
         
 
    def сheck_to_register(self, widget=None): 
        acc_data = self.get_account().fetchone() 
        print("acc_data", acc_data) 
         
         
 
        current_login = acc_data[0] 
        current_password = acc_data[1] 
         
        print(f"Login: {self.login}, Password: {self.password}") 
        print(f"Login: {self.username_input_login_regis.value}, Password: {self.password_input_login_regis.value}") 
        login = self.username_input.value.lower() 
        if not login: 
            # Ошибка, если логин пустой 
            dialog = toga.InfoDialog(title="Error", message="Please enter your login!") 
            dialog._show(self.main_window) 
            return  
         
        password = self.password_input.value.lower() 
        if not password: 
            # Ошибка, если логин пустой 
            dialog_2 = toga.InfoDialog(title="Error", message="Please enter your Passsword!") 
            dialog_2._show(self.main_window) 
            return  
 
        current_login = current_login.lower() 
        current_password = current_password.lower() 
 
        if login == current_login and password == current_password: 
            self.result = "Nice" 
        elif login == current_login and password != current_password: 
            self.result = 'Invalid Password' 
        elif login != current_login and password == current_password: 
            self.result = 'Invalid Login' 
        else: 
            self.result = 'All Invalid Login' 
             
        if self.result == "Nice": 
            dialog = toga.InfoDialog(title="Hi there!", message=self.result) 
        else: 
            dialog = toga.InfoDialog(title="Sueta", message=self.result) 
        dialog._show(self.main_window) 
 
        print("1",self.timestamp, self.username_input.value, self.password_input.value, self.result) 
         
 
        #         CREATE TABLE IF NOT EXISTS Log ( 
        # id INTEGER PRIMARY KEY AUTOINCREMENT, 
        # timestamp TEXT, 
        # login TEXT, 
        # password TEXT, 
        # result TEXT 
        # ) 
        self.cursor.execute( 
            "INSERT INTO Log (timestamp, login, password, result) VALUES (?, ?, ?, ?)", 
            (self.timestamp, self.username_input.value, self.password_input.value, self.result) 
        ) 
 
        self.conn.commit() 
    # def login_sql: 
 
 
 
 
 
         
 
def main(): 
    return HelloWorld(formal_name='Hello World')