import tkinter
from djiktraslogic import DjikAlgo as Algo
class Btn(tkinter.Button):
    def __init__(self, parent, x, y):
        super().__init__(parent)
        self.pos_x = x
        self.pos_y = y
        self.visited = False
        self.distance = float('inf')



class Djiktras:

    def __init__(self):
        self.window = tkinter.Tk()
        self.N = 10
        self.window.minsize(width=self.N*50, height=self.N*50)

        self.start_cords = []
        self.end_cords = []

        self.buttons = []
        self.generate_buttons()
        self.capture = tkinter.Button(self.window, command=self.get_djiktras, width=7, height=4)
        self.capture.grid(column=0, row=self.N+1)
        self.window.title("Djiktras")

        self.matrix = []
        self.cmd = 0


        self.window.mainloop()
    def print_matrix(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.matrix[i][j], end=' ')
            print()
        print()
        print()
    def refresh_matrix(self):
        self.matrix = [['*' if self.buttons[i][j]['bg']=='brown' else 'X' for j in range(self.N)] for i in range(self.N)]
        self.matrix[self.start_cords[0]][self.start_cords[1]] = 's'
        self.matrix[self.end_cords[0]][self.end_cords[1]] = 'e'
    def generate_buttons(self):
        for i in range(self.N):
            inst = []
            for j in range(self.N):

                button = Btn(self.window, i, j)
                button.config(text="",width=5, height=2, bg="brown", borderwidth='1px', )
                button.config(command= lambda btn=button: self.assign_click(btn))
                button.grid(column=j, row=i, padx=2, pady=2)

                inst.append(button)

            self.buttons.append(inst)


    def make_water(self, button):
        curr = button['bg']
        button.config(bg='blue' if curr=='brown' else 'brown')
        # self.refresh_matrix()
        # self.print_matrix()

    def assign_click(self, button):
        if self.cmd==0:
            self.assign_start(button)
        elif self.cmd==1:
            self.assign_end(button)
        else:
            self.make_water(button)
    def assign_start(self, button):
        curr = button['bg']
        if(curr=='brown'):
            self.cmd+=1

            self.start_cords.append(button.pos_x)
            self.start_cords.append(button.pos_y)
        else:
            self.cmd-=1
        button.config(bg='red' if curr=='brown' else 'brown')

    def assign_end(self, button):
        curr = button['bg']
        if(curr=='brown'):
            self.cmd+=1
            self.end_cords.append(button.pos_x)
            self.end_cords.append(button.pos_y)

        else:
            self.cmd-=1
        button.config(bg='red' if curr=='brown' else 'brown')

        self.refresh_matrix()
        self.print_matrix()


    def get_djiktras(self):
        pass

dj = Djiktras()



