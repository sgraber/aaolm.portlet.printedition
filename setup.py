from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='aaolm.portlet.printedition',
      version=version,
      description="This portlet displays information about the printed edition of Advanced Aquarist's Online Magazine.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='pod, Advanced Aquarist, print-on-demand, Amazon.com',
      author='Shane Graber',
      author_email='liquid@reefs.org',
      url='http://www.advancedaquarist.com/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['aaolm', 'aaolm.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.autoinclude',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
