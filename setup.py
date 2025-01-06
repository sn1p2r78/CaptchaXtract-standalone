from setuptools import setup, find_packages

setup(
    name='captcha-xtract-standalone',
    version='1.0.0',
    description='Standalone version of CaptchaXtract for local usage.',
    author='sn1p2r78',
    author_email='sn1p2r78@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'fastapi',
        'uvicorn',
        'tesserocr',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'captcha-xtract=src.main:main']
    },
    classifiers=[
        'Programming Language :: Python ::3',
        'License :: OSI Approved ::MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7'
)