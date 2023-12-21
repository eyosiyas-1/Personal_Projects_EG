import pandas as pd
import argparse
import sys

class Song:
    """Creates an object which stores details related to a given song.

    Attributes:
        name (str): The title of the song
        artist (str): The artist of the song
        genre (str): The song's primary genre
        sub_genre (str): The song's secondary genre
        energy (float): A perceptual measure of intensity and activity for the song
    """
    def __init__(self, name, artist, genre, sub_genre, energy):
        """Initializes a Song object.
        
        Args:
            name (str): See class documentation
            artist (str): See class documentation
            genre (str): See class documentation
            sub_genre (str): See class documentation
            energy (float): See class documentation
        """
        self.name = name
        self.artist = artist
        self.genre = genre
        self.sub_genre = sub_genre
        self.energy = energy


    def __str__(self):
        """Returns the name and artist of the song object as a formatted string.
        
        Args:
            None
        """
        return f"{self.name} by {self.artist}"


def is_song_in_list(name, artist, file_path):
    """Reads in the csv attribute and checks the given song title and artist name
    to make sure the base song exists in the dataset, and creates a Song object using
    the name, artist, genre, subgenre, and energy associated with the song in the dataset.

    Args:
        name (str): The title of the given (base) song, read in from the terminal
        artist (str): The name of the given song's artist, read in from the terminal
        file_path (str): The path to the csv from which song data is being pulled, 
            read in from the terminal
    Returns:
        song_in_list: Song object containing the details of the base song given by the user from the csv
    """
    song_csv_to = pd.read_csv(file_path)
    song_csv = pd.DataFrame(song_csv_to)
    song_finder = song_csv[song_csv['Name'] == name]

    num_songs = len(song_finder)

    if num_songs < 1: 
        return None
    else:
        song_artist = song_finder[song_finder['Artist'] == artist] 

        new_num_songs = len(song_artist)
        if new_num_songs < 1:
            return None
        else:
            index_num = 0

            name_val = song_artist.iat[index_num, 0]
            artist_val = song_artist.iat[index_num, 1]
            genre_val = song_artist.iat[index_num, 2]
            sub_genre_val = song_artist.iat[index_num, 3]
            energy_val = song_artist.iat[index_num, 4]

            song_in_list = Song(name_val, artist_val, genre_val, sub_genre_val, energy_val)
        
    return song_in_list


def recommend_song(name, artist, filepath):
    """Uses the subgenre and energy attributes of the song_in_list object created in the 
    is_song_in_list method to find another song from the dataset which has the same subgenre
    and the closest energy level. If the base song was not found in the csv, returns an error message.

    Args:
        name (str): The name of the Song object returned from the is_song_in_list method
        artist (str): The artist's name of the Song object returned from the is_song_in_list method 
        filepath (str): The path to the csv from which song data is being pulled
    Returns:
        song_to_return: The recommended song that will be produced for the user
    """
    if is_song_in_list(name, artist, filepath) is None:
        return "Song not found. Try another one!"
    else: 
        base_song = is_song_in_list(name, artist, filepath)

        
        base_subgenre = base_song.sub_genre
        base_energy = base_song.energy

        song_csv = pd.read_csv(filepath)
        
        song_finder = song_csv[song_csv['Subgenre'] == base_subgenre]

        song_list = []

        for ind in range(len(song_finder)):

            name_val = song_finder.iat[ind, 0]
            artist_val = song_finder.iat[ind, 1]
            genre_val = song_finder.iat[ind, 2]
            sub_genre_val = song_finder.iat[ind, 3]
            energy_val = song_finder.iat[ind, 4]

            to_be_added = Song(name_val, artist_val, genre_val, sub_genre_val, energy_val)
            song_list.append(to_be_added)

    
        song_to_return = None

        for new_songs in song_list:
            if song_to_return is None or abs(base_energy - new_songs.energy) < abs(base_energy - song_to_return.energy):
                if base_song.name == new_songs.name and base_song.artist == new_songs.artist:
                    continue
                song_to_return = new_songs

        return song_to_return
    
    
def main(name, artist, filepath):
    """Runs the recommend_song method.

    Args:
        name (str): name of the recommended song
        artist (str): artist of the recommended song
        filepath (str): path to the song csv from which song data will be pulled
    Returns:
        recommend_song 
    """
    return recommend_song(name, artist, filepath)


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments.
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('song_name', type=str, help='Song name')
    parser.add_argument('artist_name', type=str, help='Artist name')  
    parser.add_argument('spotify_csv', type=str, help='CSV of songs')

    args = parser.parse_args(args_list)

    return args


if __name__ == "__main__":
    parsed_args = parse_args(sys.argv[1:])

    print(main(parsed_args.song_name, parsed_args.artist_name, parsed_args.spotify_csv))