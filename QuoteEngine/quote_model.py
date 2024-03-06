"""The quote model calss."""


class QuoteModel:
    """The quote model calss."""

    def __init__(self, body="", author=""):
        """Initiate the quote model."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Print the value stored in this model in a human readable format."""
        return f"{self.body} - {self.author}"
