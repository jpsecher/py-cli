import sys
import traceback
from constants import SUCCESS, EXCEPTION
from app import App


def full_stack() -> str:
    exc = sys.exc_info()[0]
    # Remove call to this function.
    stack = traceback.extract_stack()[:-1]
    if exc is not None:  # An exception is present
        del stack[-1]
    trc = 'Traceback (most recent call last):\n'
    stackstr = trc + ''.join(traceback.format_list(stack))
    if exc is not None:
        stackstr += '  ' + traceback.format_exc().lstrip(trc)
    return stackstr


if __name__ == '__main__':
    try:
        app = App(sys.argv[1:])
        app.set_up_log()
        app.run()
        app.epilog()
        sys.exit(SUCCESS)
    except Exception as error:
        print(full_stack())
        print(f'Error: {error}')
        sys.exit(EXCEPTION)
