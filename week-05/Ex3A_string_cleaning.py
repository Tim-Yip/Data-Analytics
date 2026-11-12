name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

name_1_lower = name_1.lower()
name_2_lower = name_2.lower()
name_3_lower = name_3.lower()

name_1_cleaned = name_1_lower.title()
name_2_cleaned = name_2_lower.title()
name_3_cleaned = name_3_lower.title()

print(name_1_cleaned)
print(name_2_cleaned)
print(name_3_cleaned)

salary_1_cleaned = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_cleaned, type(salary_1_cleaned)) 