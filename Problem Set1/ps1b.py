# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:03:03 2023

@author: GUILH
"""

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual-raise, as decimal:"))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
number_of_months = 0
x = 0 # counter to check semi-annual raise


while current_savings < total_cost*portion_down_payment:
    current_savings = current_savings + monthly_salary*portion_saved + current_savings*r/12
    number_of_months = number_of_months + 1
    x = x + 1
    if x == 6:
        monthly_salary = monthly_salary*(1+semi_annual_raise)
        x = 0
    
print("The number of months is:", number_of_months)