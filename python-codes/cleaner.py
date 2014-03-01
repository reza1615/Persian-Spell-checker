#!/usr/bin/python
# -*- coding: utf-8  -*-
#
# Reza(User:reza1615), 2011
#
# Distributed under the terms of GNU Lesser General Public License (LGPL 2.1)
#coding:utf8
import codecs,re
def arabic_to_farsi(text):
    text = re.sub(ur'[كﮑﮐﮏﮎﻜﻛﻚﻙ]', ur'ک', text)
    text = re.sub(ur'[ىىىﻴﻢﻳﻲﻱﻰىىﻯي]', ur'ی', text)
    return text

text2 = codecs.open( 'FinallResult-list.txt',u'r' ,u'utf8' )
text = text2.read()
text=re.sub(ur'[\d\w]',u' ',text)
text=re.sub(ur'[۰۱۲۳۴۵۶۷۸۹٠١١٢٣٤٥٦٧٧٨٨٩٩●]',u' ',text)
text=re.sub(ur'[\·\♦\٭\\,\^\|\˝\٬\’\”\‹\▪\○¼ç½éêüəıœ™Ááàäāćíłñū©ٰٔ]',u' ',text)
text=re.sub(ur'[ًٌٍَُِّْ]',u' ',text)
text=re.sub(ur'[]',u' ',text)
text=re.sub(ur'[\–\—…°≈≠±≤≥\−×÷√٪→←↔↑↓\#\٫]',u' ',text) 
text=text.replace(u'•',u' ').replace(u'ˈ',u' ').replace(u'؛',u' ').replace(u'/',u' ').replace(u'ۀ',u'هٔ').replace(u"﴿",u' ').replace(u"﴾",u' ').replace(u"'",u' ').replace(u'\\',u' ').replace(u'[',u' ').replace(u']',u' ').replace(u'?',u' ').replace(u'؟',u' ').replace(u')',u' ').replace(u'_',u' ').replace(u'(u',u' ').replace(u'}',u' ').replace(u'{',u' ').replace(u'.',u' ').replace(u'>',u' ').replace(u'<',u' ')
text=text.replace(u'`',u' ').replace(u'\t',u' ').replace(u'=',u' ').replace(u'»',u' ').replace(u'«',u' ').replace(u'~',u' ').replace(u'!',u' ').replace(u'@',u' ').replace(u'$',u' ').replace(u',u',u' ').replace(u'%',u' ').replace(u'،',u' ').replace(u'-',u' ').replace(u';',u' ').replace(u':',u' ').replace(u'*',u' ').replace(u'"',u' ').replace(u'&',u' ').replace(u'#',u' ').replace(u'+',u' ')
text=re.sub(ur'[\n\r]{2,}',u'\n',text)
text = re.sub(u'(\u202A|\u202B|\u202C|\u202D|\u202E|\u200F|\uFEFF|\u2003|\¬|\­)',u'\u200C', text)#حذف کارکترهای تغییرجهت
text = re.sub(u'‌{2,}', u'‌', text) # پشت‌سرهم
text = re.sub(u'‌(?![ئاآأإژزرذدوؤةبپتثجچحخسشصضطظعغفقکگلمنهیيًٌٍَُِّْٰٓٔ]|[\u0900-\u097F]|ֹ)', u'', text) # در پس
text = re.sub(u'(?<![ئبپتثجچحخسشصضطظعغفقکگلمنهیيًٌٍَُِّْٰٓٔ]|[\u0900-\u097F]|f|ֹ)‌', u'', text) # در پیش
text=text.replace(u'­',u' ').replace(u'­',u' ').replace(u'ـ',u' ').replace(u'ـ',u' ').replace(u'ـ',u' ').replace(u'ـ',u' ').replace(u'',u' ')
text=text.replace(u'',u' ')
text = re.sub(u'‌{2,}', u'‌', text) # پشت‌سرهم
text = re.sub(u'(\u00A0)',u' ', text).replace(u'(',u' ').replace(u')',u' ')
text=text.replace(u'    ',u' ').replace(u'    ',u' ').replace(u'   ',u' ').replace(u'  ',u' ').replace(u'  ',u' ').replace(u'  ',u' ')
text=arabic_to_farsi(text)

with codecs.open( 'FinallResult-list-2.txt',mode = 'w',encoding = 'utf8') as f:
    f.write(text.strip())

    
