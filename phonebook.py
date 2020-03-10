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
    llist.print_list()

def Search_for_Contact():
    user_input = input('Search by mobile number: ')
    llist.search_list(user_input)

def Delete_Contact():
    user_input = input('Enter number to delete: ')
    llist.delete_node(user_input)

def Exit():
    print("exiting..")
    exit()

def menu():
    switch={
        '0':Display_Contacts,
        '1':Add_new_Contact,
        '2':Search_for_Contact,
        '3':Delete_Contact,
        '4':'Update Contact',
        '5':Exit
    }

    while(True):
        print('-------Phonebook menu-------')
        print('0: Display Contacts\n1: Add New Contact\n2:Search for Contact\n3:Delete a Contact\n5:Exit')
        user_input = input('Enter: ')
        switch[user_input]()

def main():
    menu()

if __name__ == '__main__':
    llist = Lists()
    main()
