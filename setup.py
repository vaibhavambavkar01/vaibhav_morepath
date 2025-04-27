from setuptools import setup, find_packages

setup(name='morepath_app',
      packages=find_packages(),
      install_requires=[
         'morepath'
      ],
      entry_points={
         'console_scripts': [
          'myproject-start = morepath_app.run:run'
          ]
      })