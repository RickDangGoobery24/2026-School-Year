"""
temperatureconverter.py
Project 3 – Chapter 9 Programming Exercises
A GUI-based temperature converter between Fahrenheit and Celsius.

Layout (grid):
  Row 0: Labels  – "Fahrenheit"        | "Celsius"
  Row 1: Fields  – fahrenheitField     | celsiusField
  Row 2: Buttons – ">>>>" (F→C)        | "<<<<" (C→F)
"""

from breezypythongui import EasyFrame

class TemperatureConverter(EasyFrame):
    """Converts temperature values between Fahrenheit and Celsius."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Temperature Converter")

        # Row 0 – column labels
        self.addLabel(text = "Fahrenheit",
                      row = 0, column = 0,
                      sticky = "NSEW")
        self.addLabel(text = "Celsius",
                      row = 0, column = 1,
                      sticky = "NSEW")

        # Row 1 – input/output float fields
        self.fahrenheitField = self.addFloatField(value = 32.0,
                                                  row = 1,
                                                  column = 0,
                                                  precision = 2,
                                                  sticky = "NSEW")

        self.celsiusField = self.addFloatField(value = 0.0,
                                               row = 1,
                                               column = 1,
                                               precision = 2,
                                               sticky = "NSEW")

        # Row 2 – conversion buttons
        self.addButton(text = ">>>>",
                       row = 2, column = 0,
                       command = self.fahrenheitToCelsius)

        self.addButton(text = "<<<<",
                       row = 2, column = 1,
                       command = self.celsiusToFahrenheit)

    def fahrenheitToCelsius(self):
        """Reads the Fahrenheit field and outputs the Celsius equivalent."""
        fahrenheit = self.fahrenheitField.getNumber()
        celsius    = (fahrenheit - 32.0) * 5.0 / 9.0
        self.celsiusField.setNumber(celsius)

    def celsiusToFahrenheit(self):
        """Reads the Celsius field and outputs the Fahrenheit equivalent."""
        celsius    = self.celsiusField.getNumber()
        fahrenheit = celsius * 9.0 / 5.0 + 32.0
        self.fahrenheitField.setNumber(fahrenheit)


def main():
    TemperatureConverter().mainloop()

main()
