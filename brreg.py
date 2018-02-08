#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import json

def name(query):
    if True:
        try:
            #Littlebit of this, little bit of that
            firmnavn = query.replace(' ', '%20')
            url = "http://data.brreg.no/enhetsregisteret/enhet.json?$filter=startswith(navn,'{0}')".format(firmnavn)
            json_obj = urllib2.urlopen(url)
            data = json.load(json_obj)
            dp = data['data'][0]
            adrF = data['data'][0]['forretningsadresse']
            gotoUrl = 'https://w2.brreg.no/enhet/sok/detalj.jsp?orgnr={0}'.format(dp['organisasjonsnummer'])

            #All the prints
            print '\n'
            print '[+]Firmanavn:', dp['navn']
            print '[+]Org.Nr:', dp['organisasjonsnummer']
            print '[+]F.adr:', adrF['adresse'], adrF['postnummer'], adrF['poststed']
            print '[+]F.type:', dp['orgform']['beskrivelse']
            print '\n'
            print '[!]Mer info:', gotoUrl,'\n'
            
        except KeyError:
            print '[-][NO DATA]'
    else:
        print '[-]Noe gikk galt...'
    
if __name__ == '__main__':
    search = raw_input('\n[*]Firmanavn: ')
    name(search)
