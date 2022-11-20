from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import( QApplication, QWidget,
 QPushButton, QLabel, QListWidget, 
 QLineEdit, QTextEdit, QInputDialog,
 QHBoxLayout, QVBoxLayout, QFormLayout
)

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

main_win.show()

app.exec_()
