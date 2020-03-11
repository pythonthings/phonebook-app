'''
python3.7 -m pip install pytest

run tests by doing
- pytest filename.py
or - pytest (will run all files with _*.py or _test.py)
'''
from doublyLists import Lists
import pytest

def Add_new_Contact():
    new_contacts = 0
    for i in test_new_contacts:
        llist.push(i[0],i[1],i[2])
        new_contacts +=1
    return new_contacts

def Delete_Contact(contact_delete):
    llist.delete_node(contact_delete)
    total_contacts = llist.print_list()
    return total_contacts

#tests adding the new nodes/contacts to the front of the llist
def test_add_contact():
    assert len_new_cont == Add_new_Contact()

#tests deleting the head
def test_delete_contact_front():
    len_contact = len(test_new_contacts) - 1
    assert len_contact == Delete_Contact('0000000')

#tests deleting anything but the tail or head
def test_delete_contact():
    len_contact = len(test_new_contacts) - 2
    assert len_contact == Delete_Contact('7141234567')

test_new_contacts = [['11111111','jedi','sbs last'],['7141234567','nike','sb last'],['0000000','kid','cudi'],['5555555','mazda','rx7']]
len_new_cont = len(test_new_contacts)

llist = Lists()
