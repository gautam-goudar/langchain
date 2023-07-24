# About
---
To get started with LangChain and OpenAI


## Creating an environment file to store the Open API key
    
```bash
/path/to/langchain$ touch .env
```

## Setting up the environment file

```bash
OPENAI_API_KEY=sk-[redacted]
```

## Getting started

### 1. Create a virtual environment (venv)

- Follow the instructions [here](https://docs.python.org/3/library/venv.html) to create a virtual environment.

- For VSCode, follow the instructions [here](https://code.visualstudio.com/docs/python/environments#_creating-environments) to create a virtual environment.

### 2. Install the required packages

```bash
/path/to/langchain$ pip install -r requirements.txt
```

### 3. Activate the environment

```bash
/path/to/langchain$ source .venv/bin/activate
```


### References
[Langchain docs](https://python.langchain.com/docs/get_started/introduction)