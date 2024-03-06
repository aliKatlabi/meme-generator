"""ingesting strategy for pdf files."""

import subprocess
from .quote_model import QuoteModel
from .ingestor_interface import IngestorInterface
from .text_ingestor import TextIngestor
from tempfile import NamedTemporaryFile


class PDFIngestor(IngestorInterface):
    """pdf files ingestor class."""

    @classmethod
    def parse(cls, path):
        """Parse pdf file.

        :param path: the location of the pdf file
        :return: list of parsed quotes
        """
        tmp = NamedTemporaryFile(delete=False)
        try:
            # call pdftotext via subprocess
            cmd = f"./pdftotext -layout -nopgbrk {path} {tmp}"
            subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
            quotes = TextIngestor.parse(tmp.name)

            return quotes

        except FileNotFoundError as error_out:
            print(error_out)

        finally:
            tmp.close()
