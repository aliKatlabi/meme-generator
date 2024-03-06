"""ingesting strategy for docx files."""

from docx import Document
from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """docx files ingestor class."""

    @classmethod
    def parse(cls, path):
        """Parse docx file.

        :param path: the location of the docx file
        :return: list of parsed quotes
        """
        try:
            document = Document(path)
        except ValueError as ve:
            print(ve)

        quotes = []
        for paragraph in document.paragraphs:
            paragraph.text and quotes.append(
                QuoteModel(*paragraph.text.split(" - ")))
        return quotes
