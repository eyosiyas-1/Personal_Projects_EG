import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import proj

class SongRecommendationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Song Recommendation")

        # Entry widgets
        self.song_entry = ttk.Entry(master, width=30)
        self.artist_entry = ttk.Entry(master, width=30)

        # Labels
        ttk.Label(master, text="Song Name:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        ttk.Label(master, text="Artist Name:").grid(row=1, column=0, padx=10, pady=5, sticky='e')

        # Entry placements
        self.song_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        self.artist_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        # Recommendation button
        ttk.Button(master, text="Recommend Song", command=self.show_recommendation).grid(row=3, column=0, columnspan=2, pady=10)

    def show_recommendation(self):
        song_name = self.song_entry.get()
        artist_name = self.artist_entry.get()
        csv_path = "C:\\Users\\azari\\spotify_songs_updated.csv"


        try:
            recommended_song = proj.recommend_song(song_name, artist_name, csv_path)
            if isinstance(recommended_song, str):
                messagebox.showinfo("Song Recommendation", recommended_song)
            else:
                messagebox.showinfo("Song Recommendation", f"Recommended Song: {recommended_song}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SongRecommendationGUI(root)
    root.mainloop()
