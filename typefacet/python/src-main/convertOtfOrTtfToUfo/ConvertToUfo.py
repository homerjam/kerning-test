'''
robofont-extensions-and-scripts
ConvertToUfo.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com

Apache License

Version 2.0, January 2004

http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.

"Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:

You must give any other recipients of the Work or Derivative Works a copy of this License; and

You must cause any modified files to carry prominent notices stating that You changed the files; and

You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and

If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License. You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS
'''


#import locale
#import math
import os
import shutil
#import tempfile
#import traceback
#import zipfile

#import freetype
#import freetype.ft_structs as ft_structs
#import freetype.ft_enums as ft_enums

#import pystache
import robofab.world

from CtuSettings import CtuSettings
from tfs.common.TFSPoint import TFSPoint
from tfs.common.TFSPath import TFSPath
from tfs.common.TFSSegment import TFSSegment

#from tfs.common.TFSPath import polygonWithPoints, debugPaths, isClosedPathClockwise
#from collections import defaultdict
from tfs.common.TFSMap import TFSMap
#from tfs.common.UnicodeCharacterNames import getUnicodeCharacterName, getUnicodeLongName
from tfs.common.TFSFont import TFSFont
from tfs.common.TFFreetypeFont import TFFreetypeFont


class ConvertToUfo(object):

    def configure(self):
        if self.src_file is None:
            raise Exception('Missing src_file')
        if not (os.path.exists(self.src_file) and os.path.isfile(self.src_file)):
            raise Exception('Invalid src_file: %s' % self.src_file)

        if self.dst_file is None:
            raise Exception('Missing dst_file')
        if os.path.exists(self.dst_file):
            if os.path.isdir(self.dst_file):
                shutil.rmtree(self.dst_file)
            elif os.path.isfile(self.dst_file):
                os.unlink(self.dst_file)
            if os.path.exists(self.dst_file):
                raise Exception('Could not overwrite: %s' % (self.dst_file,))


    def createUfo(self, ftFont):
        familyName = ftFont.familyName
        styleName = ftFont.styleName
        print 'familyName', familyName
        print 'styleName', styleName

        if not familyName:
            raise Exception('Font missing familyName')

        if not styleName:
            raise Exception('Font missing styleName')

        ufoFont = robofab.world.NewFont(familyName=familyName, styleName=styleName)
#        ufoFont.info.autoNaming()


#        def formatOpentypeScalar(value):
#            return int(round(opentype_multiplier * value))
#
        ufoFont.info.ascender = ftFont.ascender
        ufoFont.info.descender = ftFont.descender
        ufoFont.info.unitsPerEm = ftFont.unitsPerEm

        '''
        TODO: there's a lot more metadata to fill in:

        http://unifiedfontobject.org/versions/ufo2/fontinfo.html
        '''
#        ufoFont.info.xHeight = metadata.xHeight
#        ufoFont.info.capHeight = metadata.capHeight
#        ufoFont.info.versionMajor = metadata.versionMajor
#        ufoFont.info.versionMinor = metadata.versionMinor
#
#        ufoFont.info.italicAngle = metadata.italicAngle
#        #ufoFont.info.openTypeHeadFlags = metadata.openTypeHeadFlags
#        ufoFont.info.openTypeHheaAscender = ufoFont.info.ascender
#        ufoFont.info.openTypeHheaDescender = ufoFont.info.descender
#        ufoFont.info.openTypeHheaCaretSlopeRise = metadata.caretSlopeRise
#        ufoFont.info.openTypeHheaCaretSlopeRun = metadata.caretSlopeRun
#        ufoFont.info.openTypeHheaCaretOffset = 0
#
#        ufoFont.update()
#
#
#        ufoFont.info.styleMapFamilyName = ufoFont.info.familyName
#        ufoFont.info.styleMapStyleName = ufoFont.info.styleName

#        ufoFont.info.openTypeNamePreferredFamilyName = ufoFont.info.familyName
#        ufoFont.info.openTypeNamePreferredSubfamilyName = ufoFont.info.styleName
#        ufoFont.info.fullName = ufoFont.info.familyName + '-' + ufoFont.info.styleName
#        ufoFont.info.ufoFontName = ufoFont.info.fullName.replace(' ', '')
#        #ufoFont.info.postscriptUniqueID = ufoFont.info.ufoFontName
#        ufoFont.info.postscriptFontName = ufoFont.info.ufoFontName
#        ufoFont.info.postscriptFullName = ufoFont.info.fullName
#        #ufoFont.info.weightName = ufoFont.info.fullName
#        #ufoFont.info.postscriptFullName = ufoFont.info.fullName
#        # TODO: remove
#        ufoFont.info.menuName = ufoFont.info.fullName
#        # TODO: remove
#        ufoFont.info.fondName = ufoFont.info.familyName
#        ufoFont.info.macintoshFONDName = ufoFont.info.familyName
#
#        ufoFont.info.otFamilyName = ufoFont.info.familyName
#        ufoFont.info.otStyleName = ufoFont.info.styleName
#        ufoFont.info.otMacName = ufoFont.info.fullName
#        ufoFont.info.openTypeNameCompatibleFullName = ufoFont.info.fullName
#
#        ufoFont.info.designer = metadata.designer
#        ufoFont.info.openTypeNameDesigner = metadata.designer
#        ufoFont.info.createdBy = metadata.designer
#        ufoFont.info.year = metadata.year
#        # TODO: openTypeNameLicense
#        # TODO: openTypeNameLicenseURL
#
#        ufoFont.update()
#        ufoFont.autoUnicodes()
#        ufoFont.update()
#        ufoFont.save(dstFile)
#
#        ufoFont.close()
        return ufoFont


    def convertGlyph(self, ftFont, ufoFont, glyphInfo):

#        print 'convertGlyph', glyphInfo.characterCode, glyphInfo.glyphIndex

        contours, xAdvance = ftFont.getGlyphContours(glyphInfo.glyphIndex)

        ufoGlyph = ufoFont.insertGlyph(glyphInfo.characterCode, contours, xAdvance,
                                       glyphName=glyphInfo.glyphName,
                                       correctDirection=False)
#        print '\t', 'writing glyph', ufoGlyph.name, 'characterCode', glyphInfo.characterCode, hex(glyphInfo.characterCode) if glyphInfo.characterCode is not None else '<None>'
        return ufoGlyph


    def convertKerning(self, ftFont, ufoFont, glyphInfos):

        if not ftFont.has_kerning:
            return

        for glyphInfo0 in glyphInfos:
            for glyphInfo1 in glyphInfos:
                kerning = ftFont.getKerning(glyphInfo0.glyphIndex, glyphInfo1.glyphIndex)
                if kerning != 0:
                    ufoFont.setKerningPair(glyphInfo0.glyphName,
                                           glyphInfo1.glyphName, kerning)


    def convertFont(self):
        ftFont = TFFreetypeFont(self.src_file)

        ufoFont = self.createUfo(ftFont)
        ufoFont = TFSFont(ufoFont)

        glyphInfos = ftFont.getGlyphInfos()

        convertedGlyphIndices = set()
        for glyphInfo in glyphInfos:
            self.convertGlyph(ftFont, ufoFont, glyphInfo)
            convertedGlyphIndices.add(glyphInfo.glyphIndex)


        for glyphIndex in ftFont.getGlyphIndices():
            if glyphIndex not in convertedGlyphIndices:
                print 'Could not convert glyph', glyphIndex

        self.convertKerning(ftFont, ufoFont, glyphInfos)

        ufoFont.update()
        ufoFont.save(self.dst_file)
        ufoFont.close()


    def process(self):
        self.configure()
        self.convertFont()


if __name__ == "__main__":
    import sys
    print 'sys.argv', sys.argv

    ctu = ConvertToUfo()
    settings = CtuSettings(ctu).getCommandLineSettings()
    ctu.process()

    print
    print 'complete.'
