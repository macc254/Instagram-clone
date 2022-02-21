class Contact:
    """
    Class that generates new instances of contacts
    
    """

contact_list = [] # Empty contact list

def __init__(self,first_name,last_name,phone_number,email):
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email

def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)
@classmethod
def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)  
        