from setuptools import setup, find_packages

setup(
    name='bowl',
    version='0.1.1',
    packages=find_packages(),
    license='LICENSE',
    description='Tool for easily building and configuring virtual environments on top of Docker.',
    long_description=open('README.md').read(),
    author=u'Charlie Lewis',
    author_email='charlie.lewis42@gmail.com',
    package_data={'': ['LICENSE', 'README.md', 'requirements.txt'], 'bowl': ['containers/*/*/databases/dockerfiles/*/Dockerfile', 'containers/*/*/environment/dockerfiles/*/Dockerfile', 'containers/*/*/services/dockerfiles/*/Dockerfile', 'containers/*/*/tools/dockerfiles/*/Dockerfile']},
    install_requires=['docker-py==0.3.0'],
    entry_points={
        'console_scripts': [
            'bowl = bowl.cli:main',
        ]
    }
)
