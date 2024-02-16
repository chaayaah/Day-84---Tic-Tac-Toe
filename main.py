from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")


clicked = True
count = 0


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def check_winner():
    global winner
    winner = False
    if count < 9:
        if b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X":
            winner = True
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X":
            winner = True
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X":
            winner = True
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X":
            winner = True
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X":
            winner = True
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X":
            winner = True
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X":
            winner = True
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X":
            winner = True
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O":
            winner = True
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O":
            winner = True
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O":
            winner = True
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O":
            winner = True
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O":
            winner = True
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O":
            winner = True
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O":
            winner = True
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
        elif b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O":
            winner = True
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            messagebox.showinfo("Tic Tac Toe", message="Player X wins!")
            disable_all_buttons()
    else:
        messagebox.showinfo("Tic Tac Toe", "Draw!")
        disable_all_buttons()
def button_click(button):
    global clicked, count
    if button['text'] == " " and clicked == True:
        button['text'] = "X"
        clicked = False
        count = count + 1
        check_winner()
    elif button['text'] == " " and clicked == False:
        button['text'] = "O"
        clicked = True
        count = count + 1
        check_winner()
    else:
        messagebox.showerror("Tic Tac Toe", "This is already clicked. Click other buttons ...")


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count= 0
    # 1. Build the buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                background="SystemButtonFace", command=lambda: button_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                background="SystemButtonFace", command=lambda: button_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                background="SystemButtonFace", command=lambda: button_click(b3))

    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                background="SystemButtonFace", command=lambda: button_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                background="SystemButtonFace", command=lambda: button_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                background="SystemButtonFace", command=lambda: button_click(b6))

    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                background="SystemButtonFace", command=lambda: button_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                background="SystemButtonFace", command=lambda: button_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                background="SystemButtonFace", command=lambda: button_click(b9))

# 2. Grid the button
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

#3. Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)
reset()

root.mainloop()