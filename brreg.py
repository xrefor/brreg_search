#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json

def name(query):
    firmnavn = query.replace(' ', '%20')
    url = "http://data.brreg.no/enhetsregisteret/enhet.json?$filter=startswith(navn,'{0}')".format(firmnavn)
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    dp = data['data'][0]
    adrF = data['data'][0]['forretningsadresse']
    try:
        print '\n'
        print '[+]Firmanavn:', dp['navn']
        print '[+]Org.Nr:', dp['organisasjonsnummer']
        print '[+]F.adr:', adrF['adresse'], adrF['postnummer'], adrF['poststed']
        print '[+]F.type:', dp['orgform']['beskrivelse']
        print '\n'
    except KeyError:
        print '[-][NO DATA]'
    

search = raw_input('\n[*]Firmanavn: ')
name(search)
