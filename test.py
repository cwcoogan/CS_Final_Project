import pickle

d = {
    12: "Harry",
    10: "Hary"
}
newFile = 'leaderboards.data' 
with open(newFile, 'wb') as f:
    pickle.dump(d, f)
