from distutils.core import setup
setup(
  name = '102217053_topsis',
  packages = ['102217053_topsis'],
  version = '1.0.1',
  license='MIT',
  description = 'This is a topsis package',
  author = 'Mitul Agarwal',
  author_email = 'mitulagarwal2003@gmail.com',
  url = 'https://github.com/user/reponame',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['topsis'],
  install_requires=[
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)