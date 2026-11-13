import pandas as pd

marvel_year = {
'Spider-Man: No Way Home': 2021,
'Black Panther: Wakanda Forever': 2022,
'Guardians of the Galaxy Vol. 3': 2023,
'Deadpool & Wolverine': 2024,
'Captain America: Brave New World': 2025
}
s = pd.Series(marvel_year)

print(s)
s.index