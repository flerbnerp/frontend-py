import os
import requests
from urllib.parse import quote

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

class QuestionInterface(Widget):
    def __init__(self, **kwargs):
        super(QuestionInterface, self).__init__(**kwargs)
        
class Quizzer(App):
    def build(self):
        return QuestionInterface()

if __name__ == '__main__':
    Quizzer().run()

      





# class LoginScreen(GridLayout):
#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)


