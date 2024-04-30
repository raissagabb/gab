from kivy.app import App
from kivy.uix.togglebutton import ToggleButton

class MinhaApp(App):
    def build(build):
        return ToggleButton(text='Ligado', state='normal')
    
if __name__ == "__main__":
    MinhaApp().run()