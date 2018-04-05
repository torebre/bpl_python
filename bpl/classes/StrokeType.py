

class StrokeType:

    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, newValue):
        self._R = newValue

    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, newValue):
        self._ids = newValue

    @property
    def invscales(self):
        return self._invscales

    @invscales.setter
    def invscales(self, newValue):
        self._invscales = newValue

    @property
    def shapes_type(self):
        return self._shapes_type

    @shapes_type.setter
    def shapes_type(self, newValue):
        self._shapes_type = newValue
