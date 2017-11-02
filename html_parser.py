# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:01:32 2017

@author: I.SERRA
"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_data(self, data):
        self.output.append(data)
    def feed(self, data):
        self.output = []
        HTMLParser.feed(self, data)

   

 

