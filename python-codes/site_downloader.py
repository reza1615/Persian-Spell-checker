#!/usr/bin/python
# -*- coding: utf-8  -*-
#
# Reza(User:reza1615), 2014
#
# Distributed under the terms of the GNU Lesser General Public License (LGPL 2.1)
#coding:utf8
import urllib2,codecs,re,time
from BeautifulSoup import BeautifulSoup

webadress=u'http://www.' #here you should add website link without last number

for i in range(0,10000):
    urlr=webadress+str(1000+i)

    try:
        page = urllib2.urlopen(urlr)
        soup = BeautifulSoup(page)
        text=str(soup)
        cases=text.split('<p>')
        item=[]
        count=0
        for case in cases:
            count+=1
            if count==1:
                continue
            our_text=case.split('</p>')[0]
            our_text=re.sub(r'\<a .*?\>.*?\<\/a\>',' ',our_text)
            our_text=re.sub(r'[\d\w]',' ',our_text)
            our_text=our_text.replace('•',' ').replace('/',' ').replace('ü',' ').replace("'",' ').replace('\\',' ').replace('[',' ').replace(']',' ').replace('?',' ').replace('؟',' ').replace(')',' ').replace('_',' ').replace('(',' ').replace('}',' ').replace('{',' ').replace('.',' ').replace('\r','').replace('>',' ').replace('<',' ')
            our_text=our_text.replace('`',' ').replace('=',' ').replace('»',' ').replace('«',' ').replace('~',' ').replace('!',' ').replace('@',' ').replace('$',' ').replace(',',' ').replace('%',' ').replace('،',' ').replace('-',' ').replace(';',' ').replace(':',' ').replace('*',' ').replace('"',' ').replace('\t',' ').replace('&',' ').replace('#',' ').replace('+',' ')
            our_text=our_text.replace('  ',' ').replace('    ',' ').replace('   ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('\n ','\n').replace('\n\n\n\n','\n').replace('\n\n\n','\n').replace('\n\n','\n')
            item.append(our_text.strip())
        text='\n'.join(item)
    except:
       continue
    print urlr
    with codecs.open( 'FinallResult.txt',mode = 'a') as f:
                    f.write( text+'\n' )
    time.sleep(1)
    
