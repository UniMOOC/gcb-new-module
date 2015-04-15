
import logging

from models import custom_modules

from . import handlers


def register_module():
    """Registers this module in the registry."""

    def on_module_enabled():
        logging.info('Module new_module.py was just enabled')

    def on_module_disabled():
        logging.info('Module new_module.py was just dissabled')

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
        global_urls, course_urls,
        notify_module_disabled=on_module_disabled,
        notify_module_enabled=on_module_enabled)
    return custom_module
