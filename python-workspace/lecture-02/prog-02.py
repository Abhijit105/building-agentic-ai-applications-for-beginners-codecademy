list_1 = [
    "Abhi", 
    35, 
    {
        "cn": "India", 
        "city": "Bangalore"
    }, 
    "Appbrew", 
    False,
    ["HTML", "CSS", "Javascript"]
]

print(type(list_1))
print(type(list_1[0]))
print(type(list_1[1]))
print(type(list_1[2]))
print(type(list_1[3]))

print(len(list_1))
print(len(list_1[5]))

tup_1 = (
    "Abhi",
    35,
    "Appbrew"
)

tup_2 = "Abhi", 35, "Appbrew"

print(type(tup_1))
print(type(tup_2))

set_1 = {1, 2, 3, 4, 2, 3, 4, 1}
print(set_1)
print(type(set_1))

list_2 = [1, 2, 3, 4]
print(list_1 + list_2)
print(list_1 + list_2)
print(type(list_1 + list_2))

list_3 = [5, 6]
list_2.extend(list_3)
print(list_2)

list_2.append(list_3)
print(list_2)

dict_1 = {
    "name": "Abhijit Kumar",
    "age": 35,
    "job": "Appbrew",
    "is_married": False,
    "skills": ["HTML", "CSS", "Javascript"]
}
print(dict_1)
print(type(dict_1))
print(len(dict_1))
del dict_1["age"]
print(dict_1)
dict_1["skills"].append("React")
print(dict_1)
dict_1["skills"].extend(["NodeJS"])
print(dict_1)
