import os
import sys
import openai
import json
from flask import Flask, redirect, render_template, request, url_for, jsonify
import logging

app = Flask(__name__)


@app.route("/", methods=(["GET"]))
def root():
  return { "text": "hello world" };
