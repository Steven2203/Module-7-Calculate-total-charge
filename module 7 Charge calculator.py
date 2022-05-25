#-------------------------------------------------------------------------------
# Name:        module 7 - Calculate the total to charge
# Purpose:     Learn complex decision making with code.
# Author:      Steven
# Created:     25-05-2022
# Copyright:   (c) Steven 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##Asking the user questions to define if they need to pay taxes.

userCountry = input ("In what country do you live? ")
userProvince = input ("In what province do you live?")
orderTotal = input ("Enter your total order amount: ")

##Defining the TAX values inside variables for calculations.
orderTotal = float(orderTotal)
albertaCharge = orderTotal * 100.05
ontarioCharge = orderTotal * 100.13
provTax = orderTotal * 100.06
provGst = provTax * 100.05

if userCountry == "Canada" and userProvince == "Alberta":
    print("You have to pay the following amount incl charges: " + str(albertaCharge))
if userCountry == "Canada" and userProvince == "Ontario":
    print("You have to pay the following amount incl charges: " + str(ontarioCharge))
if userCountry == "Canada" and userProvince != "Alberta" or "Ontario":
    print("You have to pay the provincial / GST tax: " + str(provTax) + str(provGst))
else:
    if userCountry != "Canada":
        print("You do not need to pay taxes and are charged: " + str(orderTotal))