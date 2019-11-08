from setuptools import setup, find_packages

setup(name='pkg_tools',
      setup_requires=['setuptools_scm'],
      install_requires=['setuptools_scm'],
      use_scm_version={'write_to': 'pkg_tools/version.txt'},
      description="python package tools",
      author='Susanne Landgren', author_email="susanne.landgren@gmail.com",
      url='https://www.linkedin.com/in/susannelandgren',
      packages=find_packages(),
      test_suite = 'tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/make-package'],
      zip_safe=False)
