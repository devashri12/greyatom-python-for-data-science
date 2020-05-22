# --------------
# Code starts here
class_1=['Geoffrey','Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

# Create the lists 
new_class= class_1+class_2
print (new_class)
# Concatenate both the strings
new_class.append('Peter Warden')
print (new_class)

# Append the list

# Print updated list
new_class.remove('Carla Gentry')
print (new_class)
# Remove the element from the list

# Print the list
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}

# Create the Dictionary
a=courses['Math']
print (a)
b=courses['English']
print(b)
c=courses['History']
print(c)
d=courses['French']
print(d)
e=courses['Science']
print(e)
# Slice the dict and stores  the all subjects marks in variable
s=courses.values()
Total=sum(s)

# Store the all the subject in one variable `Total`
print (Total)
# Print the total
percentage=(Total/500)*100
# Insert percentage formula
print (percentage)
# Print the percentage
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':60,'Peter Warden':75}
topper=max(mathematics,key= mathematics.get)
print (topper)



# Create the Dictionary
 



# Given string
first_name,last_name=topper.split()
#print(name)
#first_name=name[0]
print(first_name)
# Create variable first_name 
#last_name=name[1]
print(last_name)
# Create variable Last_name and store last two element in the list
full_name=last_name+" " +first_name
print(full_name)
# Concatenate the string

# print the full_name
certificate_name=full_name.upper()
print(certificate_name)
# print the name in upper case

# Code ends here


