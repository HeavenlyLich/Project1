import tkinter as tk
from tkinter import messagebox




class TicTacToeBase:
    """Базовий клас з логікою, яку ми будемо перевизначати"""

    def __init__(self, title):
        self.window = tk.Toplevel()  # Використовуємо Toplevel для вікна гри
        self.window.title(title)
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []

    #Додаткова зміна
class TicTacToeBuggy(TicTacToeBase):
    def __init__(self):
        super().__init__("Хрестики-нулики (BUGGY)")
        self.label_text = tk.StringVar(value="Зараз ходить: X")
        self.create_widgets()
        self.window.geometry("150x150")  # BUG: Мале вікно

    def create_widgets(self):
        # Fix: Додали Label з індикацією ходу
        tk.Label(self.window, textvariable=self.label_text, font=('Arial', 12)).grid(row=3, column=0, columnspan=3)
        for i in range(9):
            if i == 4:  # BUG: Крива червона кнопка
                btn = tk.Button(self.window, text=" ", font=('Arial', 10), width=2, height=1,
                                command=lambda i=i: self.make_move(i), bg="red")
            else:
                btn = tk.Button(self.window, text=" ", font=('Arial', 20), width=5, height=2,
                                command=lambda i=i: self.make_move(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def make_move(self, i):
        if self.board[i] == " ":  # BUG: Дозволяє перезапис \\ Виправлено
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Перемога", f"Виграв {self.current_player}")
                self.window.destroy()
            elif " " not in self.board:
                messagebox.showinfo("Нічия", "Гра завершена нічиєю!")
                self.window.destroy() # Додаємо скидання
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label_text.set(f"Зараз ходить: {self.current_player}")


    def check_winner(self):
        # BUG: Відсутні діагоналі
        win_coords = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]            # ВИПРАВЛЕНО: Діагоналі
        for combo in win_coords:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False


class TicTacToeClean(TicTacToeBase):
    def __init__(self):
        super().__init__("Хрестики-нулики (CLEAN)")
        self.label_text = tk.StringVar(value="Зараз ходить: X")
        self.create_widgets()

    def create_widgets(self):
        # FIX: Додано індикатор ходу
        tk.Label(self.window, textvariable=self.label_text, font=('Arial', 12)).grid(row=3, column=0, columnspan=3)
        for i in range(9):
            btn = tk.Button(self.window, text=" ", font=('Arial', 20), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def make_move(self, i):
        if self.board[i] == " ":  # FIX: Перевірка зайнятості
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Перемога", f"Виграв {self.current_player}")
                self.window.destroy()
            elif " " not in self.board:
                messagebox.showinfo("Нічия", "Гру закінчено!")
                self.window.destroy()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label_text.set(f"Зараз ходить: {self.current_player}")

    def check_winner(self):
        # FIX: Всі комбінації на місці
        win_coords = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in win_coords:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False


def main_menu():
    root = tk.Tk()
    root.title("Вибір версії")
    root.geometry("300x150")

    tk.Label(root, text="Оберіть версію програми:", font=('Arial', 12)).pack(pady=10)

    tk.Button(root, text="Запустити з БАГАМИ", bg="red", fg="white",
              command=TicTacToeBuggy).pack(fill='x', padx=20, pady=5)

    tk.Button(root, text="Запустити ВИПРАВЛЕНУ версію", bg="green", fg="white",
              command=TicTacToeClean).pack(fill='x', padx=20, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main_menu()