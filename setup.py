from setuptools import setup

install_requires = [line.strip()
                    for line in open('requirements.txt').readlines()]

setup(
    name='onehourloop',
    version='0.1.0',
    description='Combine audio clips and GIFs to create video loops.',
    url='https://github.com/cyberseckenny/onehourloop',
    author='Kenny',
    license='GNU',
    packages=['onehourloop'],
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    project_urls={
        'Github': 'https://github.com/cyberseckenny/onehourloop'
    }
)
