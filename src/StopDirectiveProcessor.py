#!/usr/bin/env python
# $Id: StopDirectiveProcessor.py,v 1.2 2001/08/07 22:14:17 tavis_rudd Exp $
"""StopDirectiveProcessor class Cheetah's codeGenerator

Meta-Data
================================================================================
Author: Tavis Rudd <tavis@calrudd.com>
License: This software is released for unlimited distribution under the
         terms of the Python license.
Version: $Revision: 1.2 $
Start Date: 2001/08/01
Last Revision Date: $Date: 2001/08/07 22:14:17 $
"""
__author__ = "Tavis Rudd <tavis@calrudd.com>"
__version__ = "$Revision: 1.2 $"[11:-2]

##################################################
## DEPENDENCIES ##

# intra-package imports ...
import TagProcessor
from Delimiters import delimiters
##################################################
## CONSTANTS & GLOBALS ##

True = (1==1)
False = (0==1)

##################################################
## CLASSES ##

class Error(Exception):
    pass

class StopDirectiveProcessor(TagProcessor.TagProcessor):
    _tagType = TagProcessor.EXEC_TAG_TYPE
    _token = 'stopDirective'
    _delimRegexs = [delimiters['stopDirective_gobbleWS'],
                    delimiters['stopDirective'],]    
    def translateTag(self, templateObj, tag):
        indent = templateObj.setting('indentationStep')
        
        outputCode = """%(baseInd)soutput = ''.join(outputList)
%(baseInd)sif trans and not iAmNested:
%(baseInd)s    trans.response().write(output)
%(baseInd)sreturn output
%(baseInd)s""" % {'baseInd':indent*templateObj._codeGeneratorState['indentLevel']}
        
        return outputCode