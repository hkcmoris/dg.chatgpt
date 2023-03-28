from setuptools import setup, find_packages

setup(
    name='dg_chatgpt',
    version='1.1',
    description='wrapper for OpenAI chatgpt API, using `gpt-3.5-turbo` model',
    url='https://github.com/hkcmoris/dg_chatgpt',
    author='Ondřej Moravec',
    author_email='moravec@devground.cz',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv',
        'requests'
    ]
)
