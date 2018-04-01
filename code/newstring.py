class LanguageString(str):

    def __new__(cls, value, lang='en'):
        obj = str.__new__(cls, value)
        obj.lang = lang
        return obj
