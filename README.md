# CTFd user push

This script reads list of users from a separated file and uploads that to CTFd.
You need to specify a few initial config from this source code below.
Braces supported. To work properly and avoid modification of CTFd behavior, brace setting need to make a few API requests.
To begin you'll need an API key. With an admin user you can optain it from CTFd dashboard > user settings.

Required module: requests
```
pip install requests
```
If you need to install as a system package, it usualy available as python3-requests or py3-requests.
