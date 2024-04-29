from kivy.app import App
from kivy.uix.slider import Slider

class MinhaApp(App):
    def build(self):
         return Slider(min=50, max=150, value=70)
    
if __name__ == "__main__":
     MinhaApp().run()