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
    print("5. Редактировать заметку")
    print("6. Удалить заметку")
    print("7. Импортировать заметки из файла")
    print("9. Выход\n")

def handle_choice(choice, notes_app):
    if choice == '1':
        pass
    
    elif choice == '5':
        notes_app.edit_note()
    elif choice == '6':
        notes_app.delete_note()
    elif choice == '7':
        notes_app.import_notes()
    
    elif choice == '9':
        print("До свидания!")
        return 
    
    else:
        print("Неверный ввод. Пожалуйста, выберите число от 1 до 9.")
    return True


if __name__ == "__main__":
    app = NotesApp()
    app.run()