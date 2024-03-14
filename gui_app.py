from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import math
import requests
from urllib.parse import quote
import json
import subprocess

class BoxLayoutMain(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "vertical" # Makes the layout vertical
        # Initialize Buttons
        # settings_button = Button(text="Settings", size=".8,.5")
        # stats_button = Button(text="stats_button")
        # title_bar = ""
        # self.add_widget(settings_button)
        # self.add_widget(stats_button)

class MainWidget(Widget):
    pass

class Quizzer(App):
    pass

Quizzer().run()