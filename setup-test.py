import asyncio
from browser_use import Agent
from langchain_ollama import ChatOllama
from pydantic import Field

# We add 'model_config' to tell Pydantic to allow extra attributes
class OllamaLLM(ChatOllama):
    provider: str = Field(default="ollama")
    model_config = {"extra": "allow"} # ✅ FIX: Allows browser-use to add its tracking tools

    @property
    def model_name(self):
        return self.model

async def main():
    # Use your high-power gpt-oss model
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

if __name__ == "__main__":
    asyncio.run(main())