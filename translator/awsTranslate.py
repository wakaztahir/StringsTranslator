#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This python skript extracts string resources, calls Google translate
# and reassambles a new strings.xml as fitted for Android projects.

# run via 

# PYTHONIOENCODING=utf8 python3 awsTranslate.py OR using pythong launcher
# follow instructions

# P.S. You must have AWS CLI installed and configure on the machine!
# edited by alexVinrskis, March 2020

### LANGUAGE CODES FOR REFERENCE

#   af          Afrikaans
#   ak          Akan
#   sq          Albanian
#   am          Amharic
#   ar          Arabic
#   hy          Armenian
#   az          Azerbaijani
#   eu          Basque
#   be          Belarusian
#   bem         Bemba
#   bn          Bengali
#   bh          Bihari
#   xx-bork     Bork, bork, bork!
#   bs          Bosnian
#   br          Breton
#   bg          Bulgarian
#   km          Cambodian
#   ca          Catalan
#   chr         Cherokee
#   ny          Chichewa
#   zh-CN       Chinese (Simplified)
#   zh-TW       Chinese (Traditional)
#   co          Corsican
#   hr          Croatian
#   cs          Czech
#   da          Danish
#   nl          Dutch
#   xx-elmer    Elmer Fudd
#   en          English
#   eo          Esperanto
#   et          Estonian
#   ee          Ewe
#   fo          Faroese
#   tl          Filipino
#   fi          Finnish
#   fr          French
#   fy          Frisian
#   gaa         Ga
#   gl          Galician
#   ka          Georgian
#   de          German
#   el          Greek
#   gn          Guarani
#   gu          Gujarati
#   xx-hacker   Hacker
#   ht          Haitian Creole
#   ha          Hausa
#   haw         Hawaiian
#   iw          Hebrew
#   hi          Hindi
#   hu          Hungarian
#   is          Icelandic
#   ig          Igbo
#   id          Indonesian
#   ia          Interlingua
#   ga          Irish
#   it          Italian
#   ja          Japanese
#   jw          Javanese
#   kn          Kannada
#   kk          Kazakh
#   rw          Kinyarwanda
#   rn          Kirundi
#   xx-klingon  Klingon
#   kg          Kongo
#   ko          Korean
#   kri         Krio (Sierra Leone)
#   ku          Kurdish
#   ckb         Kurdish (Soranî)
#   ky          Kyrgyz
#   lo          Laothian
#   la          Latin
#   lv          Latvian
#   ln          Lingala
#   lt          Lithuanian
#   loz         Lozi
#   lg          Luganda
#   ach         Luo
#   mk          Macedonian
#   mg          Malagasy
#   ms          Malay
#   ml          Malayalam
#   mt          Maltese
#   mi          Maori
#   mr          Marathi
#   mfe         Mauritian Creole
#   mo          Moldavian
#   mn          Mongolian
#   sr-ME       Montenegrin
#   ne          Nepali
#   pcm         Nigerian Pidgin
#   nso         Northern Sotho
#   no          Norwegian
#   nn          Norwegian (Nynorsk)
#   oc          Occitan
#   or          Oriya
#   om          Oromo
#   ps          Pashto
#   fa          Persian
#   xx-pirate   Pirate
#   pl          Polish
#   pt-BR       Portuguese (Brazil)
#   pt-PT       Portuguese (Portugal)
#   pa          Punjabi
#   qu          Quechua
#   ro          Romanian
#   rm          Romansh
#   nyn         Runyakitara
#   ru          Russian
#   gd          Scots Gaelic
#   sr          Serbian
#   sh          Serbo-Croatian
#   st          Sesotho
#   tn          Setswanadef findall_content(xml_string, tag):

#   crs         Seychellois Creole
#   sn          Shona
#   sd          Sindhi
#   si          Sinhalese
#   sk          Slovak
#   sl          Slovenian
#   so          Somali
#   es          Spanish
#   es-419      Spanish (Latin American)
#   su          Sundanese
#   sw          Swahili
#   sv          Swedish
#   tg          Tajik
#   ta          Tamil
#   tt          Tatar
#   te          Telugu
#   th          Thai
#   ti          Tigrinya
#   to          Tonga
#   lua         Tshiluba
#   tum         Tumbuka
#   tr          Turkish
#   tk          Turkmen
#   tw          Twi
#   ug          Uighur
#   uk          Ukrainian
#   ur          Urdu
#   uz          Uzbek
#   vi          Vietnamese
#   cy          Welsh
#   wo          Wolof
#   xh          Xhosa
#   yi          Yiddish
#   yo          Yoruba
#   zu          Zulu


# MAIN PROGRAM

# import libraries
import os
import xml.etree.ElementTree as ET

import boto3


def runAwsTranslator(filePath, inputLanguage, outputLanguage, statusUpdate, outputDirectory=""):
    # create outfile in subfolder
    if not os.path.exists(outputDirectory + "values-" + outputLanguage):
        os.mkdir(outputDirectory + "values-" + outputLanguage)
    OUTFILE = outputDirectory + "values-" + outputLanguage + "\\strings.xml"

    # connect to AWS
    translate = boto3.client(service_name='translate', region_name='eu-west-1', use_ssl=True)

    # read xml structure
    tree = ET.parse(filePath)
    root = tree.getroot()

    # cycle through elements
    for i in range(len(root)):
        #	for each translatable string call the translation subroutine
        #   and replace the string by its translation,
        #   descend into each string array
        isTranslatable = root[i].get('translatable')
        if (root[i].tag == 'string') & (isTranslatable != 'false'):
            # trasnalte text and fix any possible issues traslotor creates: messing up HTML tags, adding spaces
            # between string formatting elements
            totranslate = root[i].text
            if (totranslate != None):
                translated = translate.translate_text(Text=totranslate, SourceLanguageCode=inputLanguage,
                                                      TargetLanguageCode=outputLanguage).get(
                    'TranslatedText').replace('\\ ', '\\').replace('\\ n ', '\\n').replace('\\n ', '\\n').replace('/ ',
                                                                                                                  '/')
                statusUpdate(outputLanguage + ":" + totranslate + "->" + translated)
                root[i].text = translated

            # if string was broken down due to HTML tags, reassemble it
            if len(root[i]) != 0:
                for element in range(len(root[i])):
                    root[i][element].text = " " + translate.translate_text(Text=root[i][element].text,
                                                                           SourceLanguageCode=inputLanguage,
                                                                           TargetLanguageCode=outputLanguage).get(
                        'TranslatedText').replace('\\ ', '\\').replace('\\ n ', '\\n').replace('\\n ', '\\n').replace(
                        '/ ', '/')
                    root[i][element].tail = " " + translate.translate_text(Text=root[i][element].tail,
                                                                           SourceLanguageCode=inputLanguage,
                                                                           TargetLanguageCode=outputLanguage).get(
                        'TranslatedText').replace('\\ ', '\\').replace('\\ n ', '\\n').replace('\\n ', '\\n').replace(
                        '/ ', '/')

        if root[i].tag == 'string-array':
            for j in range(len(root[i])):
                #	for each translatable string call the translation subroutine
                #   and replace the string by its translation,
                isTranslatable = root[i][j].get('translatable')
                if (root[i][j].tag == 'item') & (isTranslatable != 'false'):
                    # trasnalte text and fix any possible issues traslotor creates: messing up HTML tags,
                    # adding spaces between string formatting elements
                    totranslate = root[i][j].text
                    if totranslate != None:
                        root[i][j].text = translate.translate_text(Text=totranslate, SourceLanguageCode=inputLanguage,
                                                                   TargetLanguageCode=outputLanguage).get(
                            'TranslatedText').replace('\\ ', '\\').replace('\\ n ', '\\n').replace('\\n ',
                                                                                                   '\\n').replace('/ ',
                                                                                                                  '/')

                    # if string was broken down due to HTML tags, reassemble it
                    if len(root[i][j]) != 0:
                        for element in range(len(root[i][j])):
                            root[i][j][element].text = " " + translate.translate_text(Text=root[i][j][element].text,
                                                                                      SourceLanguageCode=inputLanguage,
                                                                                      TargetLanguageCode=outputLanguage).get(
                                'TranslatedText').replace('\\ ', '\\').replace('\\ n ', '\\n').replace('\\n ',
                                                                                                       '\\n').replace(
                                '/ ', '/')
                            root[i][j][element].tail = " " + translate.translate_text(Text=root[i][j][element].tail,
                                                                                      SourceLanguageCode=inputLanguage,
                                                                                      TargetLanguageCode=outputLanguage).get(
                                'TranslatedText').replace('\\ ', '\\').replace('\\ n ', '\\n').replace('\\n ',
                                                                                                       '\\n').replace(
                                '/ ', '/')

    # write new xml file
    statusUpdate(outputLanguage + ":Writing to a file")
    tree.write(OUTFILE, encoding='utf-8')
