# Poster Pricer
# By Reuben John B. Unicruz

import os

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

# Roll Width
rollWidth = 42

# Price per foot

paper_final = 5
paper_draft = 4

fabric      = 8

# Function Prototype(s)
def price_by_size(size, isFinal, isFabric): pass
        
# The Kivy Grid. Think of a table as an example.
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        # Poster width data entry
        self.add_widget(Label(text="Poster Width:", font_size=25))
        self.pwidth = TextInput(
            text = '0',
            font_size=25,
            multiline=False,
            halign='center',
            tab_width=0
        )
        self.add_widget(self.pwidth)

        # Poster height data entry
        self.add_widget(Label(text="Poster Height:", font_size=25))
        self.pheight = TextInput(
            text = '0',
            font_size=25,
            multiline=False,
            halign='center',
            tab_width=0
        )
        self.add_widget(self.pheight)

        # Poster Material entry
        self.add_widget(Label(text="Is the poster fabric?", font_size=25))
        self.is_fabric = CheckBox(active=False)
        self.add_widget(self.is_fabric)

        # Poster Quality Entry
        self.add_widget(Label(text="Is the poster final?", font_size=25))
        self.is_final = CheckBox(active=False)
        self.add_widget(self.is_final)

        # Poster Price
        self.calc_price = Button(text="Calculate Price!", font_size=25)
        self.add_widget(self.calc_price)
        self.calc_price.bind(on_press=self.get_price)

        self.price = 0

        self.final_price = Label(
            text=("Total Price: $%.2f")%(self.price),
            font_size = 25
        )
        
        self.add_widget(self.final_price)

    def get_price(self, event):
        self.price = price_by_size(
            [
                float(self.pwidth.text),
                float(self.pheight.text)
            ],
            self.is_final.active,
            self.is_fabric.active
        )

        self.final_price.text = ("Total Price: $%.2f")%(round(self.price, 2))


# The main app class using the defined
# Grid class defined above.
class PosterPriceApp(App):
    def build(self):
        return MyGrid()


# The bread and butter of this app.
# This takes the dimensions and the
# material of the poster to calculate
# price.
def price_by_size(size, isFinal, isFabric):
    maxSize = max(size)
    minSize = min(size)

    max_footage = round(maxSize / 12, 0)
    min_footage = round(minSize / 12, 0)

    if (not isFabric):
        if (maxSize > rollWidth):
            if (isFinal):
                return paper_final * max_footage
            else:
                return paper_draft * max_footage

        if (isFinal):
            return paper_final * min_footage

        return paper_draft * min_footage
    else:
        if (maxSize > rollWidth):
            return fabric * max_footage
        else:
            return fabric * min_footage

# Run the app.
if __name__ == "__main__":
    PosterPriceApp().run()
    quit()
