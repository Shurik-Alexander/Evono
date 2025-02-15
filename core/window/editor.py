from tkinter import *
import tkinter.filedialog   #модуль filedialog для диалогов открытия/закрытия файла
from core.builder import builde
import threading

def editor(physics_box, id):
    threading.Thread(target=__editor__, args=(physics_box, id,)).start()

def __editor__(physics_box, id):
    
    def LoadFile(id):
        textbox.delete('1.0', 'end')    # Очищаем окно редактирования
        textbox.insert('1.0', physics_box.scene[id].__script__)   # Вставляем текст в окно редактирования
        global block_id
        global block_x
        global block_y
        block_x = physics_box.scene[id].x
        block_y = physics_box.scene[id].y
        block_id = id # Храним путь к открытому файлу

    def Quit(ev):
        global root
        root.destroy()
    
    def SaveFile(ev):
        global block_id
        global block_x
        global block_y
        block = builde(physics_box, textbox.get('1.0', 'end'))
        block.x = block_x
        block.y = block_y
        block.id = block_id
        physics_box.scene[block_id] = block
    
    root = Tk()   # объект окна верхнего уровня создается от класса Tk модуля tkinter. 
    #Переменную, связываемую с объектом, часто называют root (корень)

    root.title(u'')


    panelFrame = Frame(root, height = 60, bg = 'gray')
    textFrame = Frame(root, height = 340, width = 600)

    panelFrame.pack(side = 'top', fill = 'x')   #упакуем с привязкой к верху
    textFrame.pack(side = 'bottom', fill = 'both', expand = 1)  

    textbox = Text(textFrame, font='Arial 14', wrap='word')  #перенос по словам метод wrap
    scrollbar = Scrollbar(textFrame)

    scrollbar['command'] = textbox.yview
    textbox['yscrollcommand'] = scrollbar.set

    textbox.pack(side = 'left', fill = 'both', expand = 1)  #текстбокс слева
    scrollbar.pack(side = 'right', fill = 'y')    #расположим скролбар (лифт) справа

    loadBtn = Button(panelFrame, text = 'Загрузить')
    saveBtn = Button(panelFrame, text = 'Сохранить')
    quitBtn = Button(panelFrame, text = 'Выход', bg='#A9A9A9',fg='#FF0000')

    loadBtn.bind("<Button-1>", LoadFile)
    saveBtn.bind("<Button-1>", SaveFile)
    quitBtn.bind("<Button-1>", Quit)

    #loadBtn.place(x = 150, y = 10, width = 130, height = 40)
    saveBtn.place(x = 10, y = 10, width = 130, height = 40)
    #quitBtn.place(x = 290, y = 10, width = 100, height = 40)
    
    LoadFile(id)
    
    root.mainloop()