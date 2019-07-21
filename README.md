# fabric-deployment

docker file for pulling a repo remotely.

## Usage

Run with an env file: 

**env**
```bash
USER=user
HOST=12.34.567.89
PASSWORD=qwertydvorak
CWD=/path/to/my/remote/repo
```

`> docker run --rm -it --env-file env bozdoz/fabric-deployment fab gitpull`

If your remote user has proper permissions, your git repo will be pulled remotely.

## But Why?

For CI/CD: changes to a repo will be pushed automatically to production or staging.
