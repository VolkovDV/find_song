from dataclasses import dataclass


@dataclass(order=True)
class Song:
    """
    Song with name and artist
    """
    artist: str
    name: str

    def __str__(self):
        return f'{self.name} — artist {self.artist}'

    def __repr__(self):
        return self.__str__()
