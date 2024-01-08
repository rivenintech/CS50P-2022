# Motivational Quotes Image Generator

## Video Demo: <https://youtu.be/BjWlf1HjCrY>

### Motivational Quotes Image Generator - a small app that creates images with motivational quotes

#### How does it work?

1. First, we have to get the background image. To do it I used Pexels API to fetch images. By using the `download_background()` and `get_backgrounds()` functions we can get one random picture with a matching query. I decided to go with **"nature"**.
2. After getting the background image we have to edit it. By using `edit_background()` we can resize the background and make it darker to avoid blending the image and text.
3. Now it's time to get the quote and its author. A while ago, when I first thought about this project, I found an open-source repository with a CSV file containing quotes (assets/quotes.csv). Now we have to get a random one with the `get_quote()` function.
4. We have the quote and the background image. Let's add them together. To achieve this I used the Pillow library to write the quote on the background image.

#### File structure explained

- **assets/** - contains "quotes.csv" (file where all quotes are stored), "lato.ttf" (font used for quote's text generation)
- **results/** - this is where all the final created images are stored
- **img_utils.py** - there is an "ImageText" class that contains methods used to place the quote in the correct place on the image
- **project.py** - project's main file
- **test_project.py** - tests used to check if code would run properly
- **requirements.txt** - all pip packages that are necessary to run the code

It was a fun project. I wanted to create it even before CS50P, but I abandoned it shortly after finding quotes.csv on GitHub. After completing the course I decided that it was a perfect final project :D
