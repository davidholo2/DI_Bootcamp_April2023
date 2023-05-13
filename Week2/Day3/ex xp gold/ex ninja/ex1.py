# Original list of manufacturers/companies
companies_str = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Convert to list
companies_list = companies_str.split(", ")

# Print how many companies there are
print(f"There are {len(companies_list)} manufacturers/companies in the list.")

# Print the list in reverse/descending order
print("The list of manufacturers/companies in reverse order is:")
for company in reversed(companies_list):
    print(company)

# Find the number of companies with the letter 'o'
num_with_o = sum(1 for company in companies_list if 'o' in company)
print(f"There are {num_with_o} manufacturers/companies with the letter 'o' in their name.")

# Find the number of companies without the letter 'i'
num_without_i = sum(1 for company in companies_list if 'i' not in company)
print(f"There are {num_without_i} manufacturers/companies without the letter 'i' in their name.")

# Remove duplicates using set
companies_set = set(companies_list)
companies_list = list(companies_set)

# Print the list of unique companies in a comma-separated string with no line-breaks
print(f"The companies without duplicates are: {', '.join(companies_list)}")
print(f"There are now {len(companies_list)} companies in the list.")

# Print the list of manufacturers in ascending order (A-Z) with reversed letters
print("The list of manufacturers/companies in ascending order (A-Z) with reversed letters is:")
for company in sorted(companies_list):
    print(company[::-1])
