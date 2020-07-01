from setuptools import setup, find_namespace_packages, find_packages

REQUIRED_PACKAGES = [
    'flask', 'flask-login', 'werkzeug', 'Flask-Caching', 'gunicorn']

setup(name='next-free-day',
      version='0.0.1',
      url='localhost',
      author='Osvaldo Minatti',
      author_email='sebmin@gmail.com',
      install_requires=REQUIRED_PACKAGES,
      packages=find_namespace_packages(include=['next-free-day.*']),
      namespace_packages=['next-free-day'],
      include_package_data=False)
