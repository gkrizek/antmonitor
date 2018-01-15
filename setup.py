from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name="antmonitor",
    version="0.1.0",
    description="Antminer Monitoring Service",
    long_description=readme(),
    author="Graham Krizek",
    author_email="graham@krizek.io",
    url="https://github.com/gkrizek/antmonitor",
    license="MIT",
    packages=["antmonitor"],
    install_requires=[
        "boto3",
        "click",
        "requests"
    ],
    keywords="antminer bitcoin bitmain monitor btc bch cash crypto cryptocurrency"
)
