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

    def display_all_notes(self):
        print("Список всех заметок:")
        sorted_notes = sorted(self.notes, key=lambda x: x["priority"], reverse=True)
        for i, note in enumerate(sorted_notes, 1):
            print(f"{i}. Приоритет: {note['priority']}, Заметка: {note['text']}")

def display_menu():
    print("\nМеню:")
    print("3. Установить приоритет заметки")

def handle_choice(choice, notes_app):
    if choice == '1':
        notes_app.display_all_notes()
    elif choice == '2':
        notes_app.add_note()
    elif choice == '3':
        notes_app.set_note_priority()
    else:
        print("Неверный ввод. Пожалуйста, выберите число от 1 до 9.")
    return True

if __name__ == "__main__":
    app = NotesApp()
    app.run()
