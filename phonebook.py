'''
Phonebook app using doubly linked lists.

Current working Functions
- display
- add new contact
- exit

'''


from doublyLists import Lists


def Add_new_Contact():
    user_input_num = input('Enter mobile number: ')
    user_input_first = input('Enter First name: ')
    user_input_last = input('Enter Last name: ')
    llist.push(str(user_input_num),str(user_input_first),str(user_input_last))

def Display_Contacts():
    print("-----Current Contacts-----")
    list = llist.print_list()

def Exit():
    print("existing..")
    exit()

def menu():
    switch={
        '0':Display_Contacts,
        '1':Add_new_Contact,
        '2':'Find Contact by name',
        '3':'Delete Contact',
        '4':'Update Contact',
        '5':Exit
    }

    while(True):
        print('-------Phonebook menu-------')
        print('0: Display Contacts\n1: Add New Contact\n5:Exit')
        user_input = input('Enter: ')
        switch[user_input]()

def main():
    menu()

if __name__ == '__main__':
    llist = Lists()
    main()
