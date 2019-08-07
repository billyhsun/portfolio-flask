# portfolio-flask

Improved version of my original portfolio website (billyhsun.github.io/portfolio), but deployed in Flask and Docker. 


## Quick Start:

### Docker:

Install Docker:

```bash
apt-get update
apt install docker.io
```

Navigate to the folder of this repo, then build and deploy application:

```bash
sudo docker build --tag=demo .
sudo docker run -p 5000:5000 demo
```

Open the app in any web browser using the url:

```bash
localhost:5000
```

For mobile access, check the IP (IPv4) address of your device. Connect your mobile device to the local network, and open enter url in your mobile browser in the format ```[IP address]:5000```, for instance:

```bash
123.456.7.89:5000
```

