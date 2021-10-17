import logging

faker_logger = logging.getLogger("faker.factory")
faker_logger.setLevel("INFO")

pytest_plugins = ["tests.http_protocol.fixtures"]


class AsyncIterator:
    def __init__(self, seq):
        self.iter = iter(seq)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.iter)
        except StopIteration:
            raise StopAsyncIteration
