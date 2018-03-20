# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:32:37 2018

@author: echang
"""

from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='python-functions',
    url='https://github.com/DFEAGILEDEVOPS/python-functions',
    author='Eugene Chang',
    author_email='eugene.chang@education.gov.uk',
    # Needed to actually package something
    packages=['dfe_python'],
    # Needed for dependencies
    install_requires=['pandas','pymssql'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Repository of re-useable Python functions in DfE',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)