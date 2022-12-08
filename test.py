import pickle

newFile = 'leaderboards.data' 
with open(newFile, 'rb') as f:
    leaderboard_name = pickle.load(f)
    print(leaderboard_name)