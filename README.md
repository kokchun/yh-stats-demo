# yh-stats-dashboard

In this demo, we will deploy a simple dash app to Azure web apps and also set up Github actions to get continuous deployment. A simple authentication is added to demo environment variables in Azure web apps.

## venv

1. Install packages, for this project I install the following to my venv
   
```py
pip install pandas gunicorn dash_auth dash python-dotenv 
```

You can also install packages for development such as black, flake8 and more. Note that gunicorn is used for the server.

2. Take a snapshot of the venv in a requirements.txt 

```bash
pip freeze > requirements.txt
```

Note that you must activate your venv first, so that you don't freeze the global environment.

## Steps for deployment

1. Add to app.py

```py
server = app.server
```

2. Set debug to False and set the correct port. Note that by default Azure web apps will expose 443 to HTTPs and 80 to HTTP. Hence set the port to 443. 

```py
if __name__ == "__main__":
    app.run_server(debug = False, host = "0.0.0.0", port = 443)
```

3. Dockerize the app and test it out, this is the dockerfile I've created

```docker
FROM python:3.9-slim
WORKDIR /dash_app
ENV PYTHONPATH=/dash_app
COPY requirements.txt requirements.txt
COPY data data
COPY src src

RUN pip install -r requirements.txt

WORKDIR /dash_app/src

EXPOSE 443
CMD ["gunicorn", "app:server", "--bind", ":443"]
```

Build the image and run it, exposing the ports  

```bash
docker build -t yh-stats-dash . 
docker run -d -p 443:443 yh-stats-dash
```

4. Test out the dockerized app 

## Azure web app deployment

There are different ways you can deploy to Azure web apps, but we will use Github actions in to get continuous deployment. 

1. Go to your Github account and create a personal access token 
   - click on your profile picture when logged in 
   - go to settings > developer settings > personal access token > tokens (classic) > generate new token (classic)
   - tick repo and write:packages and generate a new token
   - copy your access token, this will be the password for Azure web apps in the next step

2. Log into Azure portal, make sure you have gotten your educational credits
3. Add a new resource and choose Web app
4. Choose docker deployment
5. Connect your Github account and your repo to Azure web apps
6. In url type in https://ghcr.io
7. Download publish profile from your web app, copy the content
8. In your Github repository, go into settings > secrets and variables > new repository secret > name it AZURE_WEBAPP_PUBLISH_PROFILE > the value is the content from publish profile from your web app
9. As we have .env with variables to hide in our local development, we need to add this in Azure web app so that it gets injected into the docker container. 
10. Now try deploy, and you can check the build and deployment status in Github actions in your repo, then check container logs in Azure web apps. It may take a few minutes before everything is set up.