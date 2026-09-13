import pandas as pd

# PART 1 - Create a pandas series of top player scores
print('--- PART 1. Pandas series ---')
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores,index=['NightWolf', 'StarBlaze', 'PixelKing', 'Cyberfox', 'IronStorms'])
print(players)


print()
print('--- PART 2: Pandas DataFrame ---')
data = {
    'Player':['NightWolf', 'StarBlaze', 'PixelKing', 'Cyberfox', 'IronStorms'],
    'Level': [42, 38, 35, 30, 27],
    'Score': [98500, 87200, 76400, 65100, 54800],
    'Wins': [210, 185, 162, 140, 118]
}
df = pd.DataFrame(data)
print(df)
"Datatype"= 'dtype'
