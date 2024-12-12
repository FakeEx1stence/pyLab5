from task1 import Window1
from task2 import Window2
import tkinter

task_list = {
    "1": (Window1, "Lab5_1-322-v01-Shaienko-Vitaliy", "720x480"),
    "2": (Window2, "Lab5_2-322-v01-Shaienko-Vitaliy", "852x632")

}

choice = input("Please, choose the task 1-2 (0-EXIT): ")
while choice != "0":
    # якщо даний ключ є у словнику
    if choice in task_list.keys():
            # Створення відповідного вікна
        application = tkinter.Tk()
        window_class, window_name, window_size = task_list.get(choice)
        window = window_class(application)
        application.geometry(window_size)
        application.title(window_name)
        application.mainloop()
    else:
        print("Wrong task number!")
    choice = input("Please, choose the task again (0-EXIT): ")
