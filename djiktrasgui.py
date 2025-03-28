import tkinter


class Djiktras:

    def __init__(self):
        self.window = tkinter.Tk()
        self.N = 10
        self.window.minsize(width=self.N*50, height=self.N*50)

        self.buttons = []
        self.generate_buttons()
        self.window.title("Djiktras")

        self.matrix = []



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
    def generate_buttons(self):
        for i in range(self.N):
            inst = []
            for j in range(self.N):
                button = tkinter.Button(self.window, text="",width=5, height=2, bg="brown", borderwidth='1px')
                button.config(command= lambda btn=button: self.make_water(btn))
                button.grid(column=j, row=i, padx=2, pady=2)

                inst.append(button)

            self.buttons.append(inst)
    def make_water(self, button):
        curr = button['bg']
        button.config(bg='blue' if curr=='brown' else 'brown')
        # self.refresh_matrix()
        # self.print_matrix()



dj = Djiktras()



