I. ENV SETUP:
1. python3 -m venv .venv (Create an environment, makes a folder named .venv" that acts as a clean slate for this project)
2. source .venv/bin/activate (Enters the env, tells system to use py and the libs in the folder)
3. pip install browser-use playwrite langchain-ollama (install the Big Three - Browser controller, agent framwork, ollama connector)
4. playwright install chromium (downloads the engine - chromium that the AI is allowed to control)
5. ollama pull llama3 (Downloads the "brain")
