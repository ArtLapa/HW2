from abc import ABC, abstractmethod
import os
import shutil
import datetime

class UIComponent(ABC):
    @abstractmethod
    def display(self):
        pass

class ContactUI(UIComponent):
    def __init__(self, contacts):
        self.contacts = contacts

    def display(self):
        print("Contacts:")
        for contact in self.contacts:
            print(f"{contact.name} - {contact.phone}")

class NoteUI(UIComponent):
    def __init__(self, notes):
        self.notes = notes

    def display(self):
        print("Notes:")
        for note in self.notes:
            print(f"Note: {note.text}, Tags: {', '.join(note.tags)}")

class FileUI(UIComponent):
    def __init__(self, files):
        self.files = files

    def display(self):
        print("Files:")
        for file in self.files:
            print(f"File: {file.name}, Category: {file.category}")

class MainMenuUI(UIComponent):
    def display(self):
        print("\nMain Menu:")
        print("1. Show Contacts")
        print("2. Show Notes")
        print("3. Show Files")
        print("4. Exit")

class Contact:
    def __init__(self, name, address, phone, email, birthday):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.birthday = birthday

class Note:
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags

class File:
    def __init__(self, name, category):
        self.name = name
        self.category = category

class PersonalAssistant:
    def __init__(self):
        self.contacts = []
        self.notes = []
        self.files = []

    def add_contact(self, name, address, phone, email, birthday):
        new_contact = Contact(name, address, phone, email, birthday)
        self.contacts.append(new_contact)

    def search_contacts(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower()]
        return results

    def add_note(self, text, tags):
        new_note = Note(text, tags)
        self.notes.append(new_note)

    def search_notes_by_tags(self, query_tags):
        results = [note for note in self.notes if set(query_tags).issubset(note.tags)]
        return results

    def add_file(self, name, category):
        new_file = File(name, category)
        self.files.append(new_file)

    def sort_files_by_category(self, folder_path):
        for file in self.files:
            category_folder = os.path.join(folder_path, file.category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
            shutil.move(file.name, category_folder)

# Функція для виведення інтерфейсу
def display_ui(ui_components):
    for component in ui_components:
        component.display()

# Приклад використання:
assistant = PersonalAssistant()

# Додавання контактів
assistant.add_contact("John Doe", "123 Main St", "555-1234", "john@example.com", datetime.date(1990, 5, 20))
assistant.add_contact("Jane Smith", "456 Oak St", "555-5678", "jane@example.com", datetime.date(1985, 8, 15))

# Додавання нотаток
assistant.add_note("Meeting at 2 PM", ["work", "meeting"])
assistant.add_note("Shopping list", ["personal"])

# Додавання файлів
assistant.add_file("document1.txt", "documents")
assistant.add_file("image1.jpg", "images")

# Виведення інтерфейсу
ui_components = [
    MainMenuUI(),
    ContactUI(assistant.contacts),
    NoteUI(assistant.notes),
    FileUI(assistant.files)
]

display_ui(ui_components)

