#boolean data type
# true / false

print(True)
print(False)

''' Dictionary . key values
               . unorderd
               . mutable
               . key has to be usique
               . heterogenious data   '''

students_details = {'name':'Aashi', 'age':21, 'city':'Jabalpur'}
print(students_details)
print(type(students_details))

dict1 = {1:"Aashi", 2:"Mohan", True:"love"} # True=1
print(dict1)

#Dictionary constructor mathod
dict1 = dict( age="Mohan", name="aashi",city="jabalpur")


students_details = {'name':'Aashi', 'age':21, 'city':'Jabalpur'}
print(students_details['city'])
print(students_details.keys())
print(students_details.values())
print(students_details.items())

students_details = {'name':'Aashi', 'age':21, 'city':'Jabalpur'}
students_details['country'] = "india"
print(students_details)


students_details = {'name':'Aashi', 'age':21, 'city':'Jabalpur'}
marks_details = {'marks':33}
students_details.update(marks_details)
print(students_details)


#Remove the element From disctionary

print(students_details.pop('city'))
print(students_details.popitem())

del students_details['age']
print(students_details)

print(students_details.clear())


