#!/usr/bin/python  
#-*-coding:utf-8-*-
'''
Created on 2015年5月3日

@author: VirgiliaBeatrice
'''
import os
from __builtin__ import str
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
    
    

def splittag(tagstr):
    tag_list = []
    all_tag = [tag for tag in tag_generator(tagstr)]
    
    print tag_list
    
splittag(u'[CASO&SumiSora][Owari_no_Seraph][01][GB][720p].mp4')
    
    
if __name__ == '__main__':
    pass