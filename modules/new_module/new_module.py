
from models import custom_modules

from . import handlers


def register_module():
    """Registers this module in the registry."""

    global_urls = [
        ('/new-global-url', handlers.NewURLHandler)  # Global URLs go on mycourse.appspot.com/url
    ]
    course_urls = [
        ('/new-course-url', handlers.NewURLHandler)
    ]    # Course URLs go on mycourse.appspot.com/course-name/url

    global custom_module
    custom_module = custom_modules.Module(
        'New module title (has to be unique)',
        'Implements some functionality',
        global_urls, course_urls)
    return custom_module
