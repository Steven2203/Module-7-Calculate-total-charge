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
albertaCharge = orderTotal * .05
albertaCalc = orderTotal + albertaCharge
ontarioCharge = orderTotal * .13
ontarioCalc = orderTotal + ontarioCharge
provTax = orderTotal * .06 + orderTotal
provGst = provTax * .05 + orderTotal
combiTax = provTax + provGst

##I did the type casting in one line because of the concatenation issues.
##For better readability you can also do this on a separate line of code.
if userCountry == "Canada" and userProvince == "Alberta":
    print("You have to pay the following amount incl charges: " + str(albertaCalc))
if userCountry == "Canada" and userProvince == "Ontario":
    print("You have to pay the following amount incl charges: " + str(ontarioCalc))
elif userCountry == "Canada" and userProvince != "Alberta" or "Ontario":
    print("You have to pay the provincial / GST tax: " + str(combiTax))
else:
    if userCountry != "Canada":
        print("You do not need to pay taxes and are charged: " + str(orderTotal))

