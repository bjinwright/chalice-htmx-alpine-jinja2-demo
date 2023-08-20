import math


class Page(object):
    """
    A class to represent a page of records. This is used to paginate records.
    It is not what I would use in production, but it is a good example of
    how to use paginate for this exercise.
    """

    def __init__(self, current_page: int, records: list, per_page: int = 10):
        self.current_page = current_page
        self.records = records
        self.total_records = len(records)
        self.per_page = per_page
        self.total_pages = self.get_total_pages()
        self.page_range = self.get_page_range()
        self.has_next = self.get_has_next()
        self.has_previous = self.get_has_previous()
        self.next_page_number = self.get_next_page_number()
        self.previous_page_number = self.get_previous_page_number()
        self.page = self.get_page()

    def __str__(self):
        return f'Page {self.current_page} of {self.total_pages}'

    def get_page(self) -> list:
        """
        Get the page of records
        :return: list
        """
        start = (self.current_page - 1) * self.per_page
        end = start + self.per_page
        return self.records[start:end]

    def get_total_pages(self) -> int:
        """
        Get the total number of pages
        :return: int
        """
        return math.ceil(self.total_records / self.per_page)

    def get_page_range(self) -> range:
        """
        Get the range of pages
        :return: range
        """
        return range(1, self.total_pages + 1)

    def get_has_next(self) -> bool:
        """
        Check if there is a next page
        :return: bool
        """
        return self.current_page < self.total_pages

    def get_has_previous(self) -> bool:
        """
        Check if there is a previous page
        :return: bool
        """
        return self.current_page > 1

    def get_next_page_number(self) -> int:
        """
        Get the next page number
        :return: int
        """
        if self.has_next:
            return self.current_page + 1
        return None

    def get_previous_page_number(self) -> int:
        """
        Get the previous page number
        :return: int
        """
        if self.has_previous:
            return self.current_page - 1
        return None
