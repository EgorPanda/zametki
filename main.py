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
        self.notes.append({"text": note_text, "priority": 1})  # При создании заметки устанавливаем приоритет по умолчанию в 1
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

    def search_note(self):
        keyword = input("Введите ключевое слово для поиска: ")
        found_notes = [note for note in self.notes if keyword.lower() in note["text"].lower()]
        if found_notes:
            print("Найденные заметки:")
            sorted_notes = sorted(found_notes, key=lambda x: x["priority"], reverse=True)
            for i, note in enumerate(sorted_notes, 1):
                print(f"{i}. Приоритет: {note['priority']}, Заметка: {note['text']}")
        else:
            print("Заметки с указанным ключевым словом не найдены.")

    def edit_note(self):
        if not self.notes:
            print("Нет доступных заметок для редактирования.")
            return
        
        self.display_all_notes()
        note_index = input("Введите номер заметки, которую хотите отредактировать: ")
        try:
            note_index = int(note_index) - 1
            if 0 <= note_index < len(self.notes):
                print(f"Заметка {note_index + 1}:")
                print(f"Приоритет: {self.notes[note_index]['priority']}")
                print(f"Текст заметки: {self.notes[note_index]['text']}")
                new_text = input("Введите новый текст заметки: ")
                self.notes[note_index]["text"] = new_text
                print("Заметка успешно отредактирована.")
            else:
                print("Неверный номер заметки.")
        except ValueError:
            print("Неверный формат ввода. Введите целое число.")

    def delete_note(self):
        if not self.notes:
            print("Нет доступных заметок для удаления.")
            return
        
        self.display_all_notes()
        note_index = input("Введите номер заметки, которую хотите удалить: ")
        try:
            note_index = int(note_index) - 1
            if 0 <= note_index < len(self.notes):
                print(f"Заметка {note_index + 1}:")
                print(f"Приоритет: {self.notes[note_index]['priority']}")
                print(f"Текст заметки: {self.notes[note_index]['text']}")
                del self.notes[note_index]
                print("Заметка успешно удалена.")
            else:
                print("Неверный номер заметки.")
        except ValueError:
            print("Неверный формат ввода. Введите целое число.")
    
    def import_notes(self):
        self.notes.extend(import_notes())

    def export_notes(self):
        export_notes(self.notes)


def export_notes(notes):
    filename = input("Введите имя файла для экспорта заметок: ")
    try:
        with open(filename, "w") as file:
            for note in notes:
                file.write(f"Приоритет: {note['priority']}, Заметка: {note['text']}\n")
        print("Заметки успешно экспортированы в файл.")
    except IOError:
        print("Ошибка при записи в файл.")

def import_notes():
    filename = input("Введите имя файла для импорта заметок: ")
    notes = []
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.strip():  # пропускаем пустые строки
                    priority, text = line.strip().split(", ", 1)
                    priority = int(priority.split(": ")[1])
                    text = text.split(": ")[1]
                    notes.append({"text": text, "priority": priority})
        print("Заметки успешно импортированы из файла.")
    except IOError:
        print("Ошибка при чтении файла.")
    return notes

def display_menu():
    print("\nМеню:")
    print("1. Просмотреть все заметки")
    print("2. Добавить новую заметку")
    print("3. Установить приоритет заметки")
    print("4. Поиск заметки")
    print("5. Редактировать заметку")
    print("6. Удалить заметку")
    print("7. Экспортировать заметки в файл")
    print("8. Импортировать заметки из файла")
    print("9. Выход\n")

def handle_choice(choice, notes_app):
    if choice == '1':
        notes_app.display_all_notes()
    elif choice == '2':
        notes_app.add_note()
    elif choice == '3':
        notes_app.set_note_priority()
    elif choice == '4':
        notes_app.search_note()
    elif choice == '5':
        notes_app.edit_note()
    elif choice == '6':
        notes_app.delete_note()
    elif choice == '7':
        notes_app.export_notes()
    elif choice == '8':
        notes_app.import_notes()
    elif choice == '9':
        print("До свидания!")
        return False
    else:
        print("Неверный ввод. Пожалуйста, выберите число от 1 до 9.")
    return True


if __name__ == "__main__":
    app = NotesApp()
    app.run()
