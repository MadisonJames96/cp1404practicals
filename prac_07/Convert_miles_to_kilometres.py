from kivy.app import App
from kivy.lang import Builder

class ConvertingMilesToKilometresApp(App):
    def build(self):
        self.title = "Converting Miles to Kilometres"
        self.root = Builder.load_file('Convert_miles_to_kilometres.kv')

        return self.root

    def handle_calculate(self, value):
        result = value ** 2
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + increment)
        self.handle_calculate(int(self.root.ids.input_number.text))
        print(increment)


ConvertingMilesToKilometresApp().run()