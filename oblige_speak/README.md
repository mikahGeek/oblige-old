# oblige-speak

This will be a communication layer, leveraging OpenAI's ChatGPT fori rapid content generation. Oblige systems will use this service to exchange life-like content and generate insights.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd oblige_speak
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt -i https://pypi.org/simple
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```
The .env file will store your secret keys. Do not upload .env to the repo (it is already in the .gitignore). Configure the following in .env:

   ```
   OPENAI_API_KEY=
   AWS_REGION=
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ```

Port can be configured as well:

   ```bash
   $ flask run -p 5001
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).

## Executing

Run a curl POST command to the server. Use {'text': 'some text here'} as the POST body. Example:

   ```bash
   $ curl -i -H "Content-Type: application/json" -X POST -d '{"text": "tell me a story"}' http://127.0.0.1:5000/speak
   ```
