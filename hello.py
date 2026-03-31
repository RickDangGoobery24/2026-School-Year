"""
taxformwithgui.py
Project 1 – Chapter 9 Programming Exercises
A GUI-based tax calculator program.
"""

from breezypythongui import EasyFrame

class TaxFormWithGUI(EasyFrame):
    """A GUI-based tax calculator."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator")

        # Gross income field
        self.addLabel(text = "Gross Income",
                      row = 0, column = 0,
                      sticky = "E")
        self.grossIncomeField = self.addFloatField(value = 0.0,
                                                   row = 0,
                                                   column = 1,
                                                   precision = 2)

        # Exemptions field
        self.addLabel(text = "Number of Exemptions",
                      row = 1, column = 0,
                      sticky = "E")
        self.exemptionsField = self.addIntegerField(value = 1,
                                                    row = 1,
                                                    column = 1)

        # Taxable income (output)
        self.addLabel(text = "Taxable Income",
                      row = 2, column = 0,
                      sticky = "E")
        self.taxableIncomeField = self.addFloatField(value = 0.0,
                                                     row = 2,
                                                     column = 1,
                                                     precision = 2,
                                                     state = "readonly")

        # Tax rate field
        self.addLabel(text = "Tax Rate (e.g. 0.20 for 20%)",
                      row = 3, column = 0,
                      sticky = "E")
        self.taxRateField = self.addFloatField(value = 0.20,
                                               row = 3,
                                               column = 1,
                                               precision = 2)

        # Tax due (output)
        self.addLabel(text = "Tax Due",
                      row = 4, column = 0,
                      sticky = "E")
        self.taxDueField = self.addFloatField(value = 0.0,
                                              row = 4,
                                              column = 1,
                                              precision = 2,
                                              state = "readonly")

        # Compute button spanning both columns
        self.addButton(text = "Compute",
                       row = 5, column = 0,
                       columnspan = 2,
                       command = self.compute)

    def compute(self):
        """Reads inputs, computes taxable income and tax due,
        and displays the results."""
        grossIncome  = self.grossIncomeField.getNumber()
        exemptions   = self.exemptionsField.getNumber()
        taxRate      = self.taxRateField.getNumber()

        # Each exemption is worth $3,000 deduction
        taxableIncome = max(0.0, grossIncome - exemptions * 3000.0)
        taxDue        = taxableIncome * taxRate

        self.taxableIncomeField.setNumber(taxableIncome)
        self.taxDueField.setNumber(taxDue)


def main():
    TaxFormWithGUI().mainloop()

main()
