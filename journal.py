import datetime
f = open('journal.txt', 'a')
now = datetime.datetime.now()
entry_date=now.strftime("%m.%d.%Y %H:%M")
entry_time=now.strftime("%H:%M")

option = True
while option:
	print("""
	1. New entry
	2. Continue Current Entry
	3. Exit""")
	option =raw_input("What do you want to do?")
	if option == "1":
		print "Journal entry for "+entry_date+" :"
		journal_entry = raw_input()
		f.write('\n'+entry_date+'\n'+'\n'+journal_entry+'\n')
	elif option == "2":
		print "Continue entry @ "+entry_time
		journal_entry = raw_input()
		f.write('\n'+entry_time+'\n'+'\n'+journal_entry+'\n')		
	elif option !="":
		print '\n'"Not valid option"


f.close()
