from utilities import storage
from utilities.error_handler import PhoneNumberIsMissing, ValidationException, BadBirthdayFormat
from base_objects.contact_object import Name, Phone, Field, Birthday, Email, Address
from base_objects.note_object import Note


class Record:
    def __init__(self, name,):
        self.name = Name(name)
        self.phones = []
        self.emails = []
        self.address = None
        self.birthday = None
        self.note = Note()    
        
            
    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def add_email(self, email):
        new_email = Email(email)
        self.emails.append(new_email)

    def add_address(self, address):
        self.address = Address(address)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
        else:
            raise PhoneNumberIsMissing("Phone number not found in the record.")

    def edit_email(self, old_email, new_email):
        if old_email in self.emails:
            index = self.emails.index(old_email)
            self.emails[index] = new_email
        else:
            raise ValidationException("Email not found in the record.")

    def edit_address(self, new_address):
        self.address = Field(new_address)

    def edit_birthday(self, new_birthday):
        if isinstance(new_birthday, Birthday):
            self.birthday = new_birthday
        else:
            raise BadBirthdayFormat("Invalid birthday format. Expected format: dd/mm/yyyy.")

    def delete_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise PhoneNumberIsMissing("Phone number not found in the record.")

    def delete_email(self, email):
        if email in self.emails:
            self.emails.remove(email)
        else:
            raise ValidationException("Email not found in the record.")

    def delete_address(self):
        self.address = None

    def delete_birthday(self):
        self.birthday = None
        
    def add_note(self, note_text):
        self.note.add_record(Note(note_text))

    def delete_note(self, note_id):
        self.notes.remove_record(note_id)

    def edit_note(self, note_id, new_text):
        note = self.notes.data[note_id]
        note.value = new_text
        self.notes.edit_record(note_id, note)

    def __str__(self):
        phones_str = ', '.join(str(phone) for phone in self.phones)
        emails_str = ', '.join(str(email) for email in self.emails)

        return (f"Record(name: {self.name}, phones: [{phones_str}], emails: [{emails_str}], address: {self.address}, "
                f"birthday: {self.birthday})")
