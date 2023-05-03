# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:29:45 2023

@author: GUILH
"""

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
number_of_months = 0


while current_savings < total_cost*portion_down_payment:
    current_savings = current_savings + monthly_salary*portion_saved + current_savings*r/12
    number_of_months = number_of_months + 1
print("The number of months is:", number_of_months)
    

