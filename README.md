# fabric-deployment

Dockerfile for remote commands, CI/CD.

## Usage

### Run with an env file:

**env**

```bash
FAB_USER=user
FAB_HOST=12.34.567.89
# optional CWD (defaults to ".")
FAB_CWD=/path/to/my/remote/repo
# optional password
FAB_PASSWORD=qwertydvorak
# optional ssh keyfile (passed via volume)
FAB_SSH_KEY=/id_rsa
```

`> docker run --rm -it --env-file env bozdoz/fabric-deployment fab ls`

### Run in CI/CD

#### GitHub

In a workflow: 

```yml
jobs:
  deploy:
    runs-on: ubuntu-latest
    container:
      image: bozdoz/fabric-deployment:1.1.0
      env:
        FAB_CWD: ${{ secrets.FAB_CWD }}
        FAB_HOST: ${{ secrets.FAB_HOST }}
        FAB_PORT: ${{ secrets.FAB_PORT }}
        FAB_USER: ${{ secrets.FAB_USER }}
        FAB_PASSWORD: ${{ secrets.FAB_PASSWORD }}
    steps:
      - run: fab gitpull dockercomposebuild
```

### Passing a Private SSH KEY

```bash
> docker run --rm -it \
  --env-file env \
  -v ~/.ssh/id_rsa:/id_rsa \
  -e FAB_SSH_KEY=/id_rsa \
  bozdoz/fabric-deployment fab ls
```

If your remote user has proper permissions you can execute commands through fabric.

### Troubleshooting CI/CD Pipeline

You can use `bozdoz/fabric-deployment` as a CI/CD image (In GitLab for example), but you may need to execute fab commands with the collection flag `-r /app` to tell fabric where the root fabfile is (see Dockerfile WORKDIR); however, there is a workaround in the Dockerfile: 

```dockerfile
# wrap fab so that we always reference workdir
RUN mv /usr/local/bin/fab /usr/local/bin/_fab \
  && echo -e '#!/bin/sh\n_fab -r /app "$@"' > /usr/local/bin/fab \
  && chmod +x /usr/local/bin/fab
```

## But Why Do Any of This?

For ease of use with CI/CD.

## Commands

| Command              | Description                                                         |
| -------------------- | ------------------------------------------------------------------- |
| apachereload         | Reloads Apache, assuming sudo permissions are setup                 |
| djangostatic         | Runs collectstatic on a Django project                              |
| dockercomposebuild   | Runs docker-compose up -d --build                                   |
| dockercomposerestart | Runs docker-compose restart, which stops/arts containers            |
| dockercomposeup      | Runs docker-compose up -d                                           |
| gitpull              | Runs git pull                                                       |
| gulpproduction       | Runs gulp production                                                |
| ls                   | Runs ls for debugging purposes                                      |
| npmbuild             | Runs npm run build                                                  |
| npmci                | Runs npm ci                                                         |
| npminstall           | Runs npm install                                                    |
| put                  | Transfer files from local disk to remote server                     |
| pwd                  | Runs pwd for debugging purposes                                     |
| runscript            | Moves a shell script to remote CWD, executes it, and deletes it     |
