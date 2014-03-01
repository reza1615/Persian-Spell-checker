#!/usr/bin/python
# -*- coding: utf-8  -*-
#
# Reza(User:reza1615), 2011
#
# Distributed under the terms of the GNU Lesser General Public License (LGPL 2.1)
#coding:utf8
import codecs,re,string
print 'Start the first step'
text2 = codecs.open( 'FinallResult.txt',u'r' ,u'utf8' )
text = text2.read()
text=re.sub(ur'[\n\r]',u' ',text)
text=re.sub(ur'[\s]{2,}',u' ',text)
text=text.strip()
our_list=text.split(u' ')
text=u' '+text+u' '
our_dict={}
for word in our_list:
    if not word in our_dict:
        word_num= string.count( text,u' '+word+u' ')
        our_dict[word]=str(word_num)
our_new_text=u'\n'
print 'Pass the first step'
for i in our_dict:
    our_new_text+=i+u'\t'+our_dict[i]+u'\n'
print 'Finish the second step'
with codecs.open( 'FinallResult-list.txt',mode = 'w',encoding = 'utf8') as f:
    f.write(our_new_text.strip())
