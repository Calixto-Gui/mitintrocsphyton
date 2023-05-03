# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 10:42:30 2023

@author: GUILH
"""

annual_salary = float(input("Enter the starting salary:"))

total_cost = 1000000
semi_annual_raise = 0.07
down_payment = 0.25*total_cost
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
number_of_months = 0
x = 0 # counter to check semi-annual raise
low = 0
high = 10000
num_guesses = 0
guess = (high + low)/2
portion_saved = guess/10000

while abs(current_savings - down_payment) > 100 and num_guesses <= 10000 :
        
    current_savings = 0
    monthly_salary = annual_salary/12
    
    for number_of_months in range(36):
        current_savings = current_savings + monthly_salary*portion_saved + current_savings*r/12
        x = x + 1
        if x == 6:
            monthly_salary = monthly_salary*(1+semi_annual_raise)
            x = 0
    if current_savings < down_payment :
        low = guess
    else:
        high = guess
    
    num_guesses += 1
    guess = (high + low)/2
    portion_saved = guess/10000
    
    
       
if num_guesses >= 1000:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best saving rate:",portion_saved)
    print("Steps in bisection search:",num_guesses)


