import tkinter
from tkinter import messagebox
"""import os
import sys""" #Библиотеки для работы кнопки Restart

from pylab import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Window2(tkinter.Frame):
    def __init__(self, parent):
        # settings

        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tkinter.BOTH, expand=1)
        self.config(bg="#cec3a1")
        self.create_widgets()

        self.canvas_visible = False

        #objects
    def create_widgets(self):
        """labels"""

        self.lb1 = tkinter.Label(self,text="Введите N", font=("Noto Sans", 16), bg ="#cec3a1", fg="#28257e")
        self.lb2 = tkinter.Label(self, text="Введите K", font=("Noto Sans", 16), bg="#cec3a1", fg="#28257e")
        self.lb3 = tkinter.Label(self, text="Введите ξ", font=("Noto Sans", 16), bg="#cec3a1", fg="#28257e")
        self.lb4 = tkinter.Label(self, text="Введите U", font=("Noto Sans", 16), bg="#cec3a1", fg="#28257e")
        self.lb5 = tkinter.Label(self, text="Введите T", font=("Noto Sans", 16), bg="#cec3a1", fg="#28257e")

        """buttons & enter fields"""

        self.N_entr = tkinter.Entry(self)
        self.K_entr = tkinter.Entry(self)
        self.Xi_entr = tkinter.Entry(self)
        self.U_entr = tkinter.Entry(self)
        self.T_entr = tkinter.Entry(self)

        self.create_btn=tkinter.Button(self,text="Создать файл", command=self.create_file,
                                       background="#28257e", foreground="#Cec3a1", font=("Noto Sans", 16))

        """self.restart_btn=tkinter.Button(self, text="Restart", command=self.restart_module,
                                        background="#28257e", foreground="#Cec3a1",font=("Noto Sans", 20))"""      #Кнопка перезагрузки

        #placement

        """labels"""

        self.lb1.place(x=10,y=10)
        self.lb2.place(x=10, y=40)
        self.lb3.place(x=10, y=70)
        self.lb4.place(x=10, y=100)
        self.lb5.place(x=10, y=130)

        """buttons & enter fields"""

        self.N_entr.place(x=130, y=15)
        self.K_entr.place(x=130, y=45)
        self.Xi_entr.place(x=130, y=75)
        self.U_entr.place(x=130, y=105)
        self.T_entr.place(x=130, y=135)


        self.create_btn.place(x=260, y=15)


        self.restart_btn.place(x=600, y=10)   # Размещение кнопки перезагрузки


    def create_file(self):
        try:
            self.N = int(self.N_entr.get())
            if self.N < 20:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "N должно быть >= 20!")
        else:
            try:
                self.K = float(self.K_entr.get())
            except ValueError:
                messagebox.showerror("Ошибка", "Некорректный ввод K(!=0)")
            else:
                try:
                    self.Xi = float(self.Xi_entr.get())
                except ValueError:
                    messagebox.showerror("Ошибка", "Некорректный ввод ξ(!=0)")
                else:
                    try:
                        self.U = float(self.U_entr.get())
                    except ValueError:
                        messagebox.showerror("Ошибка", "Некорректный ввод U(!=0)")
                    else:
                        try:
                            self.T = float(self.T_entr.get())
                        except ValueError:
                            messagebox.showerror("Ошибка", "Некорректный ввод T(!=0)")
                        else:
                            x,y = self.calculate_values(self.N, self.K, self.Xi, self.U, self.T)
                            self.data_save(x,y, "graph_data.txt")
                            self.plot_data(x, y)



    """def restart_module(self):
        self.parent.destroy()
        python = sys.executable
        os.execl(python, python, *sys.argv)""" #Функция работы кнопки перезагрузки скрипта


    def calculate_values(self, N,K,Xi,U,T):
        T0 = 2 * T / N
        x = np.linspace(0, N * T0, N)
        y = np.zeros(N)

        for k in range(2, N):
            y[k] = 2 * (1 - (Xi * T0) / T) * y[k - 1] + ((2 * Xi * T0) / T - 1 - (T0**2 / T**2)) * y[k - 2] + ((K * T0**2) / T**2) * U
        return x, y


    def plot_data(self, x, y):
        if not self.canvas_visible:
            self.figure = plt.Figure(figsize=(5, 4), dpi=100)
            self.ax = self.figure.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.parent)
            self.canvas_widget = self.canvas.get_tk_widget()
            self.canvas_widget.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)
            self.canvas.get_tk_widget().place(x=10, y=200)
            self.canvas_visible = True

        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.set_title("№21")
        self.ax.set_xlabel('Время')
        self.ax.set_ylabel('Значение функции')
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()

    def data_save(self, x, y, filename):
        with open(filename, "w") as f:
            for x_vals, y_vals in zip(x, y):
                f.write(f"Шаг: {x_vals} | Значение Y: {y_vals}\n")


"""if __name__ == '__main__':
    application = tkinter.Tk()
    Window2(application)
    application.geometry("852x632+600+300")           # РазрешениехXРазрешениеy+отступ по X+отступ по Y
    application.title("Lab5_2-322-v01-Shaienko-Vitaliy")
    application.mainloop()                                    # Для функции кнопки restart и удобной настройки интерфейса // Сделано студентом 322 группы Шаенко Виталием"""


