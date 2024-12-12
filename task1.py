import tkinter

"""import os
import sys""" # Для перезагрузки

class Window1(tkinter.Frame):
    def __init__(self, parent):
        # settings

        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tkinter.BOTH, expand=1)
        self.config(bg="#000033")
        self.create_widgets()

        #objects
    def create_widgets(self):
        """labels"""
        self.lb1 = tkinter.Label(self, text="Введите К", bg="#000033", fg="#ADD8E6", font=("Helvetica", 20))
        self.lb2 = tkinter.Label(self, text="Введите D1", bg="#000033", fg="#ADD8E6", font=("Helvetica", 20))
        self.lb3 = tkinter.Label(self, text="Введите D2", bg="#000033", fg="#ADD8E6", font=("Helvetica", 20))

        self.d1k_str=tkinter.StringVar()
        self.d2k_str=tkinter.StringVar()

        self.lb_res1 = tkinter.Label(self, textvariable=self.d1k_str, bg="#000033", fg="#ADD8E6", font=("Helvetica", 9))
        self.lb_res2 = tkinter.Label(self, textvariable=self.d2k_str, bg="#000033", fg="#ADD8E6", font=("Helvetica", 9))

        self.lb5 = tkinter.Label(self, text="K+D1: ",bg="#000033", fg="#ADD8E6", font=("Helvetica", 20))
        self.lb6 = tkinter.Label(self, text="K+D2: ",bg="#000033", fg="#ADD8E6", font=("Helvetica", 20))

        """buttons & enter fields"""
        self.k_entr = tkinter.Entry(self, bg="#FDF5E6", font=("Helvetica"))
        self.d1_entr = tkinter.Entry(self, bg="#FDF5E6", font=("Helvetica"))
        self.d2_entr = tkinter.Entry(self, bg="#FDF5E6", font=("Helvetica"))

        self.insert_d1_btn = tkinter.Button(self,text="Прибавить D1 к К", command=self.inserting_d1)
        self.insert_d2_btn = tkinter.Button(self, text="Прибавить D2 к К", command=self.inserting_d2)

       #self.restart_btn=tkinter.Button(self, text="Restart", command=self.restart_module)      #Кнопка перезагрузки

        #placement

        """labels"""

        self.lb1.place(x=10, y=10)
        self.lb2.place(x=10, y=60)
        self.lb3.place(x=10, y=100)
        self.lb5.place(x=10, y=160)
        self.lb6.place(x=10, y=260)

        self.lb_res1.place(x=100, y=170)
        self.lb_res2.place(x=100, y=270)


        """buttons & enter fields"""

        self.k_entr.place(x=150, y=20)
        self.d1_entr.place(x=160, y=67)
        self.d2_entr.place(x=165, y=109)

        self.insert_d1_btn.place(x=400, y= 40)
        self.insert_d2_btn.place(x=400, y=80)

        #self.restart_btn.place(x=600, y=10)   # Размещение кнопки перезагрузки

    """def restart_module(self):
        self.parent.destroy()
        python = sys.executable
        os.execl(python, python, *sys.argv)"""  #Функция перезагрузки

    def inserting_d1(self):
        try:

         d1_value = int(self.d1_entr.get())
         k_value = int(self.k_entr.get())

         if not(1 <= d1_value < 10):
            raise ValueError("Значение D1 должно быть в пределе от 1 до 9!")

         self.d1k_str.set(str(d1_value) + str(k_value))

        except ValueError as e:
            self.d1k_str.set(f"Числа введены неверно!: {e}")

    def inserting_d2(self):
        try:

            d2_value = int(self.d2_entr.get())
            k_value = int(self.k_entr.get())

            if not (1 <= d2_value < 10):
                raise ValueError("Значение D1 должно быть в пределе от 1 до 9!")

            self.d2k_str.set(str(d2_value) + str(k_value))

        except ValueError as e:
            self.d2k_str.set(f"Числа введены неверно!: {e}")


"""if __name__ == '__main__':
    application = tkinter.Tk()
    Window1(application)
    application.geometry("720x480+900+500")
    application.title("Lab5_1-322-v01-Shaienko-Vitaliy")
    application.mainloop()"""                                     # Для функции кнопки restart и удобной настройки



