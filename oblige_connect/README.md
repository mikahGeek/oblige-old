# oblige-connect

This will be the connectivity layer between all oblige services and interfaces. It is the data integration layer, not a gateway or proxy.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

### Additional Prerequisites
* [AWS CLI](https://aws.amazon.com/cli/)
* [SAM CLI](https://github.com/awslabs/aws-sam-cli)

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
   AWS_REGION=
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   ```


7. Run the app

   ```bash
   $ flask run
   ```

The default port is 5000, but port can be configured as well:

   ```bash
   $ flask run -p 5001
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).

## Executing

