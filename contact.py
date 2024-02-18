class Contact:
    """Represents a person with contact information of name, phone number, and address"""
    def __init__(self, fn, ln, ph, addr, city, zip):
        """initalize first name, last name, phone number, address, city and zip code of contact"""
        self.first_name = fn
        self.last_name = ln
        self.phone = ph
        self.address = addr
        self.city = city
        self.zip = zip

    def __lt__(self,other):
        """return true if left contact's last and first name come before right contact's last and first name"""
        """comparing the names of 2 contact by last name, then first name"""
        """this technically overrides less-than < operator. Used for comparing object"""
        if self.last_name == other.last_name:
            return self.first_name < other.first_name
        return self.last_name < other.last_name     
    
    def __str__(self):
        """string representation of a contact"""
        """a special method in Python class that override str() function"""
        return self.first_name + " " + self.last_name + "\n" + self.phone + "\n" + self.address + "\n" + self.city + " " + self.zip 
    
    def __repr__(self):
        """string representation of a contact that will be written to a file"""
        """a special method in Python class that override repr() function. Used for debugging and logging purpose"""
        """str() - readable vs repr() - offical representation for reconstructing object"""
        return self.first_name + "," + self.last_name + "," + self.phone + "," + self.address + "," + self.city + "," + self.zip
 