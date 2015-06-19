from setuptools import setup, find_packages

with open('requirements.txt') as f:
    depends = map(str.strip, f.readlines())

setup(name='pocket-change',
      version='0.0.6',
      author='Silas Ray',
      author_email='silas.ray@nytimes.com',
      license='Apache2.0',
      url='http://pocket-change.readthedocs.org/',
      description='The web front end for Sneeze and Pocket',
      long_description='The web front end for the Sneeze nose plugin test result reporting tool.',
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Information Technology',
                   'Topic :: Software Development :: Quality Assurance',
                   'Topic :: Software Development :: Testing'],
      packages=find_packages(),
      package_data={'' : ['LICENSE',
                          'pocket_change/static/*.js',
                          'pocket_change/static/*.css',
                          'pocket_change/ui/templates/*.html']},
      include_package_data=True,
      install_requires=depends
      )
