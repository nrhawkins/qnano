from setuptools import setup, PEP420PackageFinder

setup(
    name="qnano",
    version="0.0.1",
    packages=PEP420PackageFinder.find("src"),
    package_data={"nano.executor": ["data/*.toml"]},
    package_dir={"": "src"},
    install_requires=["numpy", "pandas", "scipy", "toml", "sqlalchemy", "networkx", "tables"],
    extras_require={
        "testing": ["hypothesis", "pytest", "pytest-mock"],
        "documentation": ["sphinx", "sphinx_rtd_theme", "sphinx-autobuild", "sphinxcontrib-napoleon"],
    },
    entry_points={
        "console_scripts": [
            ["qnano=qnano.executor.qnano_main:entry"],
        ]
    },
    scripts=["scripts/qnano"],
    zip_safe=False,
    classifiers=[
        "Intendend Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Statistics",
    ],
)
