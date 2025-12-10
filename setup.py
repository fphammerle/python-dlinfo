import pathlib
import setuptools

setuptools.setup(
    name="dlinfo",
    use_scm_version=True,
    maintainer="Fabian Peter Hammerle",
    maintainer_email="fabian.dlinfo@hammerle.me",
    description="Python wrapper for libc's dlinfo and dyld_find on Mac",
    long_description=pathlib.Path("README.rst").read_text(encoding="utf-8"),
    license="MIT",
    url="https://github.com/fphammerle/python-dlinfo",
    packages=setuptools.find_packages(),
    python_requires=">=3.10",  # >=3.6 for f-strings, <3.10 untested
    setup_requires=["setuptools_scm"],
    tests_require=["pytest"],
    classifiers=[
        # https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        # .github/workflows/python.yml
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
)
