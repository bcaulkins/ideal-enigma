import datetime
now = datetime.datetime.now()
entry_date=now.strftime("%m.%d.%Y %H:%M")
entry_time=now.strftime("%H:%M")

option = True
while option !="4":
        print("""
-----------------------------
|  1. New Day                |
|  2. Continue Current Day   |
|  3. Read Today's Thoughts  |
|  4. Exit                   |
-----------------------------
""")
        option =input("What do you want to do? ")
        if option == "1":
                with open('journal.txt', 'a') as f, open('tmp.txt', 'w') as t:
                        print ("Journal entry for "+entry_date+" :")
                        journal_entry = input()
                        f.write('\n'+entry_date+'\n'+'\n'+journal_entry+'\n')
                        t.write('\n'+entry_date+'\n'+'\n'+journal_entry+'\n')
        elif option == "2":
                with open('journal.txt', 'a') as f, open('tmp.txt', 'r') as t, open('tmp.txt', 'a') as tmp:
                        tmp_read = t.readline()
                        print('----------------------------')
                        while tmp_read:
                                print(tmp_read.strip())
                                tmp_read = t.readline()
                        print('----------------------------')
                        print ('\n'+"Continue entry @ "+entry_time)
                        journal_entry = input()
                        f.write('\n'+entry_time+'\n'+'\n'+journal_entry+'\n')
                        tmp.write('\n'+entry_time+'\n'+'\n'+journal_entry+'\n')
        elif option == "3":
                with open('tmp.txt', 'r') as tmp:
                        tmp_read = tmp.readline()
                        while tmp_read:
                                print(tmp_read.strip())
                                tmp_read = tmp.readline()