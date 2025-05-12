from setuptools import setup, find_packages

setup(
    name="clearcache",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'clearcache=clearcache.cli:main',
        ],
    },
    author="OpenInfra Dev",
    description="Cross-platform CLI to clear dev caches (Chrome, pip, VSCode, etc.)",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/openinfra-dev/clearcache",
    project_urls={
        "Source": "https://github.com/openinfra-dev/clearcache"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
