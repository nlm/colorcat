from setuptools import setup,find_packages

setup(
    name = "colorcat",
    version = "0.1",
    packages = ['colorcat'],
    author = "Nicolas Limage",
    author_email = 'github@xephon.org',
    description = "colored cat utility",
    license = "GPL",
    keywords = "cat color",
    url = "https://github.com/nlm/colorcat",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Shells',
        'Topic :: Terminals',
    ],
    entry_points = {
        'console_scripts': [
            'colorcat = colorcat:main',
        ],
    }
)
