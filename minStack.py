class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.data_min = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.data_min):
            if x <= self.data_min[-1]:
                self.data_min.append(x)
        else:
            self.data_min.append(x)

    def pop(self) -> None:
        if self.data[-1] == self.data_min[-1]:
            self.data_min.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.data_min[-1]