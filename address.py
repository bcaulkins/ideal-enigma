import datetime
f = open('journal.txt', 'a')
now = datetime.datetime.now()
entry_date=now.strftime("%m.%d.%Y %H:%M")
journal_entry = raw_input("Start writing:")
##last_name = raw_input("Last Name: ")
##address = raw_input("Address: ")
##phone_num = raw_input("Mobile: ")
##email_address = raw_input("Email Address: ")

##print f ##first_name+" "+last_name, address, phone_num, email_address


f.write('\n'+entry_date+'\n'+'\n'+journal_entry+'\n')


f.close()
