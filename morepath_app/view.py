from morepath_app.app import App
from morepath_app.model import Document,User

@App.json(model=Document)
def document_default(self, request):
    return {'id': self.id, 'title': self.title, 'content': self.content }


@App.view(model=User)
def user_info(self, request):
    return "User's full name is: %s" % self.fullname