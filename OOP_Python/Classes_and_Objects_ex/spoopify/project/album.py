from typing import Tuple

from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.songs = [*songs]
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song in self.songs:
            return "Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."
        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
            self.songs.remove(song)
            return f"Removed song {song_name} from album {self.name}."
        except StopIteration:
            return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self) -> str:
        songs_info = "\n".join(f'== {s.get_info()}' for s in self.songs)
        return f"Album {self.name}\n" \
               f"{songs_info}"
