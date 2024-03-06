"""ingesting strategy for text files."""

from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface


class TextIngestor(IngestorInterface):
    """text files ingestor class."""

    @classmethod
    def parse(cls, path):
        """Parse text file.

        :param path: the location of the text file
        :return: list of parsed quotes
        """
        with open(path, "r") as file:
            lines = file.readlines()

        return [QuoteModel(*quote.rstrip("\n").split(" - "))
                for quote in lines]
