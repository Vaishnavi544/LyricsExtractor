from tkinter import *
from lyrics_extractor import SongLyrics

def get_lyrics():
	song_name=e.get()

	extract_lyrics = SongLyrics("AIzaSyBSIe7sdUm8PWwBCuiJOEqLjUdXH5zo5Bk", "c72903dbc39c247c4")
	
	temp = extract_lyrics.get_lyrics(song_name)
	res = temp['lyrics']
	result.set(res)


# object of tkinter
# and background set to light grey
master = Tk()
master.title('Lyrics Extractor')
master.configure(bg='cyan')

# Variable Classes in tkinter
result = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Enter Song Name : ",font=("Arial", 10)
              ,bg="white").grid(row=0, sticky=W)
Label(master, text="",bg="cyan").grid(row=3, sticky=W)
# Creating label for class variable
# name using widget Entry
Label(master, textvariable=result,bg="cyan").grid(row=3,column=1,sticky=W)

e = Entry(master, width=50)
e.grid(row=0, column=1)

# creating a button using the widget
b = Button(master, text="Generate lyrics",
		command=get_lyrics, bg="lavender")

b.grid(row=0, column=2, columnspan=2,
	rowspan=2, padx=5, pady=5,)

mainloop()
