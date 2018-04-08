class Example(object):

    def __enter__(self):
        print('Calling Enter')
        return 73

    def __exit__(self, exc_type, exc_value, traceback):
        print('Calling Exit: %s, %s, %s' % (exc_type, exc_value, traceback))
        # This will stop the exception
        # from being propagated
        return True
