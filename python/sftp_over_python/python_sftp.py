import pysftp

srv = pysftp.Connection(host="ajw145support.faa.gov", username="manoj", password="manoj1234",log="python_sftp.log")

# ----------- Did not work as the hostkey needs to already be present - need to figure this out futher.

#with srv.cd ('tmp'):    # change remote dir to tmp
#    srv.put("python_sftp.py")

#srv.close()