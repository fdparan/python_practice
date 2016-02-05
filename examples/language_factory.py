#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/"""


class languageGetter(object):
    
    def __init__(self, **vocabulary):
        self.trans = vocabulary
    
    def get(self, msgid):
        """We'll punt if we don't have a translation"""
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class TagalogGetter(languageGetter):

    """A simple localizer a la gettext"""
    def __init__(self, **kwargs):
        languageGetter.__init__(self, dog="aso", parrot='loro', cat="pusa", bear="oso")
        self.trans.update((kwargs))

class EnglishGetter(languageGetter):
    
    """Simply echoes the msg ids"""
    def get(self, msgid):
        return str(msgid)

def get_localizer(language="English"):
    
    """The factory method"""
    languages = dict(English=EnglishGetter, Filipino=TagalogGetter)
    return languages[language]()

if __name__ == '__main__':
    
    midwestEnglish = EnglishGetter(softdrink = 'pop')
    print(midwestEnglish.get('softdrink'))
    
    # Create our localizers
    e, g = get_localizer(language="English"), get_localizer(language="Filipino")
    # Localize some text
    for msgid in "dog parrot cat bear".split():
        print(e.get(msgid), g.get(msgid))
