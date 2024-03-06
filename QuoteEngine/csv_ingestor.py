"""ingesting strategy for csv files."""


import pandas as pd
from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """CSV files ingestor class."""

    @classmethod
    def parse(cls, path):
        """Parse csv file.

        :param path: the location of the csv file
        :return: list of parsed quotes
        """
        csv = pd.read_csv(path)
        return [QuoteModel(**row) for index, row in csv.iterrows()]
