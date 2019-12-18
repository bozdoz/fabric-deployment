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

`fab ls` -> list files and directories

`fab gitpull` -> run git pull

`fab npminstall npmbuild` -> run npm install then npm build

`fab dockercomposeup` -> run docker-compose up -d

`fab dockercomposebuild` -> run docker-compose up -d --build

`fab dockercomposerestart` -> run docker-compose restart

`fab gulpproduction` -> run gulp production

`fab djangostatic` -> run ./manage.py collectstatic --noinput

`fab apachereload` -> run sudo /etc/init.d/apache2 reload
