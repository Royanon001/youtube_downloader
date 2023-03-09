
import tkinter
import webbrowser

import customtkinter
from tkinter import *
from pytube import YouTube
import urllib


def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        title.configure(text=yt_object.title,text_color="white")
        finish_label.configure(text="")
        video.download()
        finish_label.configure(text="Download Complete")


    except:
        finish_label.configure(text="Invalid Link",text_color="red")


def mp3_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        mp3=yt_object.streams.get_audio_only()
        title.configure(text=yt_object.title,text_color="white")
        finish_label.configure(text="")
        mp3.download()
        finish_label.configure(text="Download Complete")

    except:
        finish_label.configure(text="Invalid Link", text_color = "red")


def on_progress(stream, chunk, byte_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size-byte_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPerc.configure(text=per + "%")
    pPerc.update()
# Update Progress Bar
    progressBar.set(float(percentage_of_completion)/100)

# Exit Function


def exit():
    app.destroy()
# Refresh Function


def dev():
    return webbrowser.open("https://twitter.com/RoyMutwiri001")


# System Settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Our App Frame
app = customtkinter.CTk()
app.geometry("1020x480")
app.title("Youtube Downloader")

# App Background
app.geometry("900x400")
c = Canvas(app,bg="gray16",height=200,width=200)
filename = PhotoImage(file="//home//anon//Downloads//Kali2.png")
background_label = Label(app, image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

# Adding UI
title = customtkinter.CTkLabel(app,text="Insert a Youtube Link",text_color="yellow")
title.pack(padx=10,pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()
# Finished Downloading
finish_label = customtkinter.CTkLabel(app,text="")
finish_label.pack()

# Progress Percentage

pPerc = customtkinter.CTkLabel(app,text="0%")
pPerc.pack()

progressBar = customtkinter.CTkProgressBar(app,width=100,height=5)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

# Download Mp3
mp3 = customtkinter.CTkButton(app,text="Download Mp3",text_color="coral",command=mp3_download)
mp3.pack()

# Download Button
download = customtkinter.CTkButton(app,text="Download Video",text_color="yellow",command=start_download)
download.pack(padx=10,pady=10)

# WWKD
wwkd = customtkinter.CTkLabel(app,text="WWKD")
wwkd.pack()

# Refresh Button
ref = customtkinter.CTkButton(app,text="Refresh",text_color="coral")
ref.pack()

# Exit Button
ex = customtkinter.CTkButton(app,text="Exit",text_color="black",command=exit)
ex.pack(padx=15, pady=15)

# Developer Button
dev = customtkinter.CTkButton(app,text="Developed By Anon",command=dev)
dev.place(y=670,x=600)

# Run_App
app.mainloop()
