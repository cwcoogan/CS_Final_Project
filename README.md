# 15 Piece Sliding Puzzle Game :arrow_forward:
The 15 peice sliding puzzle game takes a shuffled image and gives the user however
many attempts they decide to unshuffle and display the image in its correct format.
Try and get your name on the leaderboard! 

## **How to play:**
1. Clone the repository and open the parent folder
2. run game using puzzle_game.py
3. IF leaderboard.data error occurs (or is not found) -> RUN the build_leaderboards_file.py 
file to generate a leaderboards.data file THEN run the game
4. Have fun! 


## **How to create your own puzzle images**
1. Split your image into 4x4 (16 total images)
2. Convert images to GIFs
3. format thumbnail size 98x98
4. format individual split images into 98x98 
5. Remove 1 of the images and add a blank.gif image from any sub-folder

## **links to help create image**
1. Image Splitter: [image splitter](https://postcron.com/image-splitter/en/)
2. JPG -> GIF convert: [GIF Converter](https://www.iloveimg.com/)
3. Img resizer: [Img Resizer](https://www.iloveimg.com/)


## **Design Structure**
This game is fully built on Python and utilizes Turtles library to display the UI.
Additional modules include; Pickle, Functools, Math, Partial, Time, and many more.
