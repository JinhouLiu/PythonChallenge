# !/usr/bin/python
# coding=utf-8
#author liujinhou
#email 18070156983@163.com     
import string
original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu  ynnjw ml rfc spj."
table=string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print original.translate(table)
text="map"
print text.translate(table)
raw_input()  
