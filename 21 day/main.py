# Python has the module called statistics and we can use this module to do all the statistical calculations. 
# However, to learn how to make function and reuse function let us try to develop a program, 
# which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). 
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. 
# You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

class Statistic:
    def __init__(self, ages):
        self.ages = ages

    def count(self):
        return len(self.ages)
    def sum(self):
        return sum(ages)
    def min(self):
        return min(ages)
    def max(self):
        return max(ages)
    def range(self):
        return max(ages) - min(ages)
    def mean(self):
        return sum(self.ages) // len(self.ages)
    def median(self):
        return sorted(self.ages)[len(self.ages) // 2]
      
      
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistic(ages)

print(data.count())
print(data.sum())
print(data.min())
print(data.max())
print(data.range())
print(data.mean())
print(data.median())

# Create a class called PersonAccount. 
# It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
# Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses_properties):
       self.firstname = firstname
       self.lastname = lastname
       self.incomes = incomes
       self.expenses_properties = expenses_properties

    def total_income(self):
        return f"Incomes: {self.incomes}"
    def total_expense(self):
        return f"Expense: {self.expenses_properties}"
    def account_info(self):
        return f'Name: {self.firstname} {self.lastname}, incomes: {self.incomes}, expense: {self.expenses_properties}'
    def add_income(self, inc):
        self.incomes = self.incomes + inc
    def add_expense(self, expenses):
        self.expenses_properties = self.expenses_properties + expenses
    def account_balance(self):
        return f"Balance: {self.incomes - self.expenses_properties}"

person = PersonAccount("Nikita", "Radonov", 10, 5)

print(person.total_income())
print(person.total_expense())
print(person.account_info())
person.add_income(10)
print(person.total_income())
person.add_expense(5)
print(person.total_expense())
print(person.account_balance())
