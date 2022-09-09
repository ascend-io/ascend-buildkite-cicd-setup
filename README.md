# Ascend CICD for Dataflows

Setup script to generate Ascend pipeline. 

## Pre-requisites

* Make sure you have a [buildkite account](https://buildkite.com/).
* Make sure you have a [github](https://github.com/)/[bitbucket](https://id.atlassian.com/login?application=bitbucket) account.
* Make sure you have an active [buildkite-agent](https://buildkite.com/docs/agent/v3) to store your secrets.


## Setup guide

```
$ python3 -m venv venv/
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

Obtain your access and secret keys from your Ascend environment as it is required in the next step.
It can be found from your Profile tab:

![profile](profile.png)

```
$ python3 init.py
```

Once that is completed, your Ascend dataflow will be downloaded locally. 
You can now create a new remote repo on github/bitbucket and create a webhook for buildkite.
```
$ git remote rm origin
$ git remote add origin YOUR_NEW_REPO
$ git commit -am 'initial commit'
$ git push
```

Create a new pipeline: [![Add to Buildkite](https://buildkite.com/button.svg)](https://buildkite.com/new)

For build steps command, you can use `buildkite-agent pipeline upload`, which will deploy according to `.buildkite/pipeline.yml` instructions.

![build-steps](build_steps.png)


Add your credentials to your buildkite agent.
Use `ASCEND_ACCESS_KEY` for your access key id and `ASCEND_SECRET_KEY` for your secret access key.
