# Intro

This repo contains the code to run a Flask app locally where you can practice writing Python Pandas code to solve AI powered data analyst interviews.

### Problem

When I interviewed from my first data analyst job years ago, there were few resources online to practice.
I mostly had to rely on friends to make up interviews for me to practice my SQL and Python skills.
Things may have changed since then, but it would have been nice to have an unlimited set of interview questions to practice with!

# Design

### LLM architecture

I used OpenAI's `gpt-4o` as a starting default. There are 3 LLM calls made:
1. Dataset generation: we ask a LLM to generate a dataset suitable for an analytics interview based on parameters provided by the user which tailor the practice to a specific company and/or domain.
2. Question generation: we ask a LLM to generate a couple of analytics interview questions from that dataset.
Since we want a diverse set of questions, we ask a LLM for all 3 questions in 1 call expecting that it won't generate redundant questions.
3. Answer generation: we ask a LLM to generate the answer code for each interview question.
Since we want to maximize the ability of the LLM to produce an accurate answer, we make 1 LLM call for each question to generate an answer.

### Front-end

I built a simple front-end using Flask which can be run locally.

# How to run

* clone the repo locally
* install `poetry`, a dependency/virtual environment manager
* navigate to the repo directory and run `poetry install`
* create or copy your OpenAI api key from https://platform.openai.com/api-keys
* create a `secrets.env` file which should contain `OPENAI_API_KEY=<your OpenAI api key here>`
* run the flask app with the command `python app.py`
* go to http://127.0.0.1:5000 in your local browser and have fun!
