from setuptools import setup, find_packages
import os

version = '1.7.3'

tests_require = [
    'collective.testcaselayer',
    'plone.app.testing',
    'collective.betterbrowser[pyquery]'
]

setup(name='seantis.dir.roadworks',
      version=version,
      description="Directory of Roadworks",
      long_description='\n'.join((
          open("README.rst").read(),
          open(os.path.join("docs", "HISTORY.txt")).read()
      )),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='',
      author='Seantis GmbH',
      author_email='info@seantis.ch',
      url='https://github.com/seantis/seantis.dir.roadworks',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['seantis', 'seantis.dir'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'plone.app.dexterity',
          'collective.autopermission',
          'collective.testcaselayer',
          'collective.dexteritytextindexer',
          'seantis.dir.base>=1.7',
          'seantis.plonetools>=0.9'
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
