OPENAI_API_KEY = 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


def setup():
    """Setup the OpenAI API key from the environment variable OPENAI_API_KEY."""

    import os
    import logging
    os.load_dotenv()

    if not 'OPENAI_API_KEY' in os.environ:
        warning = 'No OpenAI API key found. Set the `OPENAI_API_KEY` environment variable.'
        logging.warning(warning)
        raise ValueError(warning)

    import openai
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

    openai.api_key = OPENAI_API_KEY

    if not openai.api_key:
        warning = 'OpenAI API key is invalid'
        logging.warning(warning)
        raise ValueError(warning)

    if not os.path.exists("chat_logs"):
        logging.log(logging.INFO, "Creating `chats` directory")
        os.mkdir("chats")

    logging.log(logging.INFO, "OpenAI API key loaded successfully")


if __name__ == '__main__':
    print("This is a setup script. Please run `python3 -m chatgpt` instead.")
