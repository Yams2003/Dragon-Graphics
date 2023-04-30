# Dragon-Graphics
Our project from the 2023 DragonHacks Hackathon

## Notes
This project is **INCOMPLETE**. We were short on time and we had other responsibilities and homework assignments to finish the hackathon. The original intent of the project was to create a small art tool kit that would come along with a guide or tutorial that explains what the computer is doing at a lower level while performing these actions. This was meant to be a project to demonstrate a very introductory level of computer graphics to someone with no prior knowledge in CS. Instead we were only able to finish the minimal paint tools before even getting to the instructional part.

## Had we more time...
We were planning on impelementing an instructional component that explains the functionality of each tool in the paint program. Here are some of the original plans we had intended for this project to contain:
* explaination of how a computer's screen is essentially a grid of pixels that get assigned an RGB value to display color
* line tool to explain Bresenham's Algorith 
* rotational tool to demonstrate a matrix multiplication between the image's pixel coordinates and a rotation matrix to compute the new coordinates of each pixel after the rotation
* selection tool to show a translation transformation on coordinates to move the selected pixels to a new location
* fill bucket tool that highlights the algorithms of Breadth-First Search and Depth-First Search
* a walkthrough tutorial that allows users to step through and back and visit each of the concepts


## Setup

1. Clone this repository.

2. Install the requirements:

   ```bash
   $ pip3 install pygame
   ```
3. That's it! Just run the program and an instance of pygame should open

## Instructions
You can select any of the buttons to draw right in the canvas. As of right now, if you want to change the features like pixel size, FPS, or background color, you should check the settings.py in the utils package. If you want to change a color you can press the "c" key or the colored button to open a prompt in the terminal for rgb values. You can also use "q" and "e" to undo and redo changes.
