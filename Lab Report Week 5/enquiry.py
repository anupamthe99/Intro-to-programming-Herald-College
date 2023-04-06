"""
Write a program to fill up a general ENQUIRY FORM ask user input (name, age,
qualification, contact number, address, email, interested area, description) at last ask them
about salary expectations if their salary expectations are higher than 20k (display
message, your work experience must be at least 2 years)
if the experience is 2 or more years display (you are shortlisted your enquiry has been
recorded, we will notify you, thank you!!)
if the experience is less than 2 years and salary expectation is less than 20k display (your
enquiry has been recorded, we will notify you, thank you!!)
"""

name=input("Enter you name :")
age=int(input("Enter you age :"))
qualification=input("Enter you qualification :")
contact_number=input("Enter you contact number :")
address=input("Enter you address :")
description=input("Enter you contact description :")
salary_expectation=input("Enter you salary expectation :")
if salary_expectation>=20000:
    print("you are shortlisted your enquiry has been recorded, we will notify you,thank you!!")
work_exp=input("Enter you contact work experience :")
if salary_expectation<20000 and work_exp<2:
    print("your enquiry has been recorded, we will notify you, thank you!!")




