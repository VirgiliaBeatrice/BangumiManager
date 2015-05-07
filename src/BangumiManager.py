#!/usr/bin/python  
#-*-coding:utf-8-*-
'''
Created on 2015年5月3日

@author: VirgiliaBeatrice
'''
import os
# from __builtin__ import str


# print os.walk('.')
print os.path.basename('[CASO&SumiSora][Owari_no_Seraph][01][GB][720p].mp4')
print os.path.splitext('[CASO&SumiSora][Owari_no_Seraph][01][GB][720p].mp4')

def test():
    for dirpath, dirnames, filenames in os.walk(u'.'):
        print dirpath
        print dirnames
        print filenames

def tag_generator(tagstr):
    tagstr_tmp = tagstr
    while 1:
        l_idx = tagstr_tmp.find(u'[')
        r_idx = tagstr_tmp.find(u']')

        if (l_idx != -1) and (r_idx != -1):
            yield tagstr_tmp[(l_idx + 1):(r_idx)]
            tagstr_tmp = tagstr_tmp[(r_idx + 1):]
        else:
            break
    
    

#TODO: Implement analysis code.
def tag_analysis(filename):
    tag_package = {}
    all_tag = [tag for tag in tag_generator(os.path.splitext(filename)[0])]
    tag_package[u'ext'] = os.path.splitext(filename)[1]
    
    tag_package[u'othertags'] = []
    dummy_idx = 0
    
    for tag in all_tag:
        if dummy_idx == 0:
            tag_package[u'fansubs'] = fansub_analysis(tag)
        elif (dummy_idx == 1):
            tag_package[u'title'] = tag
        elif (dummy_idx == 2):
            if tag.isnumeric():
                tag_package[u'no'] = int(tag)
            else:
                tag_package[u'othertags'].append(tag)
        else:
            tag_package[u'othertags'].append(tag)
        
        dummy_idx += 1
        
    return tag_package
    
    
def fansub_analysis(fansub_string):
    return fansub_string.split(u'&')    
    
    
    
if __name__ == '__main__':
    print tag_analysis(u'[CASO&SumiSora][Owari_no_Seraph][01][GB][720p].mp4')
    pass