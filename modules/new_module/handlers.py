
from controllers.utils import BaseHandler


class NewCourseHandler(BaseHandler):
    def get(self):
        self.response.out.write("/new-url works but /course doesn't")
