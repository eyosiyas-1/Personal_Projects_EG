import pytest
from proj import recommend_song

def test_recommend_song_found():
    # Test when the song is found in the CSV
    # when running this code make sure to change the string for the csv
    result = recommend_song("Heaven", "Avicii", r"C:\Users\azari\spotify_songs_updated.csv")
    assert result.name == "하드캐리 Hard Carry"
    assert result.artist == "GOT7"


def test_recommend_song_found_2():
    # Another test when the song is found in the CSV
    # when running this code make sure to change the string for the csv
    result = recommend_song("Hello", "Adele", r"C:\Users\azari\spotify_songs_updated.csv")
    assert result.name == "The Highway"
    assert result.artist == "The Restless Age"

def test_recommend_song_found_3():
    # when running this code make sure to change the string for the csv
    # Another test when the song is found in the CSV
    result = recommend_song("Not Ok", "Kygo", r"C:\Users\azari\spotify_songs_updated.csv")
    assert result.name == "Say My Name"
    assert result.artist == "David Guetta"

def test_recommend_song_not_found():
    # Test when the song is not found in the CSV
    # when running this code make sure to change the string for the csv
    result = recommend_song("NonexistentSong", "NonexistentArtist", r"C:\Users\azari\spotify_songs_updated.csv")
    assert result == "Song not found. Try another one!"

if __name__ == "__main__":
    pytest.main([__file__])
