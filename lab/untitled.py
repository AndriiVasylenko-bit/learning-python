import re
hdr = '''
rom news@gmane.org Tue Mar 04 03:33:20 2003
From: John Leasia <jleasia@umich.edu>
Subject: Re: Creating a site on collab
Date: Wed, 14 Dec 2005 18:40:44 -0500
Lines: 44
Message-ID: <29971379.1134603801926.JavaMail.tomcat5@mahimahi.ds.itd.umich.edu>
References: <5520705.1134585898311.JavaMail.tomcat5@mahimahi.ds.itd.umich.edu> <30732504.1134596730665.JavaMail.tomcat5@mahimahi.ds.itd.umich.edu> <18642115.1134597965260.JavaMail.tomcat5@mahimahi.ds.itd.umich.edu>
Mime-Version: 1.0
'''

y = re.findall('\Date: .*\n', hdr)

print(y)