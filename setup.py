from setuptools import setup, find_packages

setup(
    name='dg_chatgpt',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv',
        'requests'
    ]
)
