"""The ingestor strategy context."""

from QuoteEngine.ingestor_interface import IngestorInterface, extensions
from .text_ingestor import TextIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .csv_ingestor import CSVIngestor
import os


class Ingestor(IngestorInterface):
    """The ingestor class."""

    @classmethod
    def parse(cls, path):
        """Apply the appropriate ingestor based on file extention.

        :param path: the location of the file
        :return: list of parsed quotes
        """
        _, file_extension = os.path.splitext(path)
        if not cls.can_ingest(file_extension):
            raise ValueError("Unsupported file extension:",
                             file_extension)
        if file_extension == extensions.get("TEXT"):
            return TextIngestor.parse(path)
        if file_extension == extensions.get("DOCX"):
            return DocxIngestor.parse(path)
        if file_extension == extensions.get("PDF"):
            return PDFIngestor.parse(path)
        if file_extension == extensions.get("CSV"):
            return CSVIngestor.parse(path)
