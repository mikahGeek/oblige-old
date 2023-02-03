import os
import sys
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
    temperature=0,
    max_tokens=1500
  )
  logging.info('this is an info log');
  print('hello world');
  print(f"len={len(response.choices)}");
  text = '';
  for choice in response.choices:
    text = choice.text + ' ';
  return text;

def generate_prompt(input):
    return """
      Text: {}
      Responses:""".format( input.capitalize() )
