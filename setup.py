from distutils.core import setup

setup(
  name = 'control-toolbox',
  packages = ['control'],
  version = '0.1', 
  license='MIT',
  description = 'Python Control System Toolbox',
  author = 'Rushad Mehta',
  author_email = 'rushadmehta16@gmail.com',
  url = 'https://github.com/rushad7/control-toolbox',
  download_url = 'https://github.com/rushad7/control-toolbox/archive/v0.1.tar.gz',
  keywords = ['Control Systems', 'Python Control Toolbox', 'System Simulation'],
  install_requires=[
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'Topic :: Software Development',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
