import os

import openai
import json
from flask import Flask, redirect, render_template, request, url_for, jsonify
import logging

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/speak", methods=(["POST"]))
def speak():
  # return openai's response to the 'text' field
  input = request.get_json()['text'];  
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=generate_prompt(input),
    temperature=0.6,
  )
  return response.choices[0].text;

def generate_prompt(input):
    return """
Prompt: {}
Responses:""".format(
        input.capitalize()
    )
