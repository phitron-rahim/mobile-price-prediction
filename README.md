# LangChain AI Chatbot

An AI-powered chatbot built with **LangChain, RunnableBranch, RunnableParallel, Pydantic, and Streamlit**.

## Overview

This project demonstrates how to build a structured conversational AI application using LangChain's LCEL components. It routes user queries to appropriate prompts and generates multiple outputs in parallel.

## Key Features

- **Intelligent Query Routing:** Uses `RunnableBranch` to select an appropriate prompt based on the user's question.
- **Parallel Output Generation:** Uses `RunnableParallel` to generate a main response and a short summary simultaneously.
- **Structured Output Validation:** Uses Pydantic schemas to validate generated responses.
- **Interactive UI:** Provides a Streamlit interface for interacting with the chatbot.
- **Modular Architecture:** Separates application logic, chatbot chains, prompts, and schemas into dedicated Python files.

## Tech Stack

Python · LangChain · Streamlit · Pydantic · RunnableBranch · RunnableParallel

## Project Structure

- `app.py` — Streamlit application
- `chatbot.py` — Chatbot chain and processing logic
- `prompts.py` — Prompt templates
- `schemas.py` — Structured output schemas
- `requirements.txt` — Project dependencies

## Getting Started

1. Clone the repository.
2. Install the dependencies:

   `pip install -r requirements.txt`

3. Configure the required API key using environment variables.
4. Run the application:

   `streamlit run app.py`

## Learning Outcomes

This project demonstrates practical experience with LangChain expression language, conditional routing, parallel execution, structured outputs, and interactive AI application development.

## Author

**Rahim Hassan**

[GitHub](https://github.com/phitron-rahim) · [AI/ML Portfolio](https://rahim-ai-ml-portfolio.vercel.app/)
