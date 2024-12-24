from setuptools import setup, find_packages

setup(
    name="gois",
    version="0.1.0",
    description="A package for GOIS-based inference and evaluation",
    author="MUHAMMAD MUZAMMUL",
    author_email="munagreat123@gmail.com",
    url="https://github.com/MMUZAMMUL/GOIS",
    packages=find_packages(),  # Automatically finds the 'my_package' package
    include_package_data=True,
    install_requires=[
        "ultralytics>=8.0.0",
        "gdown>=4.5.1",
        "pycocotools>=2.0.6",
        "numpy>=1.21.6",
        "Pillow>=9.0.1",
        "torch>=1.10.0",
    
    ],
    entry_points={
        "console_scripts": [
            "gois-download-data=my_package.download_data:main",
            "gois-download-models=models.download_models:download_ultralytics_models",
            "gois-full-inference=scripts.full_inference:main",
            "gois-gois-inference=scripts.gois_inference:main",
            "gois-evaluate-full=scripts.evaluate_full_inference:main",
            "gois-evaluate-gois=scripts.evaluate_gois:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
