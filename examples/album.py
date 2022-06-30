def make_album(artist,album,number_of_songs=None):
	music_album = {'Artist':artist,'Album':album}
	if number_of_songs:
		music_album['Number of Songs'] = number_of_songs	
	return(music_album)

answer = True
while answer:
	prompt = "Would you like to add a new artist to the list? (yes/no)"
	answer = input(prompt)

	if answer == 'yes':
		artist_name = input("What is the artist's name?")
		album_name = input("What is the album's name?")
		artist_to_add = make_album(artist_name,album_name)
		print(artist_to_add)
	else:
		answer = False