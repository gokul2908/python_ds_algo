import contactList

myContact = contactList.ContactDetailsSaver()

myContact.addContact('geetha', 143243)
myContact.addContact('gokul', 143243)
myContact.addContact('kesav', 121212)
myContact.addContact('kumar', 121212)
myContact.addContact('geetha', 14323)
myContact.addContact('gokul', 143243)
myContact.addContact('kesav', 121212)
myContact.addContact('kumar', 121212)
'''
myContactTemp = contactList.ContactDetailsSaver()
myContactTemp.addContact('geetha', 143243)
myContactTemp.addContact('gokul', 143243)
'''
print(myContact.contactList.get('g'))
print(myContact.contactList.get('k'))
print(myContact.contactList)
#print(myContactTemp.contactList)