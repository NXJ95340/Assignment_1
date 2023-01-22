#creating an empty dog dictionary
dog = {}
#adding name, color, breed, legs and age to dog dictonary
dog = {"name":"lucy","color":"brown","breed":"dashshund","legs":4,"age":12}
print("Dog: ",dog)
#creating a student dictionary
student = {"first_name":"nikhil", "last_name":"jolapuram", "gender":"male", "age":"24",
           "marital status":"single", "skills":["HTML","java","python"], "country": "united states",
           "city":"overlandpark","address":"6605 W 141st St"}
print("Student: ",student)
#length of student dictonary:
length = len(student)
print("length of student dictonary: ",length)
#getting the values of skills and checking datatype
print("Student skills: ",student["skills"])
print("datatype of skills: ", type(student["skills"]))
#modifying skills by adding one more
student["skills"].append("DBMS")
print("skills: ", student["skills"])
#getting the dictionary keys as list
print("keys of student dictonary: ",list(student.keys()) )
#getting the dictionary values as list
print("values of student dictonary: ",list(student.values()) )