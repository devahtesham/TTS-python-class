# DICTIONARIES
# 1) add
# 2) del
# 3) update 
# 4) copy 
# 5) access
# CRUD OPERATION
# std_data = {
#     #key value pair
#     1:"Std One",
#     "name":"ali", 
#     "age":20,
#     "course":"Python programming"
# }
# print(std_data)
# ================ data access from dictionary
# print(std_data["name"])
# print(std_data[1])
# ==================== add & update data in dictionary
# std_data["fees"] = 2000  # add
# std_data["age"] = 30  # update
# print("old dictionary",std_data)
# # ==================== delete data in dictionary
# del std_data["course"]
# print("new distionary",std_data)
#   ==================== delete dictionary
# del std_data
# Methods in a dictionary
# print(len(std_data)) # length of a dictionary
# std_data.clear()
# print(std_data.values())
# print(std_data.keys())
# =======================
std_1 = {
    "std_id":1,
    "name":"ali", 
    "age":20,
    "course":"Python programming",
    "phone":"1234456",
    "fees":3000,
}
#

#============task==========

student=input("Enter your name: Ahtesham, Ali, Aqsa, Arqam, Ammar = \t")
student=student.capitalize()
ahtesham={
    "std_id":1,
    "name":"Ahtesham", 
    "age":20,
    "course":"Python programming",
    "phone":"1234456",
    "fees":3000,
}
ali={
    "std_id":2,
    "name":"Ali", 
    "age":25,
    "course":"Python programming",
    "phone":"1234456",
    "fees":3000,
}
aqsa={
    "std_id":3,
    "name":"aqsa", 
    "age":21,
    "course":"Python programming",
    "phone":"1234457",
    "fees":3000,
}
arqam={
    "std_id":4,
    "name":"arqam", 
    "age":22,
    "course":"Python programming",
    "phone":"1234458",
    "fees":3000,
}
ammar={
    "std_id":5,
    "name":"ammar", 
    "age":20,
    "course":"Python programming",
    "phone":"1234456",
    "fees":3000,
}
if student == "Ahtesham" or student == "ahtesham":
   for values in ahtesham :
    print(ahtesham[values])
elif student == "Ali":
   for values in ali :
    print(ali[values])
elif student == "Aqsa":
   for values in aqsa :
    print(aqsa[values]) 
elif student == "Arqam":
   for values in arqam :
    print(arqam[values]) 
elif student == "Ammar":
   for values in ammar :
    print(ammar[values])     
else:
    print("Invalid input")    

    


