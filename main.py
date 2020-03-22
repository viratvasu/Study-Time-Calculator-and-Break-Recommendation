from tkinter import *
from tkinter import messagebox
import webbrowser
from pygame import mixer
import settings
mixer.init()
from datetime import date
root=Tk()
root.title("ProductiveTime by -Tapas")
root.geometry("700x500")
def set_settings_from_file():
    global settings_of_music
    global settings_of_break
    try:
        setting_file=open("settings.txt","r")
        setting_data=setting_file.readline().strip("")
        settings_of_music=int(setting_data[0])
        settings_of_break=int(setting_data[1])
    except:
        settings_of_music=1
        settings_of_break=1
set_settings_from_file()
def setting_of_app():
    root.settings = Tk()
    root.settings.title("settings")
    root.settings.geometry("800x300")

    def save_settings():
        settings_file = open("settings.txt", "w")
        settings_file.write(str(settings_of_music))
        settings_file.write(str(settings_of_break))
        settings_file.close()
        print(settings_of_music, settings_of_break)
        root.settings.destroy()
    def music_check_yes():
        global settings_of_music
        music_check_button_yes['state'] = 'disable'
        music_check_button_no['state'] = 'disable'
        settings_of_music = 1

    def music_check_no():
        global settings_of_music
        music_check_button_yes['state'] = 'disable'
        music_check_button_no['state'] = 'disable'
        settings_of_music = 0

    def break_check_yes():
        global settings_of_break
        break_check_button_yes['state'] = 'disable'
        break_check_button_no['state'] = 'disable'
        settings_of_break = 1

    def break_check_no():
        global settings_of_break
        break_check_button_yes['state'] = 'disable'
        break_check_button_no['state'] = 'disable'
        settings_of_break = 0
    text_variable_music="music:"
    text_variable_break="break:"
    if(settings_of_music==1):
        text_variable_music=text_variable_music+"on"
    else:
        text_variable_music = text_variable_music + "off"
    if(settings_of_break==1):
        text_variable_break=text_variable_break+"on"
    else:
        text_variable_break = text_variable_break+ "off"

    Label(root.settings, text="choose your settings.....",font=('arial', 15, 'bold')).grid(row=0, column=0, pady=10)
    Label(root.settings, text=text_variable_music,font=('arial', 15, 'bold')).grid(row=1, column=0, pady=10)
    Label(root.settings, text=text_variable_break, font=('arial', 15, 'bold')).grid(row=2, column=0, pady=10)
    music_check_label = Label(root.settings, text="Music:", font=('arial', 15, 'bold'))
    music_check_label.grid(row=3, column=0, pady=10)
    music_check_button_yes = Button(root.settings, text="ON", font=('arial', 15, 'bold'), command=music_check_yes)
    music_check_button_yes.grid(row=3, column=1, pady=10)
    music_check_button_no = Button(root.settings, text="OFF", font=('arial', 15, 'bold'), command=music_check_no)
    music_check_button_no.grid(row=3, column=2, pady=10)
    break_check_label = Label(root.settings, text="Break:", font=('arial', 15, 'bold'))
    break_check_label.grid(row=4, column=0, pady=10)
    break_check_button_yes = Button(root.settings, text="ON", font=('arial', 15, 'bold'), command=break_check_yes)
    break_check_button_yes.grid(row=4, column=1, pady=10)
    break_check_button_no = Button(root.settings, text="OFF", font=('arial', 15, 'bold'), command=break_check_no)
    break_check_button_no.grid(row=4, column=2, pady=10)
    settings_save_button = Button(root.settings, text="submit your changes", fg="white", bg="black",
                                  font=("arial", 15, "bold"), command=save_settings)
    settings_save_button.grid(row=5, column=0, pady=10)
    root.settings.mainloop()
def message():
    def callable(text):
        webbrowser.open(text)
    root.about_us=Tk()
    root.about_us.title("about us")
    root.about_us.geometry("400x200")
    name=Label(root.about_us,text="This is Tapas ",font=('Helvetica', 25, 'bold'))
    name.pack(side=TOP,pady=10)
    fb=Label(root.about_us,text="click on this to go to my fb page",font=('Helvetica', 15, 'bold italic'),cursor="hand2")
    fb.pack(side=TOP,pady=10)
    fb.bind("<Button-1>",lambda e:callable("https://www.facebook.com/profile.php?id=100011931857908"))
    mail = Label(root.about_us, text="Mail:vasuvirat492@gmail.com", font=('Helvetica', 15, 'bold italic'))
    mail.pack(side=TOP,pady=10)
    contact= Label(root.about_us, text="phone no:6302957061",font=('Helvetica', 15, 'bold italic'))
    contact.pack(side=TOP,pady=10)
    root.about_us.mainloop()
menubar=Menu(root,fg="white",bg="black",font=('arial',12,'bold'),cursor="hand2")
root.config(menu=menubar)
stat_menu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Your Statastics  ",menu=stat_menu)
stat_menu.add_command(label="Today")
stat_menu.add_command(label="Yester Day")
stat_menu.add_command(label="This Week")
stat_menu.add_command(label="this month")
help_bar=Menu(menubar,tearoff=0)
menubar.add_cascade(label="help  ",menu=help_bar)
menubar.add_command(label="  About Us  ",command=message)
menubar.add_command(label="                   Settings  ",command=setting_of_app)
#==========================for clock========
#======variables================
resume=False
time_inseconds=1
stopped=False
break_time=0
number_of_breaks=1
time_of_break=0
time_started=False
settings_of_music
settings_of_break
#==========functions============
def count():
    global time_inseconds
    if(stopped==True):
        time_label.config(text="Data Submitted")
        messagebox.showinfo("infermation","your data has been submitted")
    elif(resume==True):
        time_label.config(text="paused")
    else:
        global break_time
        break_time=break_time+1
        if(break_time==1500 and settings_of_break==1):
            take_break_func()
        else:
            time_inseconds=time_inseconds+1
            temp_time=time_inseconds
            hours=temp_time//3600
            temp_time=temp_time%3600
            minuts=temp_time//60
            temp_time=temp_time%60
            seconds=temp_time
            time_label.config(text=str(hours)+":"+str(minuts)+":"+str(seconds))
            time_label.after(1000,count)
def store_data():
    today = date.today()
    read_file = open("data.txt", "r")
    read_data = read_file.readlines()
    read_file.close()
    try:
        last_data = read_data[-1]
        temp_data = last_data.split(" ")[0]
        if (temp_data == str(today.year) + "-" + str(today.month) + "-" + str(today.day)):
            write_file = open("data.txt", "w")
            read_data.pop()
            temp1_data = float(last_data.split(" ")[1])
            temp1_data = temp1_data + time_inseconds / 3600
            final_data_to_store = temp_data + " " + str(temp1_data)
            read_data.append(final_data_to_store)
            write_file.writelines(read_data)
            write_file.close()

        else:
            write_file = open("data.txt", "w")
            final_data_to_store = "\n" + str(today.year) + "-" + str(today.month) + "-" + str(today.day) + " " + str( time_inseconds / 3600)
            read_data.append(final_data_to_store)
            write_file.writelines(read_data)
            write_file.close()
    except:
        write_file = open("data.txt", "w")
        final_data_to_store =str(today.year) + "-" + str(today.month) + "-" + str(today.day) + " " + str(
            time_inseconds / 3600)
        read_data.append(final_data_to_store)
        write_file.writelines(read_data)
        write_file.close()
def start_time():
    global time_started
    global resume
    time_started=True
    resume=False
    #to again to start though it is stoppped
    #global stopped
    #stopped=False
    start_button['state']='disable'
    resume_button['state']='normal'
    stop_button['state']='normal'
    count()
def resume_time():
    global resume
    resume=True
    start_button['state']='normal'
    resume_button['state']='disable'
    stop_button['state']='normal'
    count()
def stop_time():
    global stopped
    stopped=True
    start_button['state']='disable'
    resume_button['state']='disable'
    stop_button['state']='disable'
    store_data()
    count()
def take_break_func():
    global break_time,number_of_breaks,time_of_break
    number_of_breaks=number_of_breaks+1
    break_time=0
    resume_time()
    if (number_of_breaks % 3 == 1 or number_of_breaks % 3 == 2):
        time_of_break= 10
    else:
        time_of_break= 1800
    root.root3=Tk()
    root.root3.title("Its Time to Break")
    def close_take_break_func():
        if(time_of_break==-1 and settings_of_music==1):
            mixer.music.stop()
        root.root3.destroy()
    def countdown():
        global time_of_break
        min = time_of_break// 60
        sec = time_of_break% 60
        time_label1.config(text=str(min) + ":" + str(sec))
        time_of_break= time_of_break- 1
        if (time_of_break== -1):
            if(settings_of_music==1):
                mixer.music.load("analog-watch-alarm_daniel-simion.wav")
                mixer.music.play(-1)
        else:
            time_label1.after(1000, countdown)
    instruction_label=Label(root.root3,text="Its tine to take to break.....Take a Break to keep your focus on high level")
    instruction_label.pack()
    instruction_label1=Label(root.root3,text="Its good to spent the given to your friends or listen some music for refreshment")
    instruction_label1.pack(pady=10)
    time_label1 = Label(root.root3, text="00:00", font=('arial', 20, 'bold'))
    time_label1.pack()
    close_button=Button(root.root3,text="close the break",command=close_take_break_func)
    close_button.pack(pady=10)
    countdown()
    root.root3.mainloop()

#======widgets==================
middle_frame=Frame(root,width=100,height=100)
middle_frame.pack(pady=100)
time_label=Label(middle_frame,text="00:00:00",font=('arial',20,'bold'))
time_label.grid(row=1,column=1,sticky=W)
start_button=Button(middle_frame,text="start",font=('arial',10,'bold'),fg="white",bg="black",borderwidth=4,relief="raised",command=start_time)
start_button.grid(row=2,column=0,pady=10,padx=5)
resume_button=Button(middle_frame,text="resume",font=('arial',10,'bold'),fg="white",bg="black",state="disabled",borderwidth=4,relief="raised",command=resume_time)
resume_button.grid(row=2,column=1,pady=10,padx=5)
stop_button=Button(middle_frame,text="submit",font=('arial',10,'bold'),fg="white",bg="black",borderwidth=4,relief="raised",command=stop_time,state="disabled")
stop_button.grid(row=2,column=2,pady=10,padx=5)
#take_break=Button(middle_frame,text="Take Break",font=('arial',10,'bold'),fg="white",bg="black",borderwidth=4,relief="raised",command=take_break_func)
#take_break.grid(pady=30,row=3,column=1)
def on_closing():
    if(stopped==False and time_started==True):
        def yes():
            store_data()
            root.destroy()
            root.root2.destroy()
        def no():
            root.destroy()
            root.root2.destroy()
        root.root2=Tk()
        root.root2.title("Confiramtion!!")
        root.root2.geometry("300x100")
        frame=Frame(root.root2,width=200,height=200)
        frame.pack()
        label=Label(frame,text="You didn't submitted your data ")
        label.grid(row=0,column=0,sticky=W)
        label1 = Label(frame, text="would you like to submit it ?? ")
        label1.grid(row=1,column=0,sticky=W)
        button=Button(frame,text="Yes",command=yes)
        button.grid(row=2,column=0,sticky=W,pady=20)
        button1 = Button(frame, text="No",command=no)
        button1.grid(row=2, column=1,sticky=E,pady=20)
        root.root2.mainloop()
    else:
        root.destroy()
root.protocol("WM_DELETE_WINDOW",on_closing)
#===========================================
root.mainloop()
