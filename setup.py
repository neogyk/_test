import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'python-dateutil',
    'numpy',
    'xlrd',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2',
    'PyJWT',
    'pyramid_jwt',
    'bcrypt',
    'passlib',
    'pymemcache',
    'python-memcached',
    'pandas',
    'numpy',
    'trafaret_config',
    'openpyxl',
    'Sphinx',
    'pyramid_autodoc'
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    ]

setup(name='IAP',
      version='0.0',
      description='IAP',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTPS",
          "Topic :: Internet :: WWW/HTTPS :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = iap:main
      [console_scripts]
      initialize_IAP_db = iap.common.repository.initializedb:main
      """,
      )
