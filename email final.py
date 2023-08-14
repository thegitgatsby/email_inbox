#An Email Simulation
import os

# class for creating emails
class Email:
    # the constructor for Email taking in 5 arguments (I chose to add a subject)
    def __init__(self, email_subject, email_contents, from_address, has_been_read = False, is_spam = False):
        self.email_subject = email_subject
        self.email_contents = email_contents
        self.from_address = from_address
        self.has_been_read = has_been_read
        self.is_spam = is_spam

    # printing the object returns a string of the email_contents and from_address
    def __str__(self):
        return(f"""
    Sender: {self.from_address}
    Subject: {self.email_subject}
    Email:  {self.email_contents}
        """)

    # this class method changes the 'is_read' instance variable to True
    # the 'inbox.txt' is updated with this new information
    def mark_as_read(self):
        self.has_been_read = True
        update_inbox()

    # this class method changes the 'is_spam' instance variable to True
    # the 'inbox.txt' is updated with this new information
    def mark_as_spam(self):
        self.is_spam = True
        update_inbox()

#===== The function creates an email object using the arguments============================================
# ...'email_subject' 'email_contents' and 'from_address'
#   this new object is called 'email'
#   the object is appended to the inbox list
#   the 'inbox.txt' is updated with this new information
def add_email(email_subject, email_contents, from_address):
    email = Email(email_subject, email_contents, from_address)
    inbox.append(email)
    update_inbox()

#======= The funtion counts the number of emails in the inbox ===============================================
#   a variable called 'count' is declared which is equal to zero
#   for each email 'item' in inbox the code below is executed
#      'count' is incremented by 1
#   print a message the alternative message
def get_count():
    count = 0
    for email in inbox:
        count += 1
    print(f"""Number of emails in the inbox: {count}""")

#====== The function retrieves specific emails from the inbox using their index =============================
def get_email():
    # if the length of inbox is equal to 0 execute the code below
    #   print the associated message
    if len(inbox) == 0:
        print("You have 0 emails to read in your inbox")
    # else execute the code below
        # display emails in the inbox
        # print the range of indexes to choose from
        #   declare 'email' and make equal to Email object at the inbox index
        #   print email
        #   mark the email as read
    else:
        display_emails()
        print(f"Choose an inbox index from 0 to {len(inbox)-1}")
        index = index_check("read")
        email = inbox[index]
        print(email)
        email.mark_as_read()

# ===== The function sends an email to the inbox ===========================================================
def send_email():

    # This loop will run whilst conditions are true
    while True: 
        # request the user input a subject and store in contents
        # if 'contents' does not contain ";" break from the loop
        # else print an error message
        subject = input("Please enter the subject of your email: ")
        if ";" not in subject:
            break
        else:
           print("Oops! Your email subject can't contain a semicolon - ';'. Please try again.")

    # This loop will run whilst conditions are true
    while True: 
        # request the user input an email message and store in 'contents'
        # if 'contents' does not contain ";" break from the loop
        # else print an error message
        contents = input("Please enter the contents of your email: ")
        if ";" not in contents:
            break
        else:
            print("Oops! Your email contents can't contain a semicolon - ';'. Please try again.")
 
        
        # while the conditions are True execute the code below
    while True:
                
        # request the user input an email address and make equal to 'sender_email'
        sender_email = input("Please enter the senders email address: ")
        # if ";" is in 'sender_email' display an error message
        if ";" in sender_email:
            print("Oops! Your email address can't contain a semicolon - ';'. Please try again.")
            # if "@" is in 'sender_email' display an error message  
        elif "@" not in sender_email:
            print("Oops! Your email needs to include an '@' symbol. e.g. code@camp.com")
        # if "." is in 'sender_email' display an error message
        elif "." not in sender_email:
            print("Oops! Your email needs to include a period '.' e.g. code@camp.com")
        # if 'sender_email' is less than 7 characters long display an error message
        # I picked 7 because an email could be a@b.com
        elif len(sender_email) < 7:
            print("Oops! Your email has less than 7 characters. Please try again.")
        # if the length of 'sender_email' stripped of white space and split by spaces
        #... is equal to more than one the string must be atleast two words
        # this triggers an error message
        elif len(sender_email.strip().split(" ")) > 1:
            print("Oops! Your email has to be one continuous string with no spaces")
        # else if all conditions are fine break from the loop
        else:
            break

        # a new email object is created using 'contents' and 'sender_email' as arguments
        # the 'email' object is appended to inbox
        # 'inbox.txt' is updated with this new information
    email = Email(subject, contents, sender_email)
    inbox.append(email)
    update_inbox()

#===== The function lists the indexes/senders of the unread emails in the inbox ===========================
# I chose not to include the contents so that the email can remain unread 
# ...(otherwise I'd have printed email under the if statement)
#   declare an empty list variable called 'unread_emails'
#   declare a variable called 'unread_email_index' which is equal to 0
#   for each 'email' item in the inbox execute the code below
def get_unread_email():
    unread_emails = []
    unread_email_index = 0
    for email in inbox:    

        # if instance variable 'has_been_read' is equal to False run the code below
        #   append 'unread_email_index' to the 'unread_emails' list
        # increment 'unread_email_index' by 1
        if email.has_been_read == False:
            unread_emails.append(unread_email_index)
        unread_email_index +=1

    # if the length of 'unread_emails' is equal to 0 execute the code below:
    #   print the associated statement
    if len(unread_emails) == 0:
        print("""There are 0 unread emails in the inbox""")

    # else print the number of unread emails in the inbox
    # for the variable 'i' in 'unread_emails' execute the code below
    #     make 'email' equal to the object found at the inbox index
    #     print the inbox index of the email and the associated email address and subject
    else:
        print(f"Number of unread emails in the inbox: {len(unread_emails)}")
    
        for i in unread_emails:
            email = inbox[i]
            print(f"""
    ==========Email [{i}]==========
    Sender: {email.from_address}
    Subject: {email.email_subject}""")

#===== The function lists the inbox index/sender of the spam emails ======================================
#   declare an empty list variable called 'spam_emails'
#   declare a variable called 'spam_email_index' equal to 0
#   for each 'email' item in inbox execute the code below
def get_spam_emails():
    spam_emails = []
    spam_email_index = 0
    for email in inbox:
        
        # if the instance variable 'is_spam' is equal to True execute the code below
        #   append the 'spam_email_index varaible to the 'spam_emails' list
        # increment 'spam_email_index' by 1
        if email.is_spam == True:
            spam_emails.append(spam_email_index)
        spam_email_index += 1
    
    # if the length of 'spam_emails' is equal to 0 execute the code below
    #   print the associated statement
    if len(spam_emails) == 0:
        print("""There are 0 spam emails in the inbox""")
    # else print the number of spam emails in the in the inbox
    #   for each item 'i' in 'spam_emails' execute the code below:
    #       email is equal to index i in the inbox
    #       print the index and sender/subject of the spam email
    else:
        print(f"Number of spam emails in the inbox: {len(spam_emails)}")
        for i in spam_emails:
            email = inbox[i]
            print(f"""
    ==========Email [{i}]========== 
    Sender:  {email.from_address}
    Subject: {email.email_subject}""")

#===== the function deletes an email from the inbox =======================================================
def delete():
    # if the length of the inbox is equal to 0 execute the code below
    #   print the associated statement
    if len(inbox) == 0:
        print("You have 0 emails in your inbox")
    # else display the emails in inbox
    # declare 'index' equal to "delete" ran through the 'index_check()'
    # print the range of indexes the user can choose from
    # declare the 'email' object is equal to the object found at the inbox index
    #       print out the deleted email
    else:
        display_emails()
        index = index_check("delete")
        print(f"Choose an inbox index from 0 to {len(inbox)-1} to delete")
        email = inbox[index]
        print(f"""The following email has been deleted:
{email}""")
        # delete the email from the inbox
        # update the inbox
        inbox.pop(index)
        update_inbox()

#===== the function updates the 'inbox.txt' file with new information =====================================
#   create a new file object 'inbox_file' linked to 'inbox.txt' in write mode
#      declare an empty list variable called 'inbox_data_to_write'
#      for each 'email' item in 'inbox'
#         declare an 'email_str' list with variable equal to the Email instance variables
#         convert all instance variables to strings
#         join the items in 'email_str' with ';' and append to 'inbox_data_to_write'
#     join the items in 'inbox_data_to_write' with '\n' and write to 'inbox_file'
def update_inbox():
    with open("inbox.txt", "w") as inbox_file:
        inbox_data_to_write = []
        for email in inbox:
            email_str = [str(email.email_subject),
            str(email.email_contents),
            str(email.from_address),
            str(email.has_been_read),
            str(email.is_spam)]
            inbox_data_to_write.append(";".join(email_str))
        inbox_file.write("\n".join(inbox_data_to_write))

#====== this function checks if a users input is a numberical value and within range ======================
# it returns an 'inbox_index' integer

def index_check(string):
#   this loop will run whilst the condition is True
    while True:
        # try:
        #   request the user input a number and make it equal to 'inbox_index'
        # except ValueError:
        #   print associated error message and continue with the loop
        try:
            inbox_index = int(input(f"""Please enter the inbox index of the email you would like to {string}: """))
        except ValueError:
            print("""Oops! You failed to enter a number""")
            continue

        # if the inbox index is not in the range specified print an error message
        if inbox_index not in range(0,len(inbox)):
            print(f"""
Oops! Your inbox index was out of range. 
Please enter a number between 0 and {len(inbox)-1}.""")
        
        # else return the 'inbox_index'
        else:
            return(inbox_index)

#=====The function display the emails in the inbox=====================================================
def display_emails():
    # print the associated message
    # declare 'index_count' equal to 0
    # for each 'email' item in inbox execute the code below
    #   print the email subject and sender along with its index
    # increment 'index_count' by one
    print("Email(s) in your inbox:")
    index_count = 0
    for email in inbox:
        print(f"""
    ==========Email {index_count}==========
     Sender: {email.from_address} 
    Subject: {email.email_subject}""")
        index_count += 1


# if the 'inbox.txt' file doesn't exist execute the code below
#   create a file object 'default_file' linked to 'inbox.txt' in write mode
if not os.path.exists("inbox.txt"):
    with open("inbox.txt", "w") as default_file:
        pass

# create a file object called 'inbox_file' linked to 'inbox.txt' in read mode
#   'inbox_data' is equal to 'inbox_file' read and split into items by '\n'
with open("inbox.txt", 'r') as inbox_file:
    inbox_data = inbox_file.read().split("\n")

# declare an empty list variable called 'inbox'
inbox = []

# if the length of 'inbox_data' is more than or equal to 1
# ...or if length of the first item in inbox_data split by ';' is equal to 5
# ...the code below is executed
#   for the 'email_variables' items in 'inbox_data' execute the code below:
#       the 'email_variable' list is made equal to 'email_variables' split by ';'
#       'subject' is made equal to index 0 of 'email_variable'
#       'contents' is made equal to index 1 of 'email_variable'
#       'sender' is made equal to index 2 of 'email_variable'
#       'read_status' is made equal to True if 'email_variable' index 3 is "True"
#       ...else 'read_status' is made equal to False
#       'read_status' is made equal to True if 'email_variable' index 4 is "True"
#       ...else 'read_status' is made equal to False
#       the arguments are ran through the Email constructor to create a new object
#       the email object is appended to inbox
if (len(inbox_data)) >= 1 and len(inbox_data[0].split(";")) == 5:
    for email_variables in inbox_data:
        email_variable = email_variables.split(";")
        subject = email_variable[0]
        contents = email_variable[1]
        sender = email_variable[2]
        read_status = True if email_variable[3] == "True" else False
        spam_status = True if email_variable[4] == "True" else False
        email = Email(subject, contents, sender, read_status, spam_status)
        inbox.append(email)

# user_choice is declared as an empty string
user_choice = ""

#===== while 'user_choice' does not equal 'quit' execute the code below ==================================
#    request the user input a number which corresponds with an option
while user_choice != "8":
    user_choice = input("""
What would you like to do: 
    1 - read
    2 - mark spam
    3 - send
    4 - view unread
    5 - view spam
    6 - view inbox total
    7 - delete an email
    8 - quit

Please enter the corresponding number: """)
    
    # if 'user_choice' equals 1, e.g. 'read, execute the code below
    if user_choice == "1":
        get_email()

    # else if 'user_choice' is equal to 2, e.g. mark spam, execute the code below
    #    if the length of inbox is equal to 0 print the associated message 
    elif user_choice == "2":
        display_emails()
        if len(inbox) == 0:
            print("You have 0 emails in your inbox")
        else:
            #  print the range of inbox indexes the user should choose from
            #  declare 'inbox_index' and make equal to 'index_check("mark as spam")
            #  declare 'email' and make equal to the 'inbox_index' in inbox
            #  run the 'mark_as_spam()' method on email
            #  print a confirmation
            print(f"Choose an inbox index from 0 to {len(inbox)-1}")
            inbox_index = index_check("mark as spam")
            email = inbox[inbox_index]
            email.mark_as_spam()
            print(f"""{email}
        This email has been marked as spam""")
   
    # else if the 'user_choice' equals 3 execute the code below
    elif user_choice == "3":
        send_email()

    # if 'user_choice' is equal to "4" e.g. 'view unread' the code below executes
    elif user_choice == "4":
        get_unread_email()

    # if 'user_choice' is equal to "5" e.g. 'view spam' the code below executes  
    elif user_choice == "5":
        get_spam_emails()

    # if 'user_choice' is equal to "6" e.g. 'view inbox total' the code below executes
    elif user_choice == "6":
        get_count()

    # if 'user_choice' is equal to "7" e.g. 'delete' the code below executes
    elif user_choice == "7":
        delete()

    # if 'user_choice' is equal to "8" e.g. 'quit' the code below executes
    #   print "Goodbye"
    elif user_choice == "8":
        print("Goodbye")

    # else acknowledge an incorrect value has been input
    #   print an error message
    else:
        print("Oops - incorrect input")
