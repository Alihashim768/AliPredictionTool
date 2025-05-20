from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from collections import Counter

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class PredictionApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.title_label = Label(text="ALI PREDICTION - PAKGAME TOOL", font_size=24, size_hint=(1, 0.2), color=(0,1,0,1))
        self.add_widget(self.title_label)

        self.instruction = Label(text="15 numbers (0-9) enter karo niche input boxes me:", size_hint=(1, 0.1), color=(1,1,1,1))
        self.add_widget(self.instruction)

        self.inputs = []
        input_layout = BoxLayout(size_hint=(1, 0.3))
        for i in range(15):
            ti = TextInput(multiline=False, input_filter='int', halign="center", font_size=20)
            self.inputs.append(ti)
            input_layout.add_widget(ti)
        self.add_widget(input_layout)

        self.predict_btn = Button(text="Predict Karo", size_hint=(1, 0.15), background_color=(0, 0.5, 0, 1))
        self.predict_btn.bind(on_press=self.do_prediction)
        self.add_widget(self.predict_btn)

        self.result_label = Label(text="", size_hint=(1, 0.25), color=(1,1,0,1), font_size=20)
        self.add_widget(self.result_label)

    def do_prediction(self, instance):
        try:
            numbers = [int(ti.text) for ti in self.inputs if ti.text.strip() != ""]
            if len(numbers) != 15:
                self.result_label.text = "[ERROR] 15 numbers bharain!"
                return
        except:
            self.result_label.text = "[ERROR] Sab inputs valid number hone chahiye!"
            return

        big = len([n for n in numbers if n >= 5])
        small = 15 - big
        red = len([n for n in numbers if n % 2 == 0])
        green = 15 - red

        bigsmall = "Big" if big > small else "Small"
        redgreen = "Red" if red > green else "Green"

        self.result_label.text = f"Prediction:\nBig/Small: {bigsmall}\nRed/Green: {redgreen}"

class AliPredictionApp(App):
    def build(self):
        return PredictionApp()

if __name__ == '__main__':
    AliPredictionApp().run()