def get_response(message):

    message = message.lower()

    responses = {

        "hello":"Hello 👋",

        "hi":"Hi there!",

        "python":"Python is a programming language.",

        "html":"HTML is used for creating webpages.",

        "css":"CSS is used for styling webpages.",

        "bye":"Goodbye!"

    }

    return responses.get(message,"Sorry! I don't understand.")












