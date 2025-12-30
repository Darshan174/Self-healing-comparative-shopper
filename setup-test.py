import asyncio # preform simultaneouly tasks while waiting for others to finish
from browser_use import Agent #A Agent is a "supervisor", understands what the button mean, and decides what to do next
from langchain_ollama import ChatOllama # tells py what to do to the ollama app
from pydantic import Field # formates data sent to AI correctly 

# We add 'model_config' to tell Pydantic to allow extra attributes
class OllamaLLM(ChatOllama): # create a new class OllamaLLM that extends ChatOllama
    provider: str = Field(default="ollama") # set default provider to ollama
    model_config = {"extra": "allow"} # ✅ FIX: Allows browser-use to add its tracking tools

    @property #no matter what the library asks for, it will always return the model name
    def model_name(self):
        return self.model

async def main(): # oause while waiting for a websote to load 
    # Use high-power gpt-oss model
    llm = OllamaLLM(
        model="gpt-oss:120b-cloud", 
        num_ctx=32000
    )
    
    agent = Agent(
        task="Navigate to google.com and find the 'About' link.",
        llm=llm,
    )
    
    result = await agent.run()
    print(result)
#Engine starter
if __name__ == "__main__": #Safety switch
    asyncio.run(main())