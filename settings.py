from tkinter import *
settings_of_music=1
settings_of_break=1
def start():
    root= Tk()
    root.title("settings")
    root.geometry("500x200")
    def save_settings():
        settings_file = open("settings.txt", "w")
        settings_file.write(str(settings_of_music))
        settings_file.write(str(settings_of_break))
        settings_file.close()
        print(settings_of_music,settings_of_break)
    def music_check_yes():
        global settings_of_music
        music_check_button_yes['state']='disable'
        music_check_button_no['state'] = 'disable'
        settings_of_music=1
    def music_check_no():
        global settings_of_music
        music_check_button_yes['state']='disable'
        music_check_button_no['state'] = 'disable'
        settings_of_music=0
    def break_check_yes():
        global settings_of_break
        break_check_button_yes['state']='disable'
        break_check_button_no['state'] = 'disable'
        settings_of_break=1
    def break_check_no():
        global settings_of_break
        break_check_button_yes['state']='disable'
        break_check_button_no['state'] = 'disable'
        settings_of_break=0
    Label(root, text="Choose your setting .....", font=('arial', 15, 'bold')).grid(row=0, column=0, pady=10)
    music_check_label = Label(root, text="do you want music:", font=('arial', 15, 'bold'))
    music_check_label.grid(row=1, column=0, pady=10)
    music_check_button_yes = Button(root, text="Yes",font=('arial', 15, 'bold'),command=music_check_yes)
    music_check_button_yes.grid(row=1, column=1, pady=10)
    music_check_button_no = Button(root, text="No",font=('arial', 15, 'bold'),command=music_check_no)
    music_check_button_no.grid(row=1, column=2, pady=10)
    break_check_label = Label(root, text="do you want breaks:", font=('arial', 15, 'bold'))
    break_check_label.grid(row=2, column=0, pady=10)
    break_check_button_yes = Button(root, text="Yes",font=('arial', 15, 'bold'),command=break_check_yes)
    break_check_button_yes.grid(row=2, column=1, pady=10)
    break_check_button_no = Button(root, text="No",font=('arial', 15, 'bold'),command=break_check_no)
    break_check_button_no.grid(row=2, column=2, pady=10)
    settings_save_button = Button(root, text="submit your changes", fg="white", bg="black",
                                  font=("arial", 15, "bold"), command=save_settings)
    settings_save_button.grid(row=3, column=0, pady=10)
    root.mainloop()
if __name__=="__main__":
    start()