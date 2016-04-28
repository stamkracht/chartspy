from setuptools import setup

setup(name='chartspy',
      version='0.1',
      description='Charts using SVG for python',
      url='http://github.com/stamkracht/chartspy',
      author='Stamkracht',
      author_email='roel@stamkracht.com',
      license='MIT',
      packages=['chartspy'],
      install_requires=[
          'cairosvg',
      ],
      zip_safe=False)
