#!/usr/bin/python
width=40
title='购物清单'
print('+'+'-'*(width-2)+'+')
h=int((width-2-len(title)*2)/2)
print('|'+'-'*h+f'{title}'+'-'*h+'|')
print('+'+'-'*(width-2)+'+')
