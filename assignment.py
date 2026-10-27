# Exercise 1 
class BusCard:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.trips = 0

    def top_up(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def pay(self, fare):
        if fare > self.balance:
            return False
        self.balance -= fare
        self.trips += 1
        return True


# Exercise 2
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = [] 

    def add_grade(self, score):
        if 0 <= score <= 100:
            self.grades.append(score)
            return True
        return False

    def average(self):
        if not self.grades:
            return 0
        return round(sum(self.grades) / len(self.grades), 1)

    def highest(self):
        if not self.grades:
            return None
        return max(self.grades)


# Exercise 3
class Song:
    def __init__(self, title, artist, seconds):
        self.title = title
        self.artist = artist
        self.seconds = seconds

    def length(self):
        minutes = self.seconds // 60
        secs = self.seconds % 60
        return f"{minutes}:{secs:02d}"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def count(self):
        return len(self.songs)

    def total_seconds(self):
        return sum(song.seconds for song in self.songs)

    def longest_song(self):
        if not self.songs:
            return None
        longest = self.songs[0]
        for song in self.songs[1:]:
            if song.seconds > longest.seconds:
                longest = song
        return longest

    def songs_by(self, artist):
        return [song.title for song in self.songs if song.artist == artist]
