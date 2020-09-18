class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.stack = [homepage]
        self.idx = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if self.idx != len(self.stack) - 1:
            self.stack = self.stack[:self.idx + 1]
        self.stack.append(url)
        self.idx += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.idx = max(self.idx - steps, 0)
        return self.stack[self.idx]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.idx = min(self.idx + steps, len(self.stack) - 1)
        return self.stack[self.idx]
