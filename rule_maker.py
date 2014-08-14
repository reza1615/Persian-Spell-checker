# -*- coding: utf-8  -*-
# Reza (User:reza1615)
# Distributed under the terms of the CC-BY-SA 3.0 .
# -*- coding: utf-8 -*-
import codecs
dict={
    u"پیاده" :u"روی|رو|نظام",
}
vari=u'''
<!-- Farsi rule, 2014-08-14 -->
<rule id="%s" name="%s">
 <pattern>
  <token regexp='yes'>(%s)+</token>
  <token regexp='yes'>(%s)</token>
 </pattern>
 <message>%s</message>
 <example type='incorrect'><marker>%s</marker></example>
 <example type='correct'>%s</example>
</rule>'''
count=0
text=u'\n'
for i in dict:
    count+=1
    our_vari=vari %(u'ZwnjCorection_ID_'+str(count),u'ZwnjCorection'+str(count),i,dict[i],u'اصلاح نیم‌فاصلهٔ میان دو کلمه',i.split(u'|')[0]+u' '+dict[i].split(u'|')[0],i.split(u'|')[0]+u'‌'+dict[i].split(u'|')[0])
    text+=our_vari
with codecs.open( u'my_patch.txt',mode = 'w',encoding = 'utf8' ) as f:
                    f.write( text )
