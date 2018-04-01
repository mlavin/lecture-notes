class Borg(object):

    _state = {}

    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls, *args, **kwargs)
        # override instance namespace with shared state
        self.__dict__ = cls._state
        return self
