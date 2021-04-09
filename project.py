# Pyroll calculator project 
n = 1
while n < 5:

    print("Welcome to the payroll calculator!")
    #Employee Name
    employee = input("Employee Name: ")
    # Hours Worked 
    hours_worked = float(input("Hour Worked: "))
    extra_hours_worked = float(input("Extra Hour Worked: "))
    # Payment Rates 
    pay_rate = float(input("Pay Rate $: ")) 
    extra_hours_rate = 1.5 * pay_rate
    #Payements
    reg_pay = hours_worked * pay_rate  
    ext_pay = extra_hours_worked * extra_hours_rate
    gross_pay = reg_pay + ext_pay
    # Tax Rates
    fed_tax_rate = 0.10
    state_rate = 0.03
    fica_rate = 0.07

    #Total tax
    fed_tax = round(pay_rate * fed_tax_rate, 2)
    state_tax = round(pay_rate * state_rate, 2) 
    fica_tax = round(pay_rate * fica_rate, 2)
    total_tax = round(fed_tax + state_tax + fica_tax, 2)
    net_pay = round(gross_pay - total_tax, 2)

    print(f"Your gross payment is {gross_pay} dollars.")
    print(f"Your Total Federal tax is {pay_rate * fed_tax_rate} dollar.")
    print(f"Your State tax is {pay_rate * state_rate} dollar.")
    print(f"Your FICA payment is {fica_tax} dollar.")
    # print(f"Your FICA payment is {pay_rate * fica_rate} dollar.")
    print(f"Your total tax payed is {total_tax} dollar.")
    print(f"Your net payment is {net_pay} dollar.")
    print(f"Thank you dear {employee}!") 

    n += 1
