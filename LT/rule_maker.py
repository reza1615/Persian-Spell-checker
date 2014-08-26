# -*- coding: utf-8  -*-
# Reza (User:reza1615)
# Distributed under the terms of the CC-BY-SA 3.0 .
# -*- coding: utf-8 -*-
import codecs
dict={
u"تام":u"الاختیار",
}
vari=u'''
<rule>
 <pattern>
  <%s>%s</token>
  <%s>%s</token>
 </pattern>
<message>آیا منظور شما <suggestion>\1&#8204;\2</suggestion>است؟</message>
 <short>%s</short>
 <example type='incorrect'><marker>%s</marker></example>
 <example type='correct'>%s</example>
</rule>'''
count=0
text=u'\n'
for i in dict:
    count+=1
    if u'|' in i:
        item1=u'('+i+u')'
        case1="token regexp='yes'"
    else:
        item1=i
        case1="token"

    if u'|' in dict[i]:
        item2=u'('+dict[i]+u')'
        case2="token regexp='yes'"
    else:
        item2=dict[i]
        case2="token"

    our_vari=vari %(case1,item1,case2,item2,u'اصلاح فاصلهٔ مجازی میان کلمهٔ مرکب',item1.split(u'|')[0].replace(u'(',u'').replace(u')',u'').strip()+u' '+item2.split(u'|')[0].replace(u'(',u'').replace(u')',u'').strip(),item1.split(u'|')[0].replace(u'(',u'').replace(u')',u'').strip()+u'‌'+item2.split(u'|')[0].replace(u'(',u'').replace(u')',u'').strip())
    text+=our_vari
with codecs.open( u'my_patch.txt',mode = 'w',encoding = 'utf8' ) as f:
    f.write( text )
