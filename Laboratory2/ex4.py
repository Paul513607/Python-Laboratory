def compose_song(notes, positions, starting_position):
    song = [notes[starting_position]]
    for pos in positions:
        starting_position += pos
        if starting_position >= len(notes):
            starting_position -= len(notes)
        song.append(notes[starting_position])
    return song
