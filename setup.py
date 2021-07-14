from setuptools import setup

def parse_requirements(filename):
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith('#')]

setup(name='samplevq', version='1.0',
      description='PyTorch package for VideoGPT-Paper',
      url='https://github.com/pointoflight/samplevq',
      author='Wilson Yan',
      author_email='wilson1.yan@berkeley.edu',
      license='BSD',
      packages=['samplevq'],
      zip_safe=True)
