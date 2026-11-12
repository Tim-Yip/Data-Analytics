name = "Jefferson Wang"
address = "123 Main St"
city = "Anytown"
state = "CA"
zip = "12345"
contact_info = {
    "name": "Jefferson Wang",
    "address": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
}

print(f"{contact_info['name']}\n{contact_info['address']}\n{contact_info['city']}, \
{contact_info['state']} {contact_info['zip']}")

contact_info.pop("name")

full_name = {
    "first_name": "Jefferson",
    "last_name": "Wang"
}

full_name.update({"honorific": "Mr."})

contact_info.update({"full_name": full_name})

print(f"""{contact_info['full_name']['honorific']} {contact_info['full_name']['first_name']} {contact_info['full_name']['last_name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")