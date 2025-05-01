Follow docs:
https://morepath.readthedocs.io/en/latest/organizing_your_project.html

Project layout
Here’s a quick overview of the files and directories of Morepath project that follows the guidelines in this document:

myproject
    setup.py
    myproject
         __init__.py
        app.py
        model.py
        [collection.py]
        path.py
        run.py
        view.py

Project setup
Here is an example of your project’s setup.py with only those things relevant to Morepath shown and everything else cut out:

from setuptools import setup, find_packages

setup(name='myproject',
      packages=find_packages(),
      install_requires=[
         'morepath'
      ],
      entry_points={
         'console_scripts': [
          'myproject-start = myproject.run:run'
          ]
      })
      
      

You now need to install this project. If you want to install this project for development purposes you can use python setup.py develop, or pip install -e . from within a virtualenv.
      
App Module
The app.py module is where we define our Morepath app. Here’s a sketch of app.py:

import morepath

class App(morepath.App):
    pass
    
Run Module    
In the run.py module we define how our application should be served. We take the App class defined in app.py, then have a run() function that is going to be called by the myproject-start entry point we defined in setup.py: