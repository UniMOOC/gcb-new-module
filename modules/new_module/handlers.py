
from controllers.utils import BaseHandler


class NewURLHandler(BaseHandler):
    def get(self):
        self.response.out.write('Some stuff')
