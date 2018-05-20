#! /usr/bin/env python3

import sys

for arg in sys.argv[1:]:
    try:
        tax_money = int(sys.argv[1]) - 3500
        if tax_money <= 0:
            tax_pay = 0
        elif tax_money <= 1500:
            tax_pay = tax_money*0.03
        elif tax_money <= 4500:
            tax_pay = tax_money*0.10 - 105
        elif tax_money <= 9000:
            tax_pay = tax_money*0.20 - 555
        elif tax_money <= 35000:
            tax_pay = tax_money*0.25 - 1005
        elif tax_money <= 55000:
            tax_pay = tax_money*0.30 - 2755
        elif tax_money <= 80000:
            tax_pay = tax_money*0.35 - 5505
        else:
            tax_pay = tax_money*0.45 - 13505
        print(format(tax_pay,".2f"))
    except:
        print("Parameter Error")
        
