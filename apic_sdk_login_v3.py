from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
import getpass


username = raw_input("Username: ")
password = getpass.getpass("Password: ")

apicUrl = "https://apic1.dcloud.cisco.com/"
loginSession = LoginSession(apicUrl,username,password)
moDir = MoDirectory(loginSession)
moDir.login()

allTenant = moDir.lookupByClass('fvTenant')
for i in allTenant:
    print i.name