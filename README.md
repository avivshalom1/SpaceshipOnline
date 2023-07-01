# Spaceship Game

## Game Overview 
This is a simple spaceship game built using the Pygame library. The objective of the game is to control a spaceship and shoot down aliens while avoiding collisions. Your score increases for every alien you successfully destroy.

## How to Run

install from command line:
```
sudo apt install docker
sudo docker pull ghcr.io/avivshalom1/spaceship/spaceship:latest
```

run this command:
```
xhost +local:docker
```
and than run the game:
```
sudo docker run --rm -it --volume /tmp/.X11-unix:/tmp/.X11-unix --env DISPLAY=$DISPLAY ghcr.io/avivshalom1/spaceship/spaceship:latest
```

## How to Play
 * Enter your name in the provided input box.
 * Press Enter to start the game.
 * Use the arrow keys to control the spaceship.
 * Press the spacebar to shoot bullets.
 * Avoid collisions with the aliens and try to achieve the highest score possible.
 * Your score will increase for every alien you destroy.
 * The game ends if your spaceship collides with an alien.
 * The game will display the top 5 scores and player names from the database.

## Game Controls

 * Arrow Up: Move the spaceship forward.
 * Arrow Down: Slow down the spaceship.
 * Arrow Left: Rotate the spaceship left.
 * Arrow Right: Rotate the spaceship right.
 * Spacebar: Shoot bullets.
 * Escape: Quit the game.


Enjoy playing the spaceship game!
