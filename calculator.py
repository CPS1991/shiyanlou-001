#! /usr/bin/env python3

import sys

def social_insurance(salary):
    endowment = 0.08
    mediacare = 0.02
    unemployment = 0.005
    injury = 0.0
    maternity = 0.0
    provident = 6%
    return salary * (endowment + mediacare + unemployment + injury + maternity + provident)

def tax(salary):
    taxable = salary - social_insurance(salary) - 3500
    if taxable > 0
       if taxable > 80000:
           tax_rate = 0.45
           sskcs = 13505
       elif taxable > 55000:
           tax_rate = 0.35
           sskcs = 5505
       elif taxable > 35000:
           tax_rate = 0.3
           sskcs = 2755
       elif taxable > 9000:
           tax_rate = 0.25
           sskcs = 1005
       elif taxable > 4500:
           tax_rate = 0.2
           sskcs = 555
       elif taxable > 1500:
           tax_rate > 0.1
           sskcs = 105
       elif taxable >0:
           tax_rate = 0.03
           sskcs = 0
       return taxable * tax_rate - sskcs
    else:
        return 0

try:
    account = {}
    for arg in sys.argv[1:]:
        people_id = arg.split(':')[0]
        salary = int(arg.split(':')[1])
        account[people_id] = (salary - tax(salary) - social_insurance(salary))
    for key, value in account.items():
        print(key + ':' + '{:.2f}'. format(value))
except:
    print("Parameter Error")