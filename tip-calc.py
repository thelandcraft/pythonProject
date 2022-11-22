from tkinter import Tk, Radiobutton, Button, Label, StringVar, IntVar, Entry


class TipCalculator():
    def __init__(self):
        window = Tk()

        window.title("Калькулятор чаевых")
        window.configure(background="grey")
        window.geometry("390x320")
        window.resizable(width=False, height=False)

        # self.var_name = datatypes()
        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        # метки для создания текстовых полей и их конфигурации
        tip_percent = Label(window, text="Процент чаевых",
                            bg="light blue", fg="black")
        tip_percent.grid(column=0, row=0, padx=15, pady=30)
        bill_amount = Label(window, text="Цена чека",
                            bg="light blue", fg="black")
        bill_amount.grid(column=1, row=0, padx=15, pady=30)
        bill_amount_entry = Entry(
            window, textvariable=self.meal_cost, width=14)
        bill_amount_entry.grid(column=2, row=0, padx=15, pady=30)

        # переключатели для % с конфигурациями
        five_percent_tip = Radiobutton(
            window, text="05%", variable=self.tip_percent, value=5)
        five_percent_tip.grid(column=0, row=1)

        ten_percent_tip = Radiobutton(
            window, text="10%", variable=self.tip_percent, value=10)
        ten_percent_tip.grid(column=0, row=2)

        fifteen_percent_tip = Radiobutton(
            window, text="15%", variable=self.tip_percent, value=15)
        fifteen_percent_tip.grid(column=0, row=3)

        twenty_percent_tip = Radiobutton(
            window, text="20%", variable=self.tip_percent, value=20)
        twenty_percent_tip.grid(column=0, row=4)

        twentyfive_percent_tip = Radiobutton(
            window, text="25%", variable=self.tip_percent, value=25)
        twentyfive_percent_tip.grid(column=0, row=5)

        tip_amount_lb1 = Label(window, text="Чаевые",
                               bg="light blue", fg="black")
        tip_amount_lb1.grid(column=1, row=3, padx=15)

        tip_amount_entry = Entry(window, textvariable=self.tip, width=14)
        tip_amount_entry.grid(column=2, row=3)

        bill_total_lb1 = Label(window, text="Итоговая сумма",
                               bg="light blue", fg="black")
        bill_total_lb1.grid(column=1, row=5, padx=15)

        bill_total_entry = Entry(
            window, textvariable=self.total_cost, width=14)
        bill_total_entry.grid(column=2, row=5)

        calculate_btn = Button(window, text="Вычислить",
                               bg="light green", fg="black", command=self.calculate)
        calculate_btn.grid(column=1, row=7, padx=25, pady=25)

        clear_btn = Button(window, text="Стереть",
                           bg="pink", fg="black", command=self.clear)
        clear_btn.grid(column=2, row=7, padx=25, pady=25)

        window.mainloop()

    # функция для расчета суммы чаевых и общей суммы
    def calculate(self):
        pre_tip = float(self.meal_cost.get())
        percentage = self.tip_percent.get() / 100
        tip_amount_entry = pre_tip * percentage
        self.tip.set(tip_amount_entry)

        final_bill = pre_tip + tip_amount_entry
        self.total_cost.set(final_bill)

    # функция для очистки функции

    def clear(self):
        self.total_cost.set("")
        self.meal_cost.set("")
        self.tip.set("")


TipCalculator()
