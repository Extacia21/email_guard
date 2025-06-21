from setuptools import setup, find_packages

setup(
    name="email_guard",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scikit-learn", "flask", "beautifulsoup4", "email-validator"
    ],
    author="Extacia Fakero",
    description="Email security library: scam detection, tracking, and filtering",
    python_requires=">=3.8"
)
