class FrameDivider:
    def __init__(self):
        self.width = None

    def divide_frame(self, frame):
        height, width = frame.shape[:2]
        self.width = width // 2
        left_half = frame[:, :self.width]
        right_half = frame[:, self.width:]
        return left_half, right_half
