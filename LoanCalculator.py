from PyQt5.Qt import *
from PyQt5.uic import loadUi
import sys
import math


class LoanCalculator(QMainWindow):
    '''Loan Comparator - compares 2 mortgages, based on price salary, tax, interest rates, etc.'''

    def __init__(self):
        super().__init__()
        self.GUI()
        self.recalc()
        self.statusBar().showMessage('Ready')

    def GUI(self):
        loadUi('LoanCalculator.ui', self)
        self.spinCapital.valueChanged.connect(self.recalc)
        self.spinProportion.valueChanged.connect(self.recalc)
        self.spinInterest.valueChanged.connect(self.recalc)
        self.spinTerm.valueChanged.connect(self.recalc)
        self.spinCapital_2.valueChanged.connect(self.recalc)
        self.spinProportion_2.valueChanged.connect(self.recalc)
        self.spinInterest_2.valueChanged.connect(self.recalc)
        self.spinTerm_2.valueChanged.connect(self.recalc)
        self.spinSalary.valueChanged.connect(self.recalc)
        self.spinSalary_2.valueChanged.connect(self.recalc)
        self.spinTax.valueChanged.connect(self.recalc)
        self.spinTax_2.valueChanged.connect(self.recalc)
        self.show()

    def recalc(self):
        capital = self.spinCapital.value()
        proportion = self.spinProportion.value() / 100.0
        annual_interest = self.spinInterest.value() / 100.0
        term = self.spinTerm.value()
        salary = self.spinSalary.value()
        tax = self.spinTax.value()/100.0
        monthly_interest =(math.pow(annual_interest+1, 1/12)-1)
        monthly_interest = annual_interest / 12
        principal = capital * proportion
        factor = math.pow(1+monthly_interest, term * 12)
        repayment = principal * monthly_interest * factor
        repayment /= (factor - 1)
        nett_salary = salary*(1-tax)/12
        burden = repayment/nett_salary

        self.lblPrincipal.setText(self.price_format(principal))
        self.lblPayments.setText(self.price_format(repayment))
        self.lblBurden.setText(self.percent_format(burden))
        self.lblSalaryAfterTax.setText(self.price_format(nett_salary))

        capital2 = self.spinCapital_2.value()
        proportion2 = self.spinProportion_2.value() / 100.0
        annual_interest2 = self.spinInterest_2.value() / 100.0
        term2 = self.spinTerm_2.value()
        salary2 = self.spinSalary_2.value()/12
        tax2 = self.spinTax_2.value()/100.0
        monthly_interest2 =(math.pow(annual_interest2+1, 1/12)-1)
        monthly_interest2 = annual_interest2 / 12
        principal2 = capital2 * proportion2
        factor2 = math.pow(1+monthly_interest2, term2 * 12)
        repayment2 = principal2 * monthly_interest2 * factor2
        repayment2 /= (factor2 - 1)
        nett_salary2 = salary2*(1-tax2)
        burden2 = repayment2/nett_salary2

        self.lblPrincipal_2.setText(self.price_format(principal2))
        self.lblPayments_2.setText(self.price_format(repayment2))
        self.lblBurden_2.setText(self.percent_format(burden2))
        self.lblSalaryAfterTax_2.setText(self.price_format(nett_salary2))

        self.statusBar().showMessage('Recalculation complete', 200)

    def price_format(self, amount):
        '''format a decimal number as a dollar price

        param:amount:floating-point number to be reformatted
        returns:the number as a formatted string'''

        amount*=100
        amount=int(amount)/100.0
        return '$ {}'.format(amount)

    def percent_format(self, amount):
        '''format a decimal number as a percentage

        amount  floating-point number to be reformatted
        returns the number as a formatted string'''

        amount*=100
        amount=int(amount)
        return '{} %'.format(amount)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    calc = LoanCalculator()
    sys.exit(app.exec_())
