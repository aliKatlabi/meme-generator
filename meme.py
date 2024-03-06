"""app meme generator."""

import argparse
import os
import random

from meme.meme_engine import MemeEngine
from QuoteEngine.ingestor import Ingestor
from QuoteEngine.quote_model import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote.

    :param path: mame image path or default from photos/dog
    :param body: meme body or default from Dog Quiotes
    :param author: author
    :return: path of the outputed meme
    """
    image, quote = None, None

    if path is None:
        images_path = "./_data/photos/dog/"
        images = []
        for root, _, files in os.walk(images_path):
            images = [os.path.join(root, name) for name in files]

        image = random.choice(images)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            "./_data/DogQuotes/DogQuotesTXT.txt",
            "./_data/DogQuotes/DogQuotesDOCX.docx",
            "./_data/DogQuotes/DogQuotesPDF.pdf",
            "./_data/DogQuotes/DogQuotesCSV.csv",]

        quotes = []
        for f in quote_files:
            quote = Ingestor.parse(f)
            print(quote)
            quotes.extend(quote)

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("Author Required if Body is Used")
        quote = QuoteModel(body, author)

    meme = MemeEngine("./tmp")
    path = meme.make_meme(image, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="MemeGenerator",
        description="let's get some Dog memes with fun quotes."
    )

    parser.add_argument("-a", "--author",
                        help="Quote author to add to the image", type=str)
    parser.add_argument("-p", "--path",
                        help="Path to image file", type=str)
    parser.add_argument("-b", "--body",
                        help="Quote body to add to the image", type=str)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
