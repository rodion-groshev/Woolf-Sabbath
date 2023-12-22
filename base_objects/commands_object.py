import re
from datetime import datetime
from base_objects.contact_object import Email
from utilities.error_handler import input_error, BadPhoneNumber, BadEmailFormat, BadBirthdayFormat
from base_objects.record_object import Record


class Commands:
    @input_error
    def add_contact(self, book):
        name = input("Enter the name: ")
        phone = input("Enter the phone: ")
        email = input("Enter email: ")
        address = input("Enter the address: ")
        birthday = input("Enter a birthday: ")

        record = Record(name)
        if phone:
            record.add_phone(phone)
        if email:
            record.add_email(email)
        if address:
            record.add_address(address)
        if birthday:
            record.add_birthday(birthday)

        book.add_contact(record)
        return f"Contact {name} added successfully."

    @input_error
    def add_phone(self, args, book):
        name, phone = args
        record = book.find(name)
        record.add_phone(phone)
        return f"Phone: {phone} added to contact {name}."

    @input_error
    def add_email(self, args, book):
        name, email = args
        record = book.find(name)
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if not re.match(email_pattern, email):
            raise BadEmailFormat(email)
        record.add_email(email)
        return f"Email: {email} added to contact {name}."

    @input_error
    def add_address(self, args, book):
        name, address = args
        record = book.find(name)
        record.add_address(address)
        return f"Address: {address} added to contact {name}."

    @input_error
    def add_birthday(self, args, book):
        name, birthday = args
        record = book.find(name)
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
        except ValueError:
            raise BadBirthdayFormat(birthday)
        record.add_birthday(birthday)
        return f"Birthday: {birthday} added to contact {name}."

    @input_error
    def edit_phone(self, args, book):
        name, old_phone, new_phone = args
        if name in book:
            record = book.find(name)
            phone_pattern = re.compile(r'^\+?[1-9]\d{1,14}$')
            if not re.match(phone_pattern, new_phone):
                raise BadPhoneNumber(new_phone)
            record.edit_phone(old_phone, new_phone)
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def edit_email(self, args, book):
        name, old_email, new_email = args
        if name in book:
            record = book.find(name)
            email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            if not re.match(email_pattern, new_email):
                raise BadEmailFormat(new_email)
            record.edit_email(Email(old_email), Email(new_email))
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def edit_address(self, args, book):
        name, address = args
        if name in book:
            record = book.find(name)
            record.edit_address(address)
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def edit_birthday(self, args, book):
        name, birthday = args
        if name in book:
            record = book.find(name)
            try:
                datetime.strptime(birthday, "%d.%m.%Y")
            except ValueError:
                raise BadBirthdayFormat(birthday)
            record.edit_birthday(birthday)
            return "Contact updated."
        else:
            return "Contact not found"

    @input_error
    def show_all(self, book):
        return book.show_all()

    @input_error
    def show_contact(self, args, book):
        name = args[0]
        return book.show_contact(name)

    @input_error
    def show_phone(self, args, book):
        name = args[0]
        return book.show_phone(name)

    @input_error
    def show_email(self, args, book):
        name = args[0]
        return book.show_email(name)

    @input_error
    def show_address(self, args, book):
        name = args[0]
        return book.show_address(name)

    @input_error
    def show_birthday(self, args, book):
        name = args[0]
        return book.show_birthday(name)

    @input_error
    def delete_contact(self, args, book):
        name = args[0]
        return book.delete_contact(name)

    @input_error
    def delete_phone(self, args, book):
        name, phone = args
        record = book.find(name)
        return record.delete_phone(phone)

    @input_error
    def delete_email(self, args, book):
        name, email = args
        record = book.find(name)
        return record.delete_email(email)

    @input_error
    def delete_address(self, args, book):
        name, address = args
        record = book.find(name)
        return record.delete_email(address)

    @input_error
    def delete_birthday(self, args, book):
        name, birthday = args
        record = book.find(name)
        return record.delete_email(birthday)

    @input_error
    def upcoming_birthday(self, book):
        return book.upcoming_birthday()

    @staticmethod
    def help():
        print("\nAvailable Commands:")
        print("--------------------")
        print("add-contact <name> <address> <phone> <email> <birthday>")
        print("add-phone <name> <phone>")
        print("add-email <name> <email>")
        print("add-address <name> <address>")
        print("add-birthday <name> <birthday>")
        print("edit-phone <name> <old_phone> <new_phone>")
        print("edit-email <name> <old_email> <new_email>")
        print("edit-address <name> <new_address>")
        print("edit-birthday <name> <new_birthday>")
        print("show-all")
        print("show-phone <name>")
        print("show-email <name>")
        print("show-address <name>")
        print("show-birthday <name>")
        print("delete-contact <name>")
        print("delete-phone <name> <phone>")
        print("delete-email <name> <email>")
        print("delete-address <name>")
        print("delete-birthday <name>")
        print("birthday")
        print("exit")
        print("help")
