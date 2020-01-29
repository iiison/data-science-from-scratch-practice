class CountingClicker:
    """Door Clicker, that implements the same behaviour as a physical clickers in the malls."""

    def __init__(self, count=0):
        """Initializes the clicker counter from 0"""
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self):
        """Increses the count by 1 as normal clicker does."""
        self.count += 1

    def read(self):
        """Returns the clicker count."""
        return self.count

    def reset(self):
        """Resets the clicker count to 0"""
        self.count = 0

CLICKER = CountingClicker()
assert CLICKER.read() == 0

CLICKER.click()
assert CLICKER.read() == 1

CLICKER.reset()
assert CLICKER.read() == 0


class CustomCountCliker(CountingClicker):
    """This one accepts a nubmer in clicker function"""

    def click(self, times=1):
        """This cliker accepts times"""
        self.count += times

CUSTOM_CLICKER = CustomCountCliker()
assert CUSTOM_CLICKER.read() == 0

CUSTOM_CLICKER.click()
assert CUSTOM_CLICKER.read() == 1

CUSTOM_CLICKER.click(times=2)
assert CUSTOM_CLICKER.read() == 3
