import tkinter as tk


def main():
    root = tk.Tk()

    message = tk.Label(root, text="Hello, World!")
    message.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
