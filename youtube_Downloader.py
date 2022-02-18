from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

def download():
    url=video_link.get()

    folder=download_path.get()

    get_video=YouTube(url)

    get_stream=get_video.streams.get_highest_resolution()

    get_stream.download(folder)

    messagebox.showinfo("Success","Successfully Downloaded! You may find your video in\n"+folder)

def browse():
    download_dir=filedialog.askdirectory(initialdir="C:\\Users\\naman\\Downloads")

    download_path.set(download_dir)


root = Tk()

root.geometry("800x150")
root.resizable(False,False)
icon=PhotoImage(file="logo.png")
root.iconphoto(True,icon)
root.title("Youtube Video Downloader")
root.config(bg="#00c3ff")


video_link=StringVar()
download_path=StringVar()

link_label=Label(root,text="YouTube URL : ",font=("Lato",16),bg="#fffc47",relief=RAISED)
link_label.grid(row=0,column=0,padx=4,pady=4)

location_label=Label(root,text="Location : ",font=("Lato",16),bg="#fffc47",relief=RAISED)
location_label.grid(row=1,column=0,padx=4,pady=4)

entry1=Entry(root,font=("Lato",16),bg="#f4f4da",relief=RAISED,width=35,textvariable=video_link)
entry1.grid(row=0,column=1,padx=4,pady=4)

entry2=Entry(root,font=("Lato",16),bg="#f4f4da",relief=RAISED,width=30,textvariable=download_path)
entry2.grid(row=1,column=1,padx=4,pady=4)

downloadBt=Button(root,text="Download Video",width=20,font=("Lato",16),relief=RAISED,fg="black",bg="#fffc47",command=download)
downloadBt.grid(row=3,column=1,padx=4,pady=4)

browseBt=Button(root,text="Browse",font=("Lato",16),relief=RAISED,fg="black",bg="#fffc47",command=browse)
browseBt.grid(row=1,column=2,padx=4,pady=4)


root.mainloop()