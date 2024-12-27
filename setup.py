from setuptools import setup, find_packages

setup(
    name="gois",
    version="1.0.0",  # Updated version for production release
    description="A professional package for GOIS-based inference, evaluation, and preprocessing",
    author="MUHAMMAD MUZAMMUL",
    author_email="munagreat123@gmail.com",
    author_email="muzamal@zju.edu.cn",
    url="https://github.com/MMUZAMMUL/GOIS",
    packages=find_packages(include=["my_package", "my_package.*", "scripts.*"]),  # Include main packages and scripts
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    install_requires=[
        "ultralytics>=8.0.0",
        "gdown>=4.5.1",
        "pycocotools>=2.0.6",
        "numpy>=1.21.6",
        "Pillow>=9.0.1",
        "torch>=1.10.0",
        "pandas>=1.3.5",
        "matplotlib>=3.4.3",
    ],
    entry_points={
        "console_scripts": [
            "gois-download-data=data.download_data:main",  # Download dataset
            "gois-download-models=Models.download_models:main",  # Download pretrained models
            "gois-full-inference=scripts.full_inference:main",  # Full inference
            "gois-gois-inference=scripts.gois_inference:main",  # GOIS inference
            "gois-evaluate-full=scripts.evaluate_prediction:main",  # Evaluate full inference
            "gois-evaluate-gois=scripts.evaluate_gois:main",  # Evaluate GOIS
            "gois-generate-ground-truth=scripts.generate_ground_truth:main",  # Generate ground truth in COCO format
            "gois-calculate-results=scripts.calculate_results:main",  # Compare results
            "gois-evaluate-upscaling=scripts.evaluate_upscaling:main",  # Evaluate with upscaling
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Ensure compatibility with your tools
)
