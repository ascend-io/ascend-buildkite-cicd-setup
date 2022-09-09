# Ascend CICD for Dataflows

Setup script to generate Ascend pipeline. 

## Pre-requisites

* Make sure you have a buildkite account
* Make sure you have a github/bitbuckeet account
* Make sure you have an active [buildkite-agent](https://buildkite.com/docs/agent/v3) to store your secrets


## Setup guide

```
$ python3 -m venv venv/
$ venv/bin/activate
$ pip3 install -r requirements.txt
```

Obtain your access and secret keys
```
$ python3 init.py
```

Create a new remote repo on github/bitbuckeet
```
$ git remote rm origin
$ git remote add origin YOUR_NEW_REPO
$ git commit -am 'initial commit'
$ git push
```

Create a new pipeline: [![Add to Buildkite](https://buildkite.com/button.svg)](https://buildkite.com/new)

Add your credentials to your buildkite agent.
Use `ASCEND_ACCESS_KEY` for your access key id and `ASCEND_SECRET_KEY` for your secret access key.