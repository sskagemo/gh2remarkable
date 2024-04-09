from setuptools import setup, find_packages

setup(
    name='gh2remarkable',
    version='0.0.1',
    author='Steinar skagemo',
    author_email='sskagemo@gmail.com',
    description='A tool to sync github repositories to remarkable',
    packages=find_packages(),
    install_requires=[
        'typer',
        'requests',
        'PyGithub',
        'PyMuPDF',
    ],
    entry_points = {'console_scripts':
                    ['gh2rm=gh2remarkable.main:app' ]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
    ],
)