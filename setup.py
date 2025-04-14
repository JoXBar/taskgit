from setuptools import setup

setup(
    name='taskgit',
    version='0.1',
    py_modules=['taskgit'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'taskgit=taskgit:main',
        ],
    },
    author='JoXBar',
    author_email='23josue.barrios@gmail.com',  
    description='Herramienta de gestión de tareas en la terminal con historial usando Git',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JoXBar/taskgit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)