# Author: Joseph Kracht
# Last Modified: 10/10/2025
# Title: Rainfall

# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, # and the months with the highest and lowest amounts.

# get list of monthly rain amounts
months_rainfall = []
for i in range(12):
    current_months_rain = float(input("Input the total rain for month " + str(i+1) + ": "))
    months_rainfall.append(current_months_rain)

# find the months with the most rain
max_months = ""
for i, value in enumerate(months_rainfall):
    if value == max(months_rainfall):
        if max_months != "":
            max_months+=" and month "
        max_months+=str(i+1)

# find the months with the least rain
min_months = ""
for i, value in enumerate(months_rainfall):
    if value == min(months_rainfall):
        if min_months != "":
            min_months+=" and month "
        min_months+=str(i+1)

# display everything
print("The total rain fall for the year is", sum(months_rainfall))
print("The average monthly rain fall is", format(sum(months_rainfall)/12, '.2f'))
print("The most it rained in one month was", max(months_rainfall), "this was in month", max_months)
print("The least it rained in one month was", min(months_rainfall), "this was in month", min_months)
