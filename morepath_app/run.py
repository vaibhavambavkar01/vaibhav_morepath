
from morepath_app.app import App
import morepath

# def run():
#     morepath.autoscan()
#     App.commit()
#     morepath.run(App())

if __name__ == '__main__':
    morepath.run(App())