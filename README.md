# fabric-deployment

Dockerfile for remote commands, CI/CD.

## Usage

Run with an env file:

**env**

```bash
USER=user
HOST=12.34.567.89
CWD=/path/to/my/remote/repo
# optional password
PASSWORD=qwertydvorak
# optional ssh keyfile (passed via volume)
SSH_KEY=/id_rsa
```

`> docker run --rm -it --env-file env bozdoz/fabric-deployment fab ls`

### Passing a Private SSH KEY

`> docker run --rm -it --env-file env -v ~/.ssh/id_rsa:/id_rsa bozdoz/fabric-deployment fab ls`

If your remote user has proper permissions you can execute commands through fabric.

## But Why?

For ease of use with CI/CD.

## Commands

| apachereload | Reloads Apache, assuming sudo permissions are setup
| djangostatic | Runs collectstatic on a Django project
| dockercomposebuild | Runs docker-compose up -d --build
| dockercomposerestart | Runs docker-compose restart, which stops/starts containers
| dockercomposeup | Runs docker-compose up -d
| gitpull | Runs git pull
| gulpproduction | Runs gulp production
| ls | Runs ls for debugging purposes
| npmbuild | Runs npm run build
| npmci | Runs npm ci
| npminstall | Runs npm install
| put | Transfer files from local disk to remote server
| pwd | Runs pwd for debugging purposes
| runscript | Moves a shell script to remote CWD, then executes it
