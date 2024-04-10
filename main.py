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

    def add_note(self):
        note_text = input("Введите текст заметки: ")
        self.notes.append({"text": note_text, "priority": 1})
        print("Заметка успешно добавлена!")

    def set_note_priority(self):
        if not self.notes:
            print("Нет доступных заметок для установки приоритета.")
            return

        self.display_all_notes()
        note_index = input("Введите номер заметки, для которой хотите установить приоритет: ")
        try:
            note_index = int(note_index) - 1
            if 0 <= note_index < len(self.notes):
                new_priority = input("Введите приоритет заметки (0, 1, 2, 3): ")
                try:
                    new_priority = int(new_priority)
                    if new_priority not in range(4):
                        print("Неверный приоритет. Приоритет может быть 0, 1, 2 или 3.")
                        return
                    self.notes[note_index]["priority"] = new_priority
                    print("Приоритет заметки успешно установлен.")
                except ValueError:
                    print("Неверный формат ввода. Приоритет должен быть целым числом.")
            else:
                print("Неверный номер заметки.")
        except ValueError:
            print("Неверный формат ввода. Введите целое число.")

def display_menu():
    print("\nМеню:")
    print("1. Просмотреть все заметки")
    print("2. Добавить новую заметку")
    print("3. Установить приоритет заметки")
    print("4. Поиск заметки")

def handle_choice(choice, notes_app):
    if choice == '1':
        notes_app.display_all_notes()
    elif choice == '2':
        notes_app.add_note()
    elif choice == '3':
        notes_app.set_note_priority()
    elif choice == '4':
        notes_app.search_note()
    else:
        print("Неверный ввод. Пожалуйста, выберите число от 1 до 9.")
    return True

if __name__ == "__main__":
    app = NotesApp()
    app.run()
