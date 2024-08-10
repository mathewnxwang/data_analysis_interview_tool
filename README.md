# Intro

This repo contains the code to run a Flask app locally where you can practice with AI powered data analyst interviews.

### Problem

When I interviewed from my first data analyst job years ago, there were few resources online to practice.
I mostly had to rely on friends to make up interviews for me to practice my SQL and Python skills.
Things may have changed since then, but it would have been nice to have an unlimited set of interview questions to practice with!

# Design

### LLM architecture

There are 3 main LLM calls made:
1. Dataset generation: we ask a LLM to generate a dataset suitable for a typical analytics interview based on some parameters provided by the user which can tailor the practice to a specific company and/or domain.
2. Question generation: we ask a LLM to generate a couple of analytics interview questions from that dataset.
Since we want a diverse set of questions, we ask a LLM for all 3 questions in 1 call expecting that it won't create essentially redundant questions.
3. Answer generation: we ask a LLM to generate the answer code for each interview question.
Since we want to maximize the ability of the LLM to produce an accurate answer, each LLM call focuses on generating the answer for a single question.

# How to run

* 
