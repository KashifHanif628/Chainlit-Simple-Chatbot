# a simple chatpot build with python UV and Chainlit

# chat session
# it represent a conversession between user and the application

# Event
# when certain thing happen like sending a message.

# Hooks
# Hook are special funtion that "Hook into" these events like loading a user iformation by running custome code
# when specific events accure.

# Decorators
# these are special workers @ that enhance function.

import chainlit as cl

@cl.on_message # its a build in decorator in chainlit
async def main(message: cl.Message): # cl.Message is a class which is coming from chainlit.
    response = f"You said: {message.content}" # content is working here as a user text
    await cl.Message(content=response).send() # .send is a build in function in chainlit to send the user response.
    # without .send method message will not send and error will accure.