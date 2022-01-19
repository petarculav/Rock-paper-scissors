import tkinter as tk
import random
import re

def rock():
    choice = choices[0]
    answer.set(random.choice(answers))

    compare(choice)

def paper():
     choice = choices[1]
     answer.set(random.choice(answers))

     compare(choice)

def scissors():
    choice = choices[2]
    answer.set(random.choice(answers))


    compare(choice)

def compare(choice):
    global wins
    global losses

    if choice == "Rock":
        if answer.get() == "Paper":
            losses += 1
        elif answer.get() == "Scissors":
            wins += 1
    elif choice == "Paper":
        if answer.get() == "Scissors":
            losses += 1
        elif answer.get() == "Rock":
            wins += 1
    elif choice == "Scissors":
        if answer.get() == "Rock":
            losses += 1
        elif answer.get() == "Paper":
            wins += 1



def reset():
    global wins
    global losses

    wins = 0
    losses = 0
    answer.set("Waiting...")
    username.set("You")

def show_score():
    global wins
    global losses

    result = tk.Toplevel()
    result.title("Score")
    canvas = tk.Canvas(result, bg='white')
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    canvas.create_line(0, 150, 300, 150, fill="black")
    canvas.create_line(85, 200, 85, 100, fill="black")

    wins_str.set(wins)
    losses_str.set(losses)
    
    you = tk.Label(canvas, textvariable = username, background = "white", foreground = "black", font = "none 12")
    you.place(x = 20, y = 120)

    opp = tk.Label(canvas, text = "Opponent", background = "white", foreground = "black", font = "none 12")
    opp.place(x = 2, y = 165)

    you_score = tk.Label(canvas, textvariable = wins_str , background = "white", foreground = "black", font = "none 12")
    you_score.place(x = 100, y = 120)
    
    opp_score = tk.Label(canvas, textvariable = losses_str, background = "white", foreground = "black", font = "none 12")
    opp_score.place(x = 100, y = 165)


def save_txt():
    save_file = open('savefile.txt', 'w')
    save_file.write(username.get() + "\t" + "Opponent" "\n" + wins_str.get() + "\t" + "\t" + losses_str.get() + "\n" + answer.get())
    save_file.close()


def load_txt():
    global wins
    global losses

    load_file = open('savefile.txt', 'r')

    string = load_file.read()
    load_file.close()

    info = []
    ssplit = string.split()

    for word in ssplit:
        info.append(word)

    username.set(info[0])
    wins = int(info[2])
    losses = int(info[3])
    answer.set(str(info[4]))




def change_user():
    login = tk.Toplevel()
    login.geometry("300x200")
    login.title("Change user")

    user = tk.Label(login, text = "Username:")
    user.place(relx = 0.2, rely = 0.5)
    input = tk.Entry(login, textvariable = username)
    input.place(relx = 0.4, rely = 0.5)

    ok = tk.Button(login, text = "OK", command = lambda: username.set(input.get()))
    ok.place(relx = 0.3, rely = 0.7)
    cancel = tk.Button(login, text = "Cancel", command = login.destroy)
    cancel.place(relx = 0.4, rely = 0.7)



root = tk.Tk()
root.geometry("800x400")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command=reset)
filemenu.add_command(label="Change user", command=change_user)
filemenu.add_command(label="Save", command=save_txt)
filemenu.add_command(label="Load", command=load_txt)
filemenu.add_command(label="Score", command=show_score)
filemenu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="File", menu=filemenu)

answer = tk.StringVar()
answers = ["Rock", "Paper", "Scissors"]
answer.set("Waiting...")
wins_str = tk.StringVar()
losses_str = tk.StringVar()

global wins
wins = 0
global losses
losses = 0

wins_str.set(str(wins))
losses_str.set(str(losses))

username = tk.StringVar()
username.set("Petar")

choices = ["Rock", "Paper", "Scissors"]


root.title("Rock, Paper, Scissors")
root.configure(background = "antique white")
root.config(menu = menubar)


head = tk.Label (root, text="Rock, Paper, Scissors", background = "antique white", foreground = "powder blue", font = "none 32 bold")
head.place(relx = 0.5, rely = 0.1, anchor = 'center')

opponent = tk.Label(root, textvariable = answer, background = "antique white", foreground = "black", font = "none 24 bold")
opponent.place(relx = 0.4, rely = 0.4)


rock = tk.Button(root, text = "ROCK", height = 3, width=20, bg = 'cyan', fg = 'black', command = rock)
rock.place(relx = 0.1, rely = 0.7)

paper = tk.Button(root, text = "PAPER", height = 3, width=20, bg = 'SpringGreen2', fg = 'black', command = paper)
paper.place(relx = 0.4, rely = 0.7)

scissors = tk.Button(root, text = "SCISSORS", height = 3, width = 20, bg = 'hot pink', fg = 'black', command = scissors)
scissors.place(relx = 0.7, rely = 0.7)

root.mainloop()
