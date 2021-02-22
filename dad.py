from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

import random
Window.size = (500, 500)
class Mobilka(App):
    def my_press(self, instance):
        if self.txt.text == "123321":
            self.lab.text = "Пароль верен"
        else:
            self.lab.text = "Пароль не верен. Введите правильный пароль"
    def build(self):
        bl = BoxLayout(orientation="vertical", padding=[50, 150], spacing=30)
        
        self.lab = Label(text = "Введите пароль", color = (1,1,1,1))
        
        self.btn1 = Button(text = "Я кнопка-попрыгушка",
                      background_color = (0, 1, 0, 1))
        
        self.txt = TextInput()
        self.btn1.bind(on_press = self.my_press)
        bl.add_widget(self.lab)
        bl.add_widget(self.txt)
        bl.add_widget(self.btn1)
        
        return bl
if __name__ == "__main__":
    my = Mobilka()
    my.run()