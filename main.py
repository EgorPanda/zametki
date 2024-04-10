class NotesApp:
    def __init__(self):
        self.notes = []

    def run(self):
        print("Приложение запущено")
        while True:
            display_menu()
            choice = input("Выберите действие: ")
            if not handle_choice(choice, self):
                break

    def add_note(self):
        note_text = input("Введите текст заметки: ")
        self.notes.append({"text": note_text, "priority": 1})
        print("Заметка успешно добавлена!")

def display_menu():
    print("\nМеню:")
    print("2. Добавить новую заметку")
    
def handle_choice(choice, notes_app):
    if choice == '1':
        notes_app.display_all_notes()
    elif choice == '2':
        notes_app.add_note()
    else:
        print("Неверный ввод. Пожалуйста, выберите число от 1 до 9.")
    return True

if __name__ == "__main__":
    app = NotesApp()
    app.run()
