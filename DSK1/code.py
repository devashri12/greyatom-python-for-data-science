# --------------
#Code starts here
def read_file(path):
#Function to read file
    file=open(path,mode='r')
    #Opening of the file located in the path in 'read' mode
    sentence=file.read()
        #Reading of the first line of the file and storing it in a variable
    file.close()
    #Closing of the file
    return(sentence)
    #Returning the first line of the file
sample_message=read_file(file_path)
print(sample_message)


message_1=read_file(file_path_1)  
message_2=read_file(file_path_2)  

#Calling the function to read file

print(message_1)
print(message_2)
#Printing the line of the file


#Function to fuse message
def fuse_msg(message_a,message_b):
    a=int(message_a)
    b=int(message_b)
    quotient=b//a
    #Integer division of two numbers
    
    return((quotient))
    #Returning the quotient in string format

secret_msg_1=fuse_msg(message_1,message_2)
#Calling the function to read file  

#Calling the function 'fuse_msg'

print(secret_msg_1)
#Printing the secret message 

message_3=read_file(file_path_3)
print(message_3)

#Function to substitute the message
def substitute_msg(message_c):
    if (message_c=='Red'):
        sub='Army General'
    elif (message_c=='Green'):
            sub='Data Scientist'
    else:
            sub='Marine Biologist'
    return(sub)
    
    #If-else to compare the contents of the file
    
    
    #Returning the substitute of the message
secret_msg_2=substitute_msg(message_3)    
  

#Calling the function to read file


#Calling the function 'substitute_msg'
print(secret_msg_2)

#Printing the secret message
message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
print(message_4)
print(message_5)

#Function to compare message
def compare_msg(message_d,message_e):
    a_list=[]
    b_list=[]
    c_list=[]

    a_list=message_d.split()
    print(a_list)
        #Splitting the message into a list
    b_list=message_e.split()
    print(b_list)
        #Splitting the message into a list
    #c_list=set(a_list)-set(b_list)
    for a in b_list:
        for b in a_list:
            if a == b :
                a_list.remove(b)
    
            
    #print("Final List Size: ", len(a_list))
    print(a_list)
    #  print(c_list)
    #Comparing the elements from both the lists
    final_msg=" ".join(a_list)
    
    #Combining the words of a list back to a single string sentence
    return(final_msg)
    
    #Returning the sentence

    

#Calling the function to read file


#Calling the function to read file
secret_msg_3= compare_msg(message_4,message_5)


#Calling the function 'compare messages'
print(secret_msg_3)

#Printing the secret message

message_6=read_file(file_path_6)
print(message_6)
#Function to filter message

def extract_msg(message_f):
    a_list=message_f.split()
    print(a_list)
    #Splitting the message into a list
    
    even_word=lambda x: len(x)%2==0
                                
   #Creating the lambda function to identify even length words
    b_list=list(filter(even_word,a_list))
       
    #Splitting the message into a list
    final_msg=" ".join(b_list)
    #Combining the words of a list back to a single string sentence
    
    return(final_msg)    
    #Returning the sentence

secret_msg_4=extract_msg(message_6) 
print(secret_msg_4)  
    
#Calling the function to read file


#Calling the function 'filter_msg'


#Printing the secret message


#Secret message parts in the correct order

print(secret_msg_3)
print(secret_msg_1)
print(secret_msg_4)
print(secret_msg_2)


message_parts=[secret_msg_3,secret_msg_1,secret_msg_4,secret_msg_2]
#secret_message=str(message_parts)
secret_msg =' '.join(map(str, message_parts)) 

# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message


#Function to write inside a file
def write_file(secret_msg,final_path):
    f=open(final_path,'a+')  
    #Opening a file named 'secret_message' in 'write' mode
    for i in secret_msg:
        f.write('%s'%i)

        #Writing to the file
    
    f.close()

    #Closing the file
a=write_file(secret_msg,final_path)

print(secret_msg)
#Calling the function to w

#my_lst = ['you are now', 1, 'step closer to become', 'Data Scientist'] 
##my_lst_str = ' '.join(map(str, my_lst))
#print(my_lst_str)


#Printing the entire secret message


#Code ends here


