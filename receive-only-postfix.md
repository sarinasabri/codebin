# Receive-Only Email Server
_(Assumes Debian 7)_

Set your hostname:
	`hostname dev.domain.tld`

Install postfix:
	`sudo apt-get install postfix`
	Select "Internet Site"
	Set name to hostname

Create user you wish to receive emails with (e.g. testperson@dev.domain.tld):
	`sudo adduser testperson`

Add the following to /etc/postfix/main.cf:
```
smtpd_sender_restrictions =
        check_sender_access pcre:/etc/postfix/sender_check
        permit
```

Create /etc/postfix/sender_check and add/edit to your requirements:
```
/^root@dev\.domain\.tld$/			OK
/^testperson@.*\.domain\.tld$/		OK
/./                                 REJECT This mail server does not accept mail from you
```

Restart postfix with `sudo service postfix restart`

User's email is stored in /var/mail by default.