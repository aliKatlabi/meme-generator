"""The image generating step of the meme."""

from abc import abstractmethod
from math import ceil
import os
import random
import textwrap
from tkinter import font
from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """class handles generating meme based on ingested text and image."""

    def __init__(self, output_dir):
        """Save and create the output directory path."""
        self.output_dir = output_dir
        self.count = 1
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    @abstractmethod
    def draw_text_on_img(image, text, author, text_position, style):
        """Draw text on image."""
        draw = ImageDraw.Draw(image)
        wrapper = textwrap.TextWrapper(width=40)
        text_list = wrapper.fill(text=text)
        author_position = 27 * text_list.split('\n').__len__()

        draw.text((30, text_position), text_list,
                  style["fill"], style["font1"],
                  stroke_width=1, stroke_fill=style["stroke_fill"])
        draw.text((40, text_position + author_position), f"- {author}",
                  style["fill"], style["font2"],
                  stroke_width=1, stroke_fill=style["stroke_fill"])

    def make_meme(self, image_path, text, author, width=500):
        """Create a meme.

        :param image_path   : the image path used to create the meme
        :param text         : the text used to create the meme
        :param author       : the author used to create the meme

        :return: meme image file
        """

        try:
            image = Image.open(image_path)
        except FileNotFoundError as e:
            print(image_path, ": not_found")
        except Exception as e:
            print(e)

        outfile = os.path.join(self.output_dir, f"temp-{self.count}.jpg")
        self.count += 1
        real_width, real_height = image.size
        height = int(real_height * width / real_width)
        image.thumbnail((width, height))

        # Prepare style

        font1 = ImageFont.truetype("./_data/Fonts/Roboto-Bold.ttf", 22)
        font2 = ImageFont.truetype("./_data/Fonts/Roboto-Medium.ttf", 18)
        text_position = random.choice(range(30, height - 50))
        fill = (0, 0, 0)
        stroke_fill = (255, 255, 255)

        style = {"font1": font1, "font2": font2, "fill": fill,
                 "stroke_fill": stroke_fill}

        MemeEngine.draw_text_on_img(image, text, author, text_position, style)

        try:
            image.save(outfile, "JPEG")
        except Exception as e:
            print(e)

        return outfile
