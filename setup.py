from setuptools import setup, find_packages

setup(
    name="gois1",
    version="0.1",
    description="A package for GOIS-based inference, evaluation, and preprocessing",
    author="MUHAMMAD MUZAMMUL",
    author_email="munagreat123@gmail.com",
    url="https://github.com/MMUZAMMUL/GOIS",
    packages=find_packages(include=["my_package", "my_package.*"]),  # Include the `my_package` directory
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
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
            "gois-download-data=data.download_data:main",
            "gois-download-models=Models.download_models:main",
            "gois-full-inference=my_package.full_inference:main",
            "gois-gois-inference=my_package.gois_inference:main",
            "gois-evaluate-full=scripts.evaluate_full_inference:main",
            "gois-evaluate-gois=scripts.evaluate_gois:main",
            "gois-generate-ground-truth=scripts.generate_ground_truth:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
