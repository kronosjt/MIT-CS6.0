# coding=utf-8
"""
Problem 1.
Write a function, called nestEggFixed, which takes four arguments: a salary, a
percentage of your salary to save in an investment account, an annual growth percentage
for the investment account, and a number of years to work. This function should return a
list, whose values are the size of your retirement account at the end of each year, with the
most recent year's value at the end of the list.
Complete the implementation of:
def nestEggFixed (salary, save, growthRate, years):

Retirement fund
End of year 1 F[0] = salary * save * 0.01
End of year 2 F[1] = F[0] * (1 + 0.01 * growthRate) + salary * save * 0.01
End of year 3 F[2] = F[1] * (1 + 0.01 * growthRate) + salary * save * 0.01
"""

#
# Problem 1
#
def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    savings = [] # List to save results
    savings.append(salary * save * 0.01)
    while len(savings) < years:
        for i in range(1, years):
            savings.append(savings[i-1] * (1 + 0.01 * growthRate) + salary * save * 0.01)
    return savings

def testNestEggFixed():
    savingsRecord = nestEggFixed(10000.0, 10, 15, 5)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    savingsRecord2 = nestEggFixed(999, 15, 9.9, 10)
    print savingsRecord2

    savingsRecord3 = nestEggFixed(10000, 5, 5, 1)
    print savingsRecord3

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
        year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
        account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """

    savings = [] # List to save results
    savings.append(salary * save * 0.01)
    while len(savings) < len(growthRates):
        for i in range(1, len(growthRates)):
            savings.append(savings[i - 1] * (1 + 0.01 * growthRates[i]) + salary * save * 0.01)
    return savings

def testNestEggVariable():
    salary = 10000
    save = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    savingsRecord2 = nestEggVariable(15000, 10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    print savingsRecord2