my_dict = {"name": "Ali", "age": 25, "city": "Samarkand"}

key_to_find = input("Kalit nomini kiriting: ")

if key_to_find in my_dict:
    print(my_dict[key_to_find])
else:
    print("Topilmadi")