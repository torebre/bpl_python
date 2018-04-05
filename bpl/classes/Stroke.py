


class Stroke:

    def __init__(self, previousStroke):
        self.refresh_listener()

        if previousStroke is None:
            self.myType = previousStroke.myType
        else:
            self.myType = StrokeType()



