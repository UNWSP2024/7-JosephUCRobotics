# Author: Joseph Kracht
# Last Modified: 10/11/2025
# Title: US_Population

# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:

    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    # git list of tuples of information
    all_entered_values = []
    while True:
        try:
            year = int(input("Enter a year or enter q to exit: "))
        except:
            break
        name = input("Enter a city name: ")
        population = int(input("Enter a population: "))
        all_entered_values.append((year, name, population))


    # Now have the user enter a year.
    year_to_sum = int(input("Enter a year to get the population: "))

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    sum_population_for_year(all_entered_values, year_to_sum)


def sum_population_for_year(all_entered_values, year_to_sum):

# Loop through and sum the populations for the appropriate year.
# e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
# or 3,421,988 if they enterd 2011 for the year to sum.
    total_population = 0
    for tuple_item in all_entered_values:
        if tuple_item[0] == year_to_sum:
            total_population += tuple_item[2]


# print the totalled population
    print("The total population in", year_to_sum, "is", total_population)


# Call the main function.
if __name__ == '__main__':
    main()
