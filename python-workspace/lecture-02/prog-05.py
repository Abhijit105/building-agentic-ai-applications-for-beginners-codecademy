list_1 = [10, 20, 30, 40, 50]

for num in list_1:
    print(num)

str_1 = "Abhijit Kumar"
for char in str_1:
    print(char)

dict_1 = {
    "name": "Abhijit Kumar",
    "age": 35,
    "company": "Appbrew",
    "isMarried": False,
    "skills": ["HTML", "CSS", "Javascript"]
}

for key, value in dict_1.items():
    print(f"{key}: {value}")

print(dict_1)
print(dict_1.items())
print(dict_1.keys())
print(dict_1.values())
