
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
    ]
    course_urls = [
        ('/course', handlers.NewCourseHandler),
        ('/new-url', handlers.NewCourseHandler)
    ]

    global custom_module
    custom_module = custom_modules.Module(
        'New module title (has to be unique)',
        'Implements some functionality',
        global_urls, course_urls,
        notify_module_disabled=on_module_disabled,
        notify_module_enabled=on_module_enabled)
    return custom_module
