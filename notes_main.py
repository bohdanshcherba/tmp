from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import( QApplication, QWidget,
 QPushButton, QLabel, QListWidget, 
 QLineEdit, QTextEdit, QInputDialog,
 QHBoxLayout, QVBoxLayout, QFormLayout, QMessageBox
)
import json
app = QApplication([])

main_win = QWidget()

main_win.setWindowTitle("Smart notes")
main_win.resize(900,600)

#Створюємо віджети

field_text = QTextEdit()

list_notes_label = QLabel('Список заміток')
list_notes = QListWidget()

btn_note_create = QPushButton('Створити замітку')
btn_note_del = QPushButton('Видалити замітку')
btn_note_save = QPushButton('Зберигти замітку')


list_tags_label = QLabel('Список тегів')
list_tags = QListWidget()

field_tag = QLineEdit('')
field_tag.setPlaceholderText("Введіть тег")

button_tag_add = QPushButton('Додати до замітки')
button_tag_del = QPushButton('Відкріпити від замітки')
button_tag_search = QPushButton('Шукати замітки по тегу')

layout_main = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

col_1.addWidget(field_text)


col_2.addWidget(list_notes_label)
# самостійно далі
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(btn_note_create)
row_1.addWidget(btn_note_del)
col_2.addLayout(row_1)
col_2.addWidget(btn_note_save)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
col_2.addLayout(row_3)
col_2.addWidget(button_tag_search)

layout_main.addLayout(col_1, stretch=2)
layout_main.addLayout(col_2, stretch=1)

main_win.setLayout(layout_main)

# функціонал программи
notes = {}
def add_note():
    note_name, ok = QInputDialog.getText(main_win, "Додати замітку", "Назва замітки: ")

    if ok:
        notes[note_name] = {
            "text": "",
            "tags": []
        }

        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['tags'])


def show_note():
    key = list_notes.selectedItems()[0].text()

    field_text.setText(notes[key]['text'])
    list_tags.clear()
    list_tags.addItems(notes[key]['tags'])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()

        with open('notes.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Виберіть замітку")

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags()
        field_text.clear()
        list_notes.addItems(notes)

        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Вибріть замітку")

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if tag != '':
            notes[key]["tags"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()

        notes[key]['tags'].remove(tag)

        list_tags.clear()
        list_tags.addItems(notes[key]["tags"])
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        

button_tag_del.clicked.connect(del_tag)
button_tag_add.clicked.connect(add_tag)
with open('notes.json', 'r') as file:
    notes = json.load(file)
list_notes.addItems(notes)


btn_note_save.clicked.connect(save_note)
list_notes.itemClicked.connect(show_note)
btn_note_create.clicked.connect(add_note)



main_win.show()

app.exec_()
