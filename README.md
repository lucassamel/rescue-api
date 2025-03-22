# Rescue API

MVP

---
## How to run 

You will need to have all the Python libraries listed in `requirements.txt` installed. 
After cloning the repository, navigate to the root directory through the terminal to execute the commands described below.

> It is highly recommended to use virtual environments like [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

This command installs the dependencies/libraries described in the requirements.txt file.

To run the API, simply execute:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

In development mode, it is recommended to use the `--reload` parameter, which will automatically restart the server after any changes to the source code.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Open **http://localhost:5000/#/** in your browser to check the status of the running API.
