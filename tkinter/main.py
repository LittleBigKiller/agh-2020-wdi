import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class Observable:
    def __init__(self, initialValue=None):
        self.data = initialValue
        self.callbacks = {}

    def addCallback(self, func):
        self.callbacks[func] = 1

    def delCallback(self, func):
        # pylint: disable=no-member
        del self.callback[func]

    def _docallbacks(self):
        for func in self.callbacks:
            func(self.data)

    def set(self, data):
        self.data = data
        self._docallbacks()

    def get(self):
        return self.data

    def unset(self):
        self.data = None


class View(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.current_screen = 0
        self.master = master
        self.create_initial()

    def create_initial(self):
        self.label = tk.Label(
            self.master,
            text="Program liczący NWD",
            foreground="white",
            background="black"
        )
        self.label.place(x=10, y=10, width=300, height=50)

        self.label_a = tk.Label(
            self.master,
            text="Podaj a: "
        )
        self.label_a.place(x=10, y=70, width=55, height=40)

        self.entry_a = tk.Entry(self.master)
        self.entry_a.place(x=65, y=70, width=90, height=40)

        self.label_b = tk.Label(
            self.master,
            text="Podaj b: "
        )
        self.label_b.place(x=165, y=70, width=55, height=40)

        self.entry_b = tk.Entry(self.master)
        self.entry_b.place(x=220, y=70, width=90, height=40)

        self.b_calculate = tk.Button(
            self.master,
            text="Policz NWD(a, b)",
            # command=self.transition_to_results
        )
        self.b_calculate.place(x=10, y=120, width=300, height=50)

    def write_to_result(self, value):
        if self.current_screen == 1:
            self.result.configure(state="normal")
            self.result.insert(tk.INSERT, value)
            self.result.configure(state="disabled")
        else:
            print("WTT_BAD_SCREEN_ERR: {screen}".format(
                screen=self.current_screen))

    def transition_to_results(self):
        self.current_screen = -1

        self.label.destroy()
        self.label_a.destroy()
        self.entry_a.destroy()
        self.label_b.destroy()
        self.entry_b.destroy()
        self.b_calculate.place_forget()

        self.result = ScrolledText(self.master)
        self.result.config(state="disabled")
        self.result.place(x=10, y=10, width=300, height=160)

        self.current_screen = 1

    def entry_a_fail(self, did_fail=True):
        if did_fail:
            self.entry_a.config(bg="red")
        else:
            self.entry_a.config(bg="white")

    def entry_b_fail(self, did_fail=True):
        if did_fail:
            self.entry_b.config(bg="red")
        else:
            self.entry_b.config(bg="white")


class Controller():
    def __init__(self, root):
        self.model = Model()
        self.model.text_buffer.addCallback(self.text_buffer_changed)
        self.view = View(master=root)
        self.view.b_calculate.config(command=self.calculate_nwd)

    def calculate_nwd(self):
        did_any_fail = False

        self.model.num_a.set(self.view.entry_a.get())
        if not self.model.check_a():
            self.view.entry_a_fail()
            did_any_fail = True
        else:
            self.view.entry_a_fail(False)

        self.model.num_b.set(self.view.entry_b.get())
        if not self.model.check_b():
            self.view.entry_b_fail()
            did_any_fail = True
        else:
            self.view.entry_b_fail(False)

        if not did_any_fail:
            self.view.transition_to_results()
            self.model.find_nwd()

    def text_buffer_changed(self, val):
        # print(val)
        self.view.write_to_result(val)

# Wykorzystując algorytm Euklidesa napisz funkcję wyznaczającą Największy Wspólny
# Dzielnik (NWD) wprowadzonych przez użytkownika liczb. Zwizualizuj w konsoli rekurencyjny
# sposób działania programu.


class Model():
    def __init__(self):
        self.num_a = Observable(0)
        self.num_b = Observable(0)
        self.text_buffer = Observable("")

    def set_a(self, value):
        self.num_a.set(value)

    def check_a(self):
        return self.is_positive_int(self.num_a.get())

    def set_b(self, value):
        self.num_b.set(value)

    def check_b(self):
        return self.is_positive_int(self.num_b.get())

    def set_text(self, value):
        self.text_buffer.set(str(value + "\n"))

    def is_positive_int(self, num):
        if num == "":
            return False

        try:
            num = int(num)
        except:
            return False

        if num <= 0:
            return False

        return True

    def find_nwd(self):
        self.nwd_euclid(self.num_a.get(), self.num_b.get())

    def nwd_euclid(self, a, b):
        a = int(a)
        b = int(b)

        if a < b:       # Funkcja zakłada, że pierwsza z podanych jest większa
            # wywołanie ponowne ze "skorygowanymi" parametrami
            return self.nwd_euclid(b, a)

        if b != 0:
            # Jeżeli 'b' nie wynoosi 0, to wykonujemy dalszy krok w algorytmie ekulidesa
            self.set_text(      # Wizualizujemy krok w algorytmie sformatowanym stringiem
                '{first} = {hmt} * {second} + {diff}'.format(       # Sformatowany string, słowa w '{}' to nazwy zmiennych
                    first=a,        # Przypisanie zmiennej odpowiedniej wartości, tutaj pierwszej liczby podanej naszej funkcji
                    hmt=a//b,       # Przypisanie całkowitej wartości z dzielenia 'a' przez 'b'
                    second=b,
                    diff=a % b      # Przypisanie reszty z dzielenia 'a' przez 'b'
                )
            )

            self.set_text(
                'Wywołanie funkcji nwd_euclid({0}, {1})'.format(b, a % b))

            # ponowne wywołanie naszej funkcji z nowymi danymi - mniejsza z danych ('b') i reszta z dzielenia danych ('a' przez 'b')
            return self.nwd_euclid(b, a % b)

        else:
            self.set_text('Drugi argument funkcji wynosi 0 - znaleziono NWD')
            # Jeżeli 'b' wynosi 0, to oznacza, że podane funkcji 'a' zawiera wartość NWD pierwotnie podanych liczb
            self.set_text('NWD wynosi: {nwd}\n'.format(nwd=a))
            return a


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('320x180')
    root.title("")
    root.resizable(False, False)
    app = Controller(root)
    root.mainloop()
