import tkinter as tk

class ClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Простой кликер")
        self.root.geometry("300x200")
        
        self.counter = 0
        
        self.label = tk.Label(
            root, 
            text=f"Кликов: {self.counter}", 
            font=("Arial", 16)
        )
        self.label.pack(pady=20)
        
        self.click_button = tk.Button(
            root,
            text="Кликни меня!",
            command=self.increment_counter,
            bg="lightblue",
            font=("Arial", 12),
            height=2,
            width=15
        )
        self.click_button.pack(pady=10)
        
        self.reset_button = tk.Button(
            root,
            text="Сбросить",
            command=self.reset_counter,
            bg="lightcoral",
            font=("Arial", 10)
        )
        self.reset_button.pack(pady=10)
        
        self.achievement_label = tk.Label(
            root,
            text="",
            font=("Arial", 10),
            fg="green"
        )
        self.achievement_label.pack(pady=10)
    
    def increment_counter(self):
        """Увеличивает счетчик на 1"""
        self.counter += 1
        self.label.config(text=f"Кликов: {self.counter}")
        
        self.check_achievements()
    
    def reset_counter(self):
        """Сбрасывает счетчик до 0"""
        self.counter = 0
        self.label.config(text=f"Кликов: {self.counter}")
        self.achievement_label.config(text="")
    
    def check_achievements(self):
        """Проверяет достижения"""
        if self.counter == 10:
            self.achievement_label.config(text="🎉 Достижение: 10 кликов!")
        elif self.counter == 50:
            self.achievement_label.config(text="🎉🎉 Достижение: 50 кликов!")
        elif self.counter == 100:
            self.achievement_label.config(text="🎉🎉🎉 Достижение: 100 кликов!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickerApp(root)
    root.mainloop()