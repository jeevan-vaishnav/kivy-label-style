from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


# Design our kv design file
Builder.load_file('inherit.kv')


# Creating Lagout Class
class MyLayout(Widget):
    pass

# Creating main class as name is Awesome


class AwesomeApp(App):
    def build(self):
        return MyLayout()


# Main method
if __name__ == "__main__":
    AwesomeApp().run()
