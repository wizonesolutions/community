from talon import Context, actions

ctx = Context()
key = actions.key

@ctx.action_class('edit')
class EditActions:
    def save():     key('cmd-s')
    def save_all(): key('cmd-shift-s')
    def undo():     key('cmd-z')
    def redo():     key('cmd-shift-z')
    def cut():      key('cmd-x')
    def copy():     key('cmd-c')
    def paste():    key('cmd-v')
    def delete():   key('backspace')

    # basic selection
    def select_none(): key('right')
    def select_all():   key('cmd-a')
    def select_word():  key('left shift-right left alt-left alt-right shift-alt-left')
    # def select_sentence():
    # def select_paragraph():
    def select_line(n: int=None):
        if n is None:
            key('cmd-left cmd-shift-right')
        else:
            key('cmd-up-left')
            for i in range(n):
                key('down')
            key('cmd-left cmd-shift-right')
    def select_lines(a: int, b: int):
        key('cmd-up cmd-left')
        a, b = min((a, b)), max((a, b))
        for i in range(a):
            key('down')
        for i in range(b):
            key('shift-down')
        key('cmd-shift-right')

    # extending selection
    # def extend_column(n: int):
    # def extend_line(n: int):
    def extend_left():       key('shift-left')
    def extend_right():      key('shift-right')
    def extend_up():         key('shift-up')
    def extend_down():       key('shift-down')
    def extend_file_start(): key('cmd-shift-up')
    def extend_file_end():   key('cmd-shift-down')
    def extend_line_up():    key('shift-left cmd-shift-left')
    def extend_line_down():  key('shift-right cmd-shift-right')
    def extend_line_start(): key('cmd-shift-left')
    def extend_line_end():   key('cmd-shift-right')
    def extend_page_up():    key('cmd-shift-pageup')
    def extend_page_down():  key('cmd-shift-pagedown')
    # def extend_again():

    def extend_word_left():  key('cmd-shift-alt-left')
    def extend_word_right(): key('cmd-shift-alt-right')
    # def extend_sentence_previous():
    # def extend_sentence_next():
    # def extend_sentence_start():
    # def extend_sentence_end():
    # def extend_paragraph_previous():
    # def extend_paragraph_next():
    # def extend_paragraph_start():
    # def extend_paragraph_end():

    # moving cursor
    def jump_column(n: int):
        key('cmd-left')
        for i in range(n):
            key('right')
    def jump_line(n: int):   
        key('cmd-up')
        for i in range(n):
            key('down')
    def left():       key('left')
    def right():      key('right')
    def up():         key('up')
    def down():       key('down')
    def file_start(): key('cmd-up cmd-left')
    def file_end():   key('cmd-down cmd-left')
    def line_start(): key('cmd-left')
    def line_end():   key('cmd-right')
    def line_up():    key('up cmd-left')
    def line_down():  key('down cmd-left')
    def page_up():    key('pageup')
    def page_down():  key('pagedown')
    # def move_again():

    def word_left():  key('alt-left')
    def word_right(): key('alt-right')
    # def sentence_previous():  
    # def sentence_next():      
    # def sentence_start():     
    # def sentence_end():       
    # def paragraph_previous(): 
    # def paragraph_next():     
    # def paragraph_start():    
    # def paragraph_end():      

    # misc actions
    def zoom_in():  key('cmd-+')
    def zoom_out(): key('cmd--')

    def line_insert_up():   key('cmd-left enter up')
    def line_insert_down(): key('cmd-right enter')

    def indent_more(): key('cmd-left tab')
    def indent_less(): key('cmd-left delete')

    def delete_line():
        actions.edit.select_line()
        actions.delete()
    def delete_word(): 
        actions.edit.select_word()
        actions.delete()
    # def delete_sentence():
    # def delete_paragraph(): 

    def find(text: str=None): 
        key('cmd-f')
        if text:
            actions.insert(text)
            key('enter')

    def find_next():     key('cmd-g')
    def find_previous(): key('cmd-shift-g')

    def selected_text() -> str:
        with clip.capture() as s:
            key('cmd-c')
        return s.get()

edit = actions.edit
ctx.commands = {
    'go left':  lambda m: edit.left(),
    'go right': lambda m: edit.right(),
    'go up':    lambda m: edit.up(),
    'go down':  lambda m: edit.down(),

    'select none': lambda m: edit.select_none(),
    'select all':  lambda m: edit.select_all(),
    'select word': lambda m: edit.select_word(),
    'select line': lambda m: edit.select_line(),
    # 'select lines': lambda m: edit.select_line(),

    "extend left":  lambda m: edit.extend_left(),
    "extend right": lambda m: edit.extend_right(),
    "extend up":    lambda m: edit.extend_up(),
    "extend down":  lambda m: edit.extend_down(),
    "extend file start": lambda m: edit.extend_file_start(),
    "extend file end":   lambda m: edit.extend_file_end(),
    "extend line up":    lambda m: edit.extend_line_up(),
    "extend line down":  lambda m: edit.extend_line_down(),
    "extend line start": lambda m: edit.extend_line_start(),
    "extend line end":   lambda m: edit.extend_line_end(),
    "extend page up":    lambda m: edit.extend_page_up(),
    "extend page down":  lambda m: edit.extend_page_down(),

    'line start': lambda m: edit.line_start(),
    'line end':   lambda m: edit.line_end(),
}
