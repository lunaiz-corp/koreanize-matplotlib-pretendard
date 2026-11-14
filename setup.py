# encoding: utf8
from setuptools import find_packages, setup
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['matplotlib']

setup(name='koreanize-matplotlib-pretendard',
      version='0.0.1',
      description='install & import하는 것만으로 matplotlib에서 프리텐다드를 사용하여 한글 그래프를 표시할 수 있습니다.',
      author='minsu.kim',
      author_email='minsu.kim@lunaiz.com',
      url='https://github.com/lunaiz-corp/koreanize-matplotlib-pretendard',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT License',
      packages=find_packages(),
      install_requires=install_requires,
      include_package_data=True,
      package_data={
          'koreanize_matplotlib': ['fonts/*'],
      })
