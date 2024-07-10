import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def fetch_lyrics():
    song = entry_song.get()
    if not song:
        messagebox.showwarning("Input Error", "Please enter a song name.")
        return
    lyrics = get_lyrics_from_genius(song)
    if lyrics:
        text_lyrics.delete(1.0, tk.END)
        text_lyrics.insert(tk.END, f"Song: {song}\n\n{lyrics}")
    else:
        messagebox.showerror("Error", "Could not fetch lyrics. Please try again.")

def get_lyrics_from_genius(song):
    base_url = "https://api.genius.com"
    headers = {'Authorization': 'Bearer 0tFemNxHGarftHCsWiovuL1wHTG3wGojiFAtbDufwEvlKhpywFInESVcKsUgRS2a'}
    search_url = base_url + "/search"
    data = {'q': song}
    response = requests.get(search_url, headers=headers, params=data)
    
    if response.status_code != 200:
        print(f"API request failed with status code {response.status_code}")
        print(response.text)
        return None
    
    json = response.json()
    if 'response' in json and 'hits' in json['response']:
        for hit in json['response']['hits']:
            song_api_path = hit['result']['api_path']
            song_url = base_url + song_api_path
            song_response = requests.get(song_url, headers=headers)
            
            if song_response.status_code != 200:
                print(f"Song API request failed with status code {song_response.status_code}")
                print(song_response.text)
                return None
            
            song_json = song_response.json()
            if 'response' in song_json and 'song' in song_json['response']:
                path = song_json['response']['song']['path']
                page_url = "https://genius.com" + path
                page = requests.get(page_url)
                
                if page.status_code != 200:
                    print(f"Page request failed with status code {page.status_code}")
                    print(page.text)
                    return None
                
                html = BeautifulSoup(page.text, 'html.parser')
                lyrics_div = html.find('div', class_='lyrics')
                if lyrics_div:
                    return lyrics_div.get_text()
    return None

# Create the main window
root = tk.Tk()
root.title("Lyrics Extractor")

# Create and place widgets
tk.Label(root, text="Song Name:").grid(row=0, column=0, padx=10, pady=10)
entry_song = tk.Entry(root, width=50)
entry_song.grid(row=0, column=1, padx=10, pady=10)

btn_fetch = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
btn_fetch.grid(row=1, column=0, columnspan=2, pady=20)

text_lyrics = tk.Text(root, wrap=tk.WORD, width=60, height=20)
text_lyrics.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
