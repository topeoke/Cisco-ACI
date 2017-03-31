from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession

apicUrl = "https://apic1.dcloud.cisco.com/"
loginSession = LoginSession(apicUrl,'admin','C1sco12345')
moDir = MoDirectory(loginSession)
moDir.login()
