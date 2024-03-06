"""The ingestor strategy interface."""

from abc import ABC, abstractmethod
from typing import List
from QuoteEngine.quote_model import QuoteModel

extensions = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx",
}


class IngestorInterface(ABC):
    """acstract ingester class."""

    file_extensions = extensions

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check whether quote file is ingestable.

        :param path: the location of the file including quotes
        :return: boolean statement on whether file extention is ingestable
        """
        file_extension = '.'+path.split(".")[-1]
        return file_extension in extensions.values()

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file content (i.e., splitting each row)
        and outputting it to a Quote object.

        :param path: the location of the file including quotes
        :return: list of parsed quotes
        """
        pass
