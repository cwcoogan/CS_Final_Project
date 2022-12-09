import pickle

d = {
    12: "Chase",
    10: "Professor Bagley"
}
newFile = 'leaderboards.data' 
with open(newFile, 'wb') as f:
    pickle.dump(d, f)
