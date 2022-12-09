import pickle

"""
Helper function to create the initial dictionary 
that can be used to create a leaderboards.data file to
append to when users win the game
"""

d = {
    12: "Chase",
    10: "Professor Bagley"
}
newFile = 'leaderboards.data' 
with open(newFile, 'wb') as f:
    pickle.dump(d, f)
