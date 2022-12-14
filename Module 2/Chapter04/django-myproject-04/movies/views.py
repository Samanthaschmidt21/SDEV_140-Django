# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

TOP_MOVIE_LIST = (
    {"rank": 1, "title": "The Shawshank Redemption", "year": 1994, "rating": 9.2},
    {"rank": 2, "title": "The Godfather", "year": 1972, "rating": 9.2},
    {"rank": 3, "title": "The Godfather: Part II", "year": 1974, "rating": 9.0},
    {"rank": 4, "title": "The Dark Knight", "year": 2008, "rating": 8.9},
    {"rank": 5, "title": "Pulp Fiction", "year": 1994, "rating": 8.9},
    {"rank": 6, "title": "The Good, the Bad and the Ugly", "year": 1966, "rating": 8.9},
    {"rank": 7, "title": "Schindler's List", "year": 1993, "rating": 8.9},
    {"rank": 8, "title": "12 Angry Men", "year": 1957, "rating": 8.9},
    {"rank": 9, "title": "The Lord of the Rings: The Return of the King", "year": 2003, "rating": 8.9},
    {"rank": 10, "title": "Fight Club", "year": 1999, "rating": 8.8},
    {"rank": 11, "title": "The Lord of the Rings: The Fellowship of the Ring", "year": 2001, "rating": 8.8},
    {"rank": 12, "title": "Star Wars: Episode V - The Empire Strikes Back", "year": 1980, "rating": 8.8},
    {"rank": 13, "title": "Inception", "year": 2010, "rating": 8.7},
    {"rank": 14, "title": "Forrest Gump", "year": 1994, "rating": 8.7},
    {"rank": 15, "title": "One Flew Over the Cuckoo's Nest", "year": 1975, "rating": 8.7},
    {"rank": 16, "title": "Goodfellas", "year": 1990, "rating": 8.7},
    {"rank": 17, "title": "The Lord of the Rings: The Two Towers", "year": 2002, "rating": 8.7},
    {"rank": 18, "title": "Star Wars: Episode IV - A New Hope", "year": 1977, "rating": 8.7},
    {"rank": 19, "title": "The Matrix", "year": 1999, "rating": 8.7},
    {"rank": 20, "title": "Seven Samurai", "year": 1954, "rating": 8.7},
    {"rank": 21, "title": "City of God", "year": 2002, "rating": 8.7},
    {"rank": 22, "title": "Se7en", "year": 1995, "rating": 8.6},
    {"rank": 23, "title": "The Usual Suspects", "year": 1995, "rating": 8.6},
    {"rank": 24, "title": "The Silence of the Lambs", "year": 1991, "rating": 8.6},
    {"rank": 25, "title": "Once Upon a Time in the West", "year": 1968, "rating": 8.6},
    {"rank": 26, "title": "It's a Wonderful Life", "year": 1946, "rating": 8.6},
    {"rank": 27, "title": "L??on: The Professional", "year": 1994, "rating": 8.6},
    {"rank": 28, "title": "Casablanca", "year": 1942, "rating": 8.6},
    {"rank": 29, "title": "Life Is Beautiful", "year": 1997, "rating": 8.6},
    {"rank": 30, "title": "Raiders of the Lost Ark", "year": 1981, "rating": 8.6},
    {"rank": 31, "title": "Rear Window", "year": 1954, "rating": 8.6},
    {"rank": 32, "title": "Psycho", "year": 1960, "rating": 8.6},
    {"rank": 33, "title": "American History X", "year": 1998, "rating": 8.6},
    {"rank": 34, "title": "City Lights", "year": 1931, "rating": 8.5},
    {"rank": 35, "title": "Saving Private Ryan", "year": 1998, "rating": 8.5},
    {"rank": 36, "title": "Spirited Away", "year": 2001, "rating": 8.5},
    {"rank": 37, "title": "The Intouchables", "year": 2011, "rating": 8.5},
    {"rank": 38, "title": "Memento", "year": 2000, "rating": 8.5},
    {"rank": 39, "title": "Terminator 2: Judgment Day", "year": 1991, "rating": 8.5},
    {"rank": 40, "title": "Modern Times", "year": 1936, "rating": 8.5},
    {"rank": 41, "title": "Sunset Blvd.", "year": 1950, "rating": 8.5},
    {"rank": 42, "title": "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb", "year": 1964, "rating": 8.5},
    {"rank": 43, "title": "Apocalypse Now", "year": 1979, "rating": 8.5},
    {"rank": 44, "title": "Der Pianist", "year": 2002, "rating": 8.5},
    {"rank": 45, "title": "The Green Mile", "year": 1999, "rating": 8.5},
    {"rank": 46, "title": "The Departed", "year": 2006, "rating": 8.5},
    {"rank": 47, "title": "Gladiator", "year": 2000, "rating": 8.5},
    {"rank": 48, "title": "Back to the Future", "year": 1985, "rating": 8.5},
    {"rank": 49, "title": "Alien", "year": 1979, "rating": 8.5},
    {"rank": 50, "title": "The Dark Knight Rises", "year": 2012, "rating": 8.5},
    {"rank": 51, "title": "Django Unchained", "year": 2012, "rating": 8.4},
    {"rank": 52, "title": "The Lives of Others", "year": 2006, "rating": 8.4},
    {"rank": 53, "title": "The Prestige", "year": 2006, "rating": 8.4},
    {"rank": 54, "title": "The Great Dictator", "year": 1940, "rating": 8.4},
    {"rank": 55, "title": "The Shining", "year": 1980, "rating": 8.4},
    {"rank": 56, "title": "Cinema Paradiso", "year": 1988, "rating": 8.4},
    {"rank": 57, "title": "Paths of Glory", "year": 1957, "rating": 8.4},
    {"rank": 58, "title": "American Beauty", "year": 1999, "rating": 8.4},
    {"rank": 59, "title": "The Lion King", "year": 1994, "rating": 8.4},
    {"rank": 60, "title": "WALL??E", "year": 2008, "rating": 8.4},
    {"rank": 61, "title": "North by Northwest", "year": 1959, "rating": 8.4},
    {"rank": 62, "title": "Am??lie", "year": 2001, "rating": 8.4},
    {"rank": 63, "title": "Citizen Kane", "year": 1941, "rating": 8.4},
    {"rank": 64, "title": "Aliens", "year": 1986, "rating": 8.4},
    {"rank": 65, "title": "Toy Story 3", "year": 2010, "rating": 8.4},
    {"rank": 66, "title": "Vertigo", "year": 1958, "rating": 8.4},
    {"rank": 67, "title": "M", "year": 1931, "rating": 8.4},
    {"rank": 68, "title": "Das Boot", "year": 1981, "rating": 8.4},
    {"rank": 69, "title": "Taxi Driver", "year": 1976, "rating": 8.4},
    {"rank": 70, "title": "A Clockwork Orange", "year": 1971, "rating": 8.4},
    {"rank": 71, "title": "Double Indemnity", "year": 1944, "rating": 8.4},
    {"rank": 72, "title": "Oldboy", "year": 2003, "rating": 8.4},
    {"rank": 73, "title": "Princess Mononoke", "year": 1997, "rating": 8.4},
    {"rank": 74, "title": "To Kill a Mockingbird", "year": 1962, "rating": 8.4},
    {"rank": 75, "title": "Reservoir Dogs", "year": 1992, "rating": 8.4},
    {"rank": 76, "title": "Requiem for a Dream", "year": 2000, "rating": 8.4},
    {"rank": 77, "title": "Es war einmal in Amerika", "year": 1984, "rating": 8.4},
    {"rank": 78, "title": "Star Wars: Episode VI - Return of the Jedi", "year": 1983, "rating": 8.4},
    {"rank": 79, "title": "Braveheart", "year": 1995, "rating": 8.4},
    {"rank": 80, "title": "Lawrence of Arabia", "year": 1962, "rating": 8.4},
    {"rank": 81, "title": "Grave of the Fireflies", "year": 1988, "rating": 8.4},
    {"rank": 82, "title": "Eternal Sunshine of the Spotless Mind", "year": 2004, "rating": 8.4},
    {"rank": 83, "title": "Witness for the Prosecution", "year": 1957, "rating": 8.3},
    {"rank": 84, "title": "Full Metal Jacket", "year": 1987, "rating": 8.3},
    {"rank": 85, "title": "Singin' in the Rain", "year": 1952, "rating": 8.3},
    {"rank": 86, "title": "The Sting", "year": 1973, "rating": 8.3},
    {"rank": 87, "title": "Bicycle Thieves", "year": 1948, "rating": 8.3},
    {"rank": 88, "title": "Monty Python and the Holy Grail", "year": 1975, "rating": 8.3},
    {"rank": 89, "title": "Amadeus", "year": 1984, "rating": 8.3},
    {"rank": 90, "title": "All About Eve", "year": 1950, "rating": 8.3},
    {"rank": 91, "title": "Snatch.", "year": 2000, "rating": 8.3},
    {"rank": 92, "title": "Rashomon", "year": 1950, "rating": 8.3},
    {"rank": 93, "title": "The Treasure of the Sierra Madre", "year": 1948, "rating": 8.3},
    {"rank": 94, "title": "L.A. Confidential", "year": 1997, "rating": 8.3},
    {"rank": 95, "title": "The Apartment", "year": 1960, "rating": 8.3},
    {"rank": 96, "title": "Some Like It Hot", "year": 1959, "rating": 8.3},
    {"rank": 97, "title": "The Third Man", "year": 1949, "rating": 8.3},
    {"rank": 98, "title": "For a Few Dollars More", "year": 1965, "rating": 8.3},
    {"rank": 99, "title": "The Wolf of Wall Street", "year": 2013, "rating": 8.3},
    {"rank": 100, "title": "Indiana Jones and the Last Crusade", "year": 1989, "rating": 8.3},
    {"rank": 101, "title": "Nader und Simin - eine Trennung", "year": 2011, "rating": 8.3},
    {"rank": 102, "title": "Inglourious Basterds", "year": 2009, "rating": 8.3},
    {"rank": 103, "title": "The Kid", "year": 1921, "rating": 8.3},
    {"rank": 104, "title": "2001: A Space Odyssey", "year": 1968, "rating": 8.3},
    {"rank": 105, "title": "Batman Begins", "year": 2005, "rating": 8.3},
    {"rank": 106, "title": "Yojimbo", "year": 1961, "rating": 8.3},
    {"rank": 107, "title": "Metropolis", "year": 1927, "rating": 8.3},
    {"rank": 108, "title": "Unforgiven", "year": 1992, "rating": 8.3},
    {"rank": 109, "title": "Raging Bull", "year": 1980, "rating": 8.3},
    {"rank": 110, "title": "Chinatown", "year": 1974, "rating": 8.3},
    {"rank": 111, "title": "Toy Story", "year": 1995, "rating": 8.3},
    {"rank": 112, "title": "Scarface", "year": 1983, "rating": 8.3},
    {"rank": 113, "title": "Up", "year": 2009, "rating": 8.3},
    {"rank": 114, "title": "Die Hard", "year": 1988, "rating": 8.3},
    {"rank": 115, "title": "Downfall", "year": 2004, "rating": 8.3},
    {"rank": 116, "title": "Mr. Smith Goes to Washington", "year": 1939, "rating": 8.2},
    {"rank": 117, "title": "The Great Escape", "year": 1963, "rating": 8.2},
    {"rank": 118, "title": "Pans Labyrinth", "year": 2006, "rating": 8.2},
    {"rank": 119, "title": "On the Waterfront", "year": 1954, "rating": 8.2},
    {"rank": 120, "title": "Like Stars on Earth", "year": 2007, "rating": 8.2},
    {"rank": 121, "title": "The Bridge on the River Kwai", "year": 1957, "rating": 8.2},
    {"rank": 122, "title": "Heat", "year": 1995, "rating": 8.2},
    {"rank": 123, "title": "3 Idiots", "year": 2009, "rating": 8.2},
    {"rank": 124, "title": "The Hunt", "year": 2012, "rating": 8.2},
    {"rank": 125, "title": "The Seventh Seal", "year": 1957, "rating": 8.2},
    {"rank": 126, "title": "Wild Strawberries", "year": 1957, "rating": 8.2},
    {"rank": 127, "title": "The Grand Budapest Hotel", "year": 2014, "rating": 8.2},
    {"rank": 128, "title": "Ikiru - Einmal richtig leben", "year": 1952, "rating": 8.2},
    {"rank": 129, "title": "The Elephant Man", "year": 1980, "rating": 8.2},
    {"rank": 130, "title": "The General", "year": 1926, "rating": 8.2},
    {"rank": 131, "title": "Ran", "year": 1985, "rating": 8.2},
    {"rank": 132, "title": "My Neighbor Totoro", "year": 1988, "rating": 8.2},
    {"rank": 133, "title": "The Gold Rush", "year": 1925, "rating": 8.2},
    {"rank": 134, "title": "Blade Runner", "year": 1982, "rating": 8.2},
    {"rank": 135, "title": "Lock, Stock and Two Smoking Barrels", "year": 1998, "rating": 8.2},
    {"rank": 136, "title": "Gran Torino", "year": 2008, "rating": 8.2},
    {"rank": 137, "title": "Good Will Hunting", "year": 1997, "rating": 8.2},
    {"rank": 138, "title": "12 Years a Slave", "year": 2013, "rating": 8.2},
    {"rank": 139, "title": "Rebecca", "year": 1940, "rating": 8.2},
    {"rank": 140, "title": "The Big Lebowski", "year": 1998, "rating": 8.2},
    {"rank": 141, "title": "The Secret in Their Eyes", "year": 2009, "rating": 8.2},
    {"rank": 142, "title": "It Happened One Night", "year": 1934, "rating": 8.2},
    {"rank": 143, "title": "Rush", "year": 2013, "rating": 8.2},
    {"rank": 144, "title": "Warrior", "year": 2011, "rating": 8.2},
    {"rank": 145, "title": "Casino", "year": 1995, "rating": 8.2},
    {"rank": 146, "title": "Rang De Basanti", "year": 2006, "rating": 8.2},
    {"rank": 147, "title": "V for Vendetta", "year": 2005, "rating": 8.2},
    {"rank": 148, "title": "The Deer Hunter", "year": 1978, "rating": 8.2},
    {"rank": 149, "title": "Cool Hand Luke", "year": 1967, "rating": 8.2},
    {"rank": 150, "title": "The Maltese Falcon", "year": 1941, "rating": 8.2},
    {"rank": 151, "title": "Fargo", "year": 1996, "rating": 8.2},
    {"rank": 152, "title": "Her", "year": 2013, "rating": 8.2},
    {"rank": 153, "title": "Gone with the Wind", "year": 1939, "rating": 8.2},
    {"rank": 154, "title": "Trainspotting", "year": 1996, "rating": 8.2},
    {"rank": 155, "title": "Howl's Moving Castle", "year": 2004, "rating": 8.2},
    {"rank": 156, "title": "Into the Wild", "year": 2007, "rating": 8.2},
    {"rank": 157, "title": "How to Train Your Dragon", "year": 2010, "rating": 8.1},
    {"rank": 158, "title": "Hotel Rwanda", "year": 2004, "rating": 8.1},
    {"rank": 159, "title": "The Sixth Sense", "year": 1999, "rating": 8.1},
    {"rank": 160, "title": "Judgment at Nuremberg", "year": 1961, "rating": 8.1},
    {"rank": 161, "title": "Butch Cassidy and the Sundance Kid", "year": 1969, "rating": 8.1},
    {"rank": 162, "title": "The Thing", "year": 1982, "rating": 8.1},
    {"rank": 163, "title": "Dial M for Murder", "year": 1954, "rating": 8.1},
    {"rank": 164, "title": "Annie Hall", "year": 1977, "rating": 8.1},
    {"rank": 165, "title": "A Beautiful Mind", "year": 2001, "rating": 8.1},
    {"rank": 166, "title": "Platoon", "year": 1986, "rating": 8.1},
    {"rank": 167, "title": "Kill Bill: Vol. 1", "year": 2003, "rating": 8.1},
    {"rank": 168, "title": "No Country for Old Men", "year": 2007, "rating": 8.1},
    {"rank": 169, "title": "Sin City", "year": 2005, "rating": 8.1},
    {"rank": 170, "title": "Mary & Max, oder - Schrumpfen Schafe, wenn es regnet", "year": 2009, "rating": 8.1},
    {"rank": 171, "title": "Finding Nemo", "year": 2003, "rating": 8.1},
    {"rank": 172, "title": "Touch of Evil", "year": 1958, "rating": 8.1},
    {"rank": 173, "title": "Diabolique", "year": 1955, "rating": 8.1},
    {"rank": 174, "title": "Life of Brian", "year": 1979, "rating": 8.1},
    {"rank": 175, "title": "Network", "year": 1976, "rating": 8.1},
    {"rank": 176, "title": "The Princess Bride", "year": 1987, "rating": 8.1},
    {"rank": 177, "title": "Amores Perros", "year": 2000, "rating": 8.1},
    {"rank": 178, "title": "The Wizard of Oz", "year": 1939, "rating": 8.1},
    {"rank": 179, "title": "Stand by Me", "year": 1986, "rating": 8.1},
    {"rank": 180, "title": "The Avengers", "year": 2012, "rating": 8.1},
    {"rank": 181, "title": "Ben-Hur", "year": 1959, "rating": 8.1},
    {"rank": 182, "title": "The Grapes of Wrath", "year": 1940, "rating": 8.1},
    {"rank": 183, "title": "Die Frau die singt - Incendies", "year": 2010, "rating": 8.1},
    {"rank": 184, "title": "There Will Be Blood", "year": 2007, "rating": 8.1},
    {"rank": 185, "title": "The Best Years of Our Lives", "year": 1946, "rating": 8.1},
    {"rank": 186, "title": "The 400 Blows", "year": 1959, "rating": 8.1},
    {"rank": 187, "title": "Million Dollar Baby", "year": 2004, "rating": 8.1},
    {"rank": 188, "title": "Hachi: A Dog's Tale", "year": 2009, "rating": 8.1},
    {"rank": 189, "title": "8??", "year": 1963, "rating": 8.1},
    {"rank": 190, "title": "Lego", "year": 2014, "rating": 8.1},
    {"rank": 191, "title": "Donnie Darko", "year": 2001, "rating": 8.1},
    {"rank": 192, "title": "The Bourne Ultimatum", "year": 2007, "rating": 8.1},
    {"rank": 193, "title": "Im Namen des Vaters", "year": 1993, "rating": 8.1},
    {"rank": 194, "title": "Strangers on a Train", "year": 1951, "rating": 8.1},
    {"rank": 195, "title": "Captain America: The Winter Soldier", "year": 2014, "rating": 8.1},
    {"rank": 196, "title": "High Noon", "year": 1952, "rating": 8.1},
    {"rank": 197, "title": "Persona", "year": 1966, "rating": 8.1},
    {"rank": 198, "title": "Gandhi", "year": 1982, "rating": 8.1},
    {"rank": 199, "title": "Notorious", "year": 1946, "rating": 8.1},
    {"rank": 200, "title": "The King's Speech", "year": 2010, "rating": 8.1},
    {"rank": 201, "title": "Infernal Affairs", "year": 2002, "rating": 8.1},
    {"rank": 202, "title": "Jaws", "year": 1975, "rating": 8.1},
    {"rank": 203, "title": "Gravity", "year": 2013, "rating": 8.1},
    {"rank": 204, "title": "Nausica?? of the Valley of the Wind", "year": 1984, "rating": 8.1},
    {"rank": 205, "title": "Twelve Monkeys", "year": 1995, "rating": 8.1},
    {"rank": 206, "title": "Lagaan: Once Upon a Time in India", "year": 2001, "rating": 8.1},
    {"rank": 207, "title": "Fanny and Alexander", "year": 1982, "rating": 8.1},
    {"rank": 208, "title": "La Strada", "year": 1954, "rating": 8.0},
    {"rank": 209, "title": "The Terminator", "year": 1984, "rating": 8.0},
    {"rank": 210, "title": "Ip Man", "year": 2008, "rating": 8.0},
    {"rank": 211, "title": "The Night of the Hunter", "year": 1955, "rating": 8.0},
    {"rank": 212, "title": "Stalker", "year": 1979, "rating": 8.0},
    {"rank": 213, "title": "Groundhog Day", "year": 1993, "rating": 8.0},
    {"rank": 214, "title": "Who's Afraid of Virginia Woolf?", "year": 1966, "rating": 8.0},
    {"rank": 215, "title": "The Big Sleep", "year": 1946, "rating": 8.0},
    {"rank": 216, "title": "Dog Day Afternoon", "year": 1975, "rating": 8.0},
    {"rank": 217, "title": "Rocky", "year": 1976, "rating": 8.0},
    {"rank": 218, "title": "Harry Potter and the Deathly Hallows: Part 2", "year": 2011, "rating": 8.0},
    {"rank": 219, "title": "The Battle of Algiers", "year": 1966, "rating": 8.0},
    {"rank": 220, "title": "La Haine", "year": 1995, "rating": 8.0},
    {"rank": 221, "title": "Barry Lyndon", "year": 1975, "rating": 8.0},
    {"rank": 222, "title": "Pis of the Caribbean: The Curse of the Black Pearl", "year": 2003, "rating": 8.0},
    {"rank": 223, "title": "Shutter Island", "year": 2010, "rating": 8.0},
    {"rank": 224, "title": "Before Sunrise", "year": 1995, "rating": 8.0},
    {"rank": 225, "title": "The Graduate", "year": 1967, "rating": 8.0},
    {"rank": 226, "title": "The Celebration", "year": 1998, "rating": 8.0},
    {"rank": 227, "title": "Monsters, Inc.", "year": 2001, "rating": 8.0},
    {"rank": 228, "title": "The Hustler", "year": 1961, "rating": 8.0},
    {"rank": 229, "title": "Swades", "year": 2004, "rating": 8.0},
    {"rank": 230, "title": "Castle in the Sky", "year": 1986, "rating": 8.0},
    {"rank": 231, "title": "Memories of Murder", "year": 2003, "rating": 8.0},
    {"rank": 232, "title": "Roman Holiday", "year": 1953, "rating": 8.0},
    {"rank": 233, "title": "A Christmas Story", "year": 1983, "rating": 8.0},
    {"rank": 234, "title": "Underground", "year": 1995, "rating": 8.0},
    {"rank": 235, "title": "In the Mood for Love", "year": 2000, "rating": 8.0},
    {"rank": 236, "title": "Stalag 17", "year": 1953, "rating": 8.0},
    {"rank": 237, "title": "F??r eine Handvoll Dollar", "year": 1964, "rating": 8.0},
    {"rank": 238, "title": "The Help", "year": 2011, "rating": 8.0},
    {"rank": 239, "title": "Slumdog Millionaire", "year": 2008, "rating": 8.0},
    {"rank": 240, "title": "The Killing", "year": 1956, "rating": 8.0},
    {"rank": 241, "title": "Rope", "year": 1948, "rating": 8.0},
    {"rank": 242, "title": "Elite Squad: The Enemy Within", "year": 2010, "rating": 8.0},
    {"rank": 243, "title": "The Truman Show", "year": 1998, "rating": 8.0},
    {"rank": 244, "title": "Black Swan", "year": 2010, "rating": 8.0},
    {"rank": 245, "title": "Three Colors: Red", "year": 1994, "rating": 8.0},
    {"rank": 246, "title": "Beauty and the Beast", "year": 1991, "rating": 8.0},
    {"rank": 247, "title": "The Diving Bell and the Butterfly", "year": 2007, "rating": 8.0},
    {"rank": 248, "title": "The Hobbit: The Desolation of Smaug", "year": 2013, "rating": 8.0},
    {"rank": 249, "title": "La Dolce Vita", "year": 1960, "rating": 8.0},
    {"rank": 250, "title": "Jurassic Park", "year": 1993, "rating": 8.0},
)


def movie_list(request):
    paginator = Paginator(TOP_MOVIE_LIST, 25)

    page_number = request.GET.get("page")
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, show first page.
        page = paginator.page(1)
    except EmptyPage:
        # If page is out of range, show last existing page.
        page = paginator.page(paginator.num_pages)

    context = {
        "object_list": page,
    }
    return render(request, "movies/movie_list.html", context)
