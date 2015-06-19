# -*- coding: utf-8 -*-

#import re
import sys
import codecs
#import getopt
#import gettext
import os
import ConfigParser

try:
    foundwx = True
    import wx
    import wx.html
    from wx.lib.wordwrap import wordwrap
    wx.SetDefaultPyEncoding("utf8")
except:
    foundwx = False

#try:
#    lang = gettext.translation('latexassistant', localedir=os.path.dirname(sys.argv[0]), languages=["en"])
#    lang.install(unicode=1)
#    langloaded = True
#except IOError:
#    print os.path.dirname(sys.argv[0])
#    print "Sprache nicht gefunden. Benutze Standardsprache."
#    def _(message):
#        return message
def _(message):
    return message

programmversion = 1

class PageOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.vsizer = wx.BoxSizer(wx.VERTICAL)

        self.hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.dclass = wx.RadioBox(self,wx.ID_ANY,_("Dokumentenklasse"),wx.DefaultPosition,wx.DefaultSize,("scrartcl","scrreprt","scrbook",_("andere:")))
        self.customclass = wx.TextCtrl(self)
        self.hsizer1.Add(self.dclass,0,wx.EXPAND)
        self.hsizer1.Add(self.customclass,0,wx.ALIGN_CENTER)

        self.hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.psize = wx.RadioBox(self,wx.ID_ANY,_("Papiergröße"),wx.DefaultPosition,wx.DefaultSize,("a5","a4","a3",_("andere:")))
        self.psize.SetSelection(1)
        self.customsize = wx.TextCtrl(self)
        self.hsizer2.Add(self.psize,0,wx.EXPAND)
        self.hsizer2.Add(self.customsize,0,wx.ALIGN_CENTER)

        self.hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        self.porientation = wx.RadioBox(self,wx.ID_ANY,_("Papierausrichtung"),wx.DefaultPosition,wx.DefaultSize,(_("Hochformat"),_("Querformat")))
        self.hsizer3.Add(self.porientation,0,wx.EXPAND)

        self.hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        self.psides = wx.RadioBox(self,wx.ID_ANY,_("Druckweise"),wx.DefaultPosition,wx.DefaultSize,(_("einseitig"),_("doppelseitig")))
        self.hsizer4.Add(self.psides,0,wx.EXPAND)

        self.hsizer5 = wx.BoxSizer(wx.HORIZONTAL)
        self.fontsize = wx.RadioBox(self,wx.ID_ANY,_("Schriftgröße"),wx.DefaultPosition,wx.DefaultSize,("10pt","11pt","12pt",_("andere:")))
        self.fontsize.SetSelection(1)
        self.customfontsize = wx.TextCtrl(self)
        self.hsizer5.Add(self.fontsize,0,wx.EXPAND)
        self.hsizer5.Add(self.customfontsize,0,wx.ALIGN_CENTER)

        self.languagebox = wx.StaticBox(self,-1,_("Sprachen"))
        self.languagesizer = wx.StaticBoxSizer(self.languagebox,wx.HORIZONTAL)
        self.langgerman = wx.CheckBox(self,label=_("Deutsch"))
        self.langgerman.SetValue(True)
        self.languagesizer.Add(self.langgerman,0,wx.EXPAND)
        self.langenglish = wx.CheckBox(self,label=_("Englisch"))
        self.languagesizer.Add(self.langenglish,0,wx.EXPAND)
        self.langfrench = wx.CheckBox(self,label=_("Französisch"))
        self.languagesizer.Add(self.langfrench,0,wx.EXPAND)
        self.langfinnish = wx.CheckBox(self,label=_("Finnisch"))
        self.languagesizer.Add(self.langfinnish,0,wx.EXPAND)
        self.langcustom = wx.CheckBox(self,label=_("andere:"))
        self.languagesizer.Add(self.langcustom,0,wx.EXPAND)
        self.tlangcustom = wx.TextCtrl(self)
        self.languagesizer.Add(self.tlangcustom,0,wx.EXPAND)

        self.titlebox = wx.StaticBox(self,-1,_("Titelei"))
        self.titlesizer = wx.StaticBoxSizer(self.titlebox,wx.VERTICAL)
        self.titlesubsizer = wx.FlexGridSizer(11,2)
        self.cbextratitle = wx.CheckBox(self, label=_("Schmutztitel"))
        self.textratitle = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cbextratitle,0,wx.EXPAND)
        self.titlesubsizer.Add(self.textratitle,0,wx.EXPAND)
        self.cbtitlehead = wx.CheckBox(self, label=_("Titelseitenkopf"))
        self.ttitlehead = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cbtitlehead,0,wx.EXPAND)
        self.titlesubsizer.Add(self.ttitlehead,0,wx.EXPAND)
        self.cbsubject = wx.CheckBox(self, label=_("Typisierung"))
        self.tsubject = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cbsubject,0,wx.EXPAND)
        self.titlesubsizer.Add(self.tsubject,0,wx.EXPAND)
        self.cbtitle = wx.CheckBox(self, label=_("Titel"))
        self.cbtitle.SetValue(True)
        self.ttitle = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cbtitle,0,wx.EXPAND)
        self.titlesubsizer.Add(self.ttitle,0,wx.EXPAND)
        self.cbsubtitle = wx.CheckBox(self, label=_("Untertitel"))
        self.tsubtitle = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cbsubtitle,0,wx.EXPAND)
        self.titlesubsizer.Add(self.tsubtitle,0,wx.EXPAND)
        self.cbauthor = wx.CheckBox(self, label=_("Autor"))
        self.cbauthor.SetValue(True)
        self.tauthor = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cbauthor,0,wx.EXPAND)
        self.titlesubsizer.Add(self.tauthor,0,wx.EXPAND)
        self.cbdate = wx.CheckBox(self, label=_("Datum"))
        self.tdate = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cbdate,0,wx.EXPAND)
        self.titlesubsizer.Add(self.tdate,0,wx.EXPAND)
        self.cbpublisher = wx.CheckBox(self, label=_("Herausgeber"))
        self.tpublisher = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cbpublisher,0,wx.EXPAND)
        self.titlesubsizer.Add(self.tpublisher,0,wx.EXPAND)
        self.cbupperback = wx.CheckBox(self, label=_("Titelrückseite oben"))
        self.tupperback = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cbupperback,0,wx.EXPAND)
        self.titlesubsizer.Add(self.tupperback,0,wx.EXPAND)
        self.cblowerback = wx.CheckBox(self, label=_("Titelrückseite unten"))
        self.tlowerback = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cblowerback,0,wx.EXPAND)
        self.titlesubsizer.Add(self.tlowerback,0,wx.EXPAND)
        self.cbdedication = wx.CheckBox(self, label=_("Widmung"))
        self.tdedication = wx.TextCtrl(self)
        self.titlesubsizer.Add(self.cbdedication,0,wx.EXPAND)
        self.titlesubsizer.Add(self.tdedication,0,wx.EXPAND)
        self.titlesizer.Add(self.titlesubsizer,0,wx.EXPAND)

        self.vsizer.Add(self.hsizer1,0,wx.EXPAND)
        self.vsizer.Add(self.hsizer2,0,wx.EXPAND)
        self.vsizer.Add(self.hsizer3,0,wx.EXPAND)
        self.vsizer.Add(self.hsizer4,0,wx.EXPAND)
        self.vsizer.Add(self.hsizer5,0,wx.EXPAND)
        self.vsizer.Add(self.languagesizer,0)
        self.vsizer.Add(self.titlesizer,0)
        self.SetSizer(self.vsizer)

class PageTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        
        self.hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.font = wx.RadioBox(self,wx.ID_ANY,_("Schriftart"),wx.DefaultPosition,wx.DefaultSize,("Latin Modern","Bera",_("andere:")))
        self.customfont = wx.TextCtrl(self)
        self.hsizer1.Add(self.font,0,wx.EXPAND)
        self.hsizer1.Add(self.customfont,0,wx.ALIGN_CENTER)
        
        self.parsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.parskip = wx.RadioBox(self,wx.ID_ANY,_("Absatzkennzeichnung"),wx.DefaultPosition,wx.DefaultSize,(_("1. Zeile eingerückt"),_("1/2 Zeile Abstand"),_("1 Zeile Abstand")))
        self.parsizer.Add(self.parskip,0,wx.EXPAND)
        
        self.hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.graphicbox = wx.StaticBox(self,-1,_("Graphik"))
        self.graphicsizer = wx.StaticBoxSizer(self.graphicbox,wx.VERTICAL)
        self.cbgraphicx = wx.CheckBox(self, label=_("Bilder einbinden"))
        self.cbgraphicx.SetToolTipString("graphicx")
        self.graphicsizer.Add(self.cbgraphicx,0,wx.EXPAND)
        self.cbtikz = wx.CheckBox(self, label=_("Bilder zeichnen"))
        self.cbtikz.SetToolTipString("tikz")
        self.graphicsizer.Add(self.cbtikz,0,wx.EXPAND)
        self.cbpgfplots = wx.CheckBox(self, label=_("Diagramme erstellen"))
        self.cbpgfplots.SetToolTipString("pfgplots")
        self.graphicsizer.Add(self.cbpgfplots,0,wx.EXPAND)
        self.hsizer2.Add(self.graphicsizer,0,wx.EXPAND)
        self.hsizer2.Add((5,-1),0)
        self.tablebox = wx.StaticBox(self,-1,_("Tabellen"))
        self.tablesizer = wx.StaticBoxSizer(self.tablebox,wx.VERTICAL)
        self.cbbooktabs = wx.CheckBox(self, label=_("schöne Tabellen"))
        self.cbbooktabs.SetToolTipString("booktabs")
        self.tablesizer.Add(self.cbbooktabs,0,wx.EXPAND)
        self.cbtabularx = wx.CheckBox(self, label=_("breite Tabellen"))
        self.cbtabularx.SetToolTipString("tabularx")
        self.tablesizer.Add(self.cbtabularx,0,wx.EXPAND)
        self.cblongtable = wx.CheckBox(self, label=_("lange Tabellen"))
        self.cblongtable.SetToolTipString("longtable")
        self.tablesizer.Add(self.cblongtable,0,wx.EXPAND)
        self.hsizer2.Add(self.tablesizer,0,wx.EXPAND)
        self.hsizer2.Add((5,-1),0)
        self.refbox = wx.StaticBox(self,-1,_("Verweise"))
        self.refsizer = wx.StaticBoxSizer(self.refbox,wx.VERTICAL)
        self.cbfancyref = wx.CheckBox(self, label=_("intelligente Verweise"))
        self.cbfancyref.SetToolTipString("fancyref")
        self.refsizer.Add(self.cbfancyref,0,wx.EXPAND)
        self.cbhyperref = wx.CheckBox(self, label=_("klickbare Links"))
        self.cbhyperref.SetToolTipString("hyperref")
        self.refsizer.Add(self.cbhyperref,0,wx.EXPAND)
        self.cbhyperrefpref = wx.CheckBox(self, label=_("Einstellungen"))
        self.cbhyperrefpref.Enable(False)
        self.refsizer.Add(self.cbhyperrefpref,0,wx.EXPAND)
        self.thyperrefpref = wx.TextCtrl(self)
        self.thyperrefpref.Enable(False)
        self.refsizer.Add(self.thyperrefpref,0,wx.ALIGN_RIGHT)
        self.hsizer2.Add(self.refsizer,0,wx.EXPAND)
        self.hsizer2.Add((5,-1),0)
        self.unitbox = wx.StaticBox(self,-1,_("Einheiten / Formeln"))
        self.unitsizer = wx.StaticBoxSizer(self.unitbox,wx.VERTICAL)
        self.cbmhchem = wx.CheckBox(self, label=_("chemische Formeln"))
        self.cbmhchem.SetToolTipString("mhchem")
        self.unitsizer.Add(self.cbmhchem,0,wx.EXPAND)
        self.cbsiunitx = wx.CheckBox(self, label=_("SI-Einheiten"))
        self.cbsiunitx.SetToolTipString("siunitx")
        self.unitsizer.Add(self.cbsiunitx,0,wx.EXPAND)
        self.cbsiunitxpref = wx.CheckBox(self, label=_("Einstellungen"))
        self.cbsiunitxpref.Enable(False)
        self.unitsizer.Add(self.cbsiunitxpref,0,wx.EXPAND)
        self.tsiunitxpref = wx.TextCtrl(self)
        self.tsiunitxpref.Enable(False)
        self.unitsizer.Add(self.tsiunitxpref,0,wx.ALIGN_RIGHT)
        self.hsizer2.Add(self.unitsizer,0,wx.EXPAND)
        
        self.miscbox = wx.StaticBox(self,-1,_("Verschiedenes"))
        self.miscsizer = wx.StaticBoxSizer(self.miscbox,wx.VERTICAL)
        self.miscsubsizer = wx.FlexGridSizer(4,2,0,5)
        self.cbenumitem = wx.CheckBox(self, label=_("Aufzählungen"))
        self.cbenumitem.SetToolTipString("enumitem")
        self.miscsubsizer.Add(self.cbenumitem,0,wx.EXPAND)
        self.cbamsmath = wx.CheckBox(self, label=_("Mathematik"))
        self.cbamsmath.SetToolTipString("amsmath")
        self.miscsubsizer.Add(self.cbamsmath,0,wx.EXPAND)
        self.cbisodate = wx.CheckBox(self, label=_("Datumsangaben"))
        self.cbisodate.SetToolTipString("isodate")
        self.miscsubsizer.Add(self.cbisodate,0,wx.EXPAND)
        self.cbsetspace = wx.CheckBox(self, label=_("Zeilenabstand"))
        self.cbsetspace.SetToolTipString("setspace")
        self.miscsubsizer.Add(self.cbsetspace,0,wx.EXPAND)
        self.cbblindtext = wx.CheckBox(self, label=_("Blindtext"))
        self.cbblindtext.SetToolTipString("blindtext")
        self.miscsubsizer.Add(self.cbblindtext,0,wx.EXPAND)
        self.cbxcolor = wx.CheckBox(self, label=_("Farbe"))
        self.cbxcolor.SetToolTipString("xcolor")
        self.miscsubsizer.Add(self.cbxcolor,0,wx.EXPAND)
        self.cbcsquotes = wx.CheckBox(self, label=_("Zitate"))
        self.cbcsquotes.SetToolTipString("csquotes")
        self.miscsubsizer.Add(self.cbcsquotes,0,wx.EXPAND)
        self.cbindex = wx.CheckBox(self, label=_("Index"))
        self.cbindex.SetToolTipString("makeindex")
        self.miscsubsizer.Add(self.cbindex,0,wx.EXPAND)
        self.miscsizer.Add(self.miscsubsizer,0,wx.EXPAND)
        
        self.bibbox = wx.StaticBox(self,-1,_("Literaturverzeichnis"))
        self.bibsizer = wx.StaticBoxSizer(self.bibbox, wx.VERTICAL)
        self.cbbiblatex = wx.CheckBox(self, label=_("Literatur"))
        self.cbbiblatex.SetToolTipString("biblatex")
        self.bibsizer.Add(self.cbbiblatex,0,wx.EXPAND)
        self.bibsubsizer = wx.FlexGridSizer(3,2)
        self.bibstyle = wx.StaticText(self, label=_("Stil"))
        self.bibstyle.SetToolTipString("style")
        self.bibstyle.Enable(False)
        self.bibsubsizer.Add(self.bibstyle,0,wx.EXPAND)
        self.tbibstyle = wx.ComboBox(self,choices=["numeric","numeric-comp","numeric-verb","alphabetic",
                                                   "alphabetic-verb","authoryear","authoryear-comp","authoryear-ibid",
                                                   "authoryear-icomp","authortitle","authortitle-comp","authortitle-ibid",
                                                   "authortitle-icomp","authortitle-terse","authortitle-tcomp","verbose",
                                                   "verbose-ibid","verbose-note","verbose-inote","verbose-trad1",
                                                   "verbose-trad2","verbose-trad3"])
        self.tbibstyle.SetToolTipString("style")
        self.tbibstyle.Enable(False)
        self.bibsubsizer.Add(self.tbibstyle,0,wx.EXPAND)
        self.bibautocite = wx.StaticText(self, label=_("Zitate"))
        self.bibautocite.SetToolTipString("autocite")
        self.bibautocite.Enable(False)
        self.bibsubsizer.Add(self.bibautocite,0,wx.EXPAND)
        self.tbibautocite = wx.ComboBox(self,choices=["plain","inline","footnote","superscript"])
        self.tbibautocite.SetToolTipString("autocite")
        self.tbibautocite.Enable(False)
        self.bibsubsizer.Add(self.tbibautocite,0,wx.EXPAND)
        self.bibbibliography = wx.StaticText(self, label=_("Literaturdatei"))
        self.bibbibliography.SetToolTipString("bibliography")
        self.bibbibliography.Enable(False)
        self.bibsubsizer.Add(self.bibbibliography,0,wx.EXPAND)
        self.tbibbibliography = wx.TextCtrl(self)
        self.tbibbibliography.SetToolTipString("bibliography")
        self.tbibbibliography.Enable(False)
        self.bibsubsizer.Add(self.tbibbibliography,0,wx.EXPAND)
        self.bibsizer.Add(self.bibsubsizer,0,wx.EXPAND)

        self.vsizer.Add(self.hsizer1,0,wx.EXPAND)
        self.vsizer.Add((-1,5),0)
        self.vsizer.Add(self.parsizer,0)
        self.vsizer.Add((-1,5),0)
        self.vsizer.Add(self.hsizer2,0,wx.EXPAND)
        self.vsizer.Add((-1,5),0)
        self.vsizer.Add(self.miscsizer,0)
        self.vsizer.Add((-1,5),0)
        self.vsizer.Add(self.bibsizer,0)
        self.SetSizer(self.vsizer)
        
        self.Bind(wx.EVT_CHECKBOX, self.ToggleHyperrefPrefs, self.cbhyperref)
        self.Bind(wx.EVT_CHECKBOX, self.ToggleSiunitxPrefs, self.cbsiunitx)
        self.Bind(wx.EVT_CHECKBOX, self.ToggleBiblatexPrefs, self.cbbiblatex)
        
    def ToggleHyperrefPrefs(self,id):
        if self.cbhyperref.GetValue():
            self.cbhyperrefpref.Enable(True)
            self.thyperrefpref.Enable(True)
        else:
            self.cbhyperrefpref.Enable(False)
            self.thyperrefpref.Enable(False)
            
    def ToggleSiunitxPrefs(self,id):
        if self.cbsiunitx.GetValue():
            self.cbsiunitxpref.Enable(True)
            self.tsiunitxpref.Enable(True)
        else:
            self.cbsiunitxpref.Enable(False)
            self.tsiunitxpref.Enable(False)
    
    def ToggleBiblatexPrefs(self,id):
        if self.cbbiblatex.GetValue():
            self.bibstyle.Enable(True)
            self.tbibstyle.Enable(True)
            self.bibautocite.Enable(True)
            self.tbibautocite.Enable(True)
            self.bibbibliography.Enable(True)
            self.tbibbibliography.Enable(True)
        else:
            self.bibstyle.Enable(False)
            self.tbibstyle.Enable(False)
            self.bibautocite.Enable(False)
            self.tbibautocite.Enable(False)
            self.bibbibliography.Enable(False)
            self.tbibbibliography.Enable(False)
        
class PageThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #self.checkbutton3 = wx.CheckBox(self, label=_("checkbox3"))
        self.LayoutFrame = wx.Panel(self,wx.ID_ANY,wx.DefaultPosition,(450,360),wx.SIMPLE_BORDER)
        #wx.StaticText(self.LayoutFrame,wx.ID_ANY,_("Kopf- und Fußzeilen: Werden mit scrpage2 gesetzt."),(10,15),(400,15))
        #wx.StaticText(self.LayoutFrame,wx.ID_ANY,_("Die Einzelfelder haben Vorrang vor den Sammelfeldern."),(10,30),(400,15))
        self.cbscrpage = wx.CheckBox(self.LayoutFrame,wx.ID_ANY, _("Kopf-/Fußzeilen"),(10,4))
        self.rbstyle = wx.RadioBox(self.LayoutFrame,wx.ID_ANY,_(""),(10,16),wx.DefaultSize,("scrplain","scrheadings"))
        self.rbstyle.Enable(False)
        self.EvenSide = wx.StaticBox(self.LayoutFrame,wx.ID_ANY,"",(10,50),(200,300))
        self.OddSide = wx.StaticBox(self.LayoutFrame,wx.ID_ANY,"",(240,50),(200,300))
        self.LEhead = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(15,59),(60,-1))
        self.LEhead.SetToolTipString("lehead")
        self.LEhead.Enable(False)
        self.CEhead = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(80,59),(60,-1))
        self.CEhead.SetToolTipString("cehead")
        self.CEhead.Enable(False)
        self.REhead = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(145,59),(60,-1))
        self.REhead.SetToolTipString("rehead")
        self.REhead.Enable(False)
        self.LOhead = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(245,59),(60,-1))
        self.LOhead.SetToolTipString("lohead")
        self.LOhead.Enable(False)
        self.COhead = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(310,59),(60,-1))
        self.COhead.SetToolTipString("cohead")
        self.COhead.Enable(False)
        self.ROhead = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(375,59),(60,-1))
        self.ROhead.SetToolTipString("rohead")
        self.ROhead.Enable(False)
        self.Ihead = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(195,100),(60,-1))
        self.Ihead.SetToolTipString("ihead")
        self.Ihead.Enable(False)
        self.Chead = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(195,130),(60,-1))
        self.Chead.SetToolTipString("chead")
        self.Chead.Enable(False)
        self.Ohead = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(195,160),(60,-1))
        self.Ohead.SetToolTipString("ohead")
        self.Ohead.Enable(False)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(175,85),(1,25),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(175,110),(15,1),wx.LI_HORIZONTAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(275,85),(1,25),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(260,110),(15,1),wx.LI_HORIZONTAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(110,85),(1,55),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(110,140),(80,1),wx.LI_HORIZONTAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(340,85),(1,55),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(260,140),(80,1),wx.LI_HORIZONTAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(45,85),(1,85),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(45,170),(145,1),wx.LI_HORIZONTAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(405,85),(1,85),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(260,170),(145,1),wx.LI_HORIZONTAL)
        self.LEfoot = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(15,323),(60,-1))
        self.LEfoot.SetToolTipString("lefoot")
        self.LEfoot.Enable(False)
        self.CEfoot = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(80,323),(60,-1))
        self.CEfoot.SetToolTipString("cefoot")
        self.CEfoot.Enable(False)
        self.REfoot = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(145,323),(60,-1))
        self.REfoot.SetToolTipString("refoot")
        self.REfoot.Enable(False)
        self.LOfoot = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(245,323),(60,-1))
        self.LOfoot.SetToolTipString("lofoot")
        self.LOfoot.Enable(False)
        self.COfoot = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(310,323),(60,-1))
        self.COfoot.SetToolTipString("cofoot")
        self.COfoot.Enable(False)
        self.ROfoot = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(375,323),(60,-1))
        self.ROfoot.SetToolTipString("rofoot")
        self.ROfoot.Enable(False)
        self.Ofoot = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(195,220),(60,-1))
        self.Ofoot.SetToolTipString("ofoot")
        self.Ofoot.Enable(False)
        self.Cfoot = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(195,250),(60,-1))
        self.Cfoot.SetToolTipString("cfoot")
        self.Cfoot.Enable(False)
        self.Ifoot = wx.TextCtrl(self.LayoutFrame,wx.ID_ANY,"",(195,280),(60,-1))
        self.Ifoot.SetToolTipString("ifoot")
        self.Ifoot.Enable(False)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(175,290),(1,25),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(175,290),(15,1),wx.LI_HORIZONTAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(275,290),(1,25),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(260,290),(15,1),wx.LI_HORIZONTAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(110,260),(1,55),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(110,260),(80,1),wx.LI_HORIZONTAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(340,260),(1,55),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(260,260),(80,1),wx.LI_HORIZONTAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(45,230),(1,85),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(45,230),(145,1),wx.LI_HORIZONTAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(405,230),(1,85),wx.LI_VERTICAL)
        wx.StaticLine(self.LayoutFrame,wx.ID_ANY,(260,230),(145,1),wx.LI_HORIZONTAL)
        
        self.tLEheadPlain = ""
        self.tCEheadPlain = ""
        self.tREheadPlain = ""
        self.tLOheadPlain = ""
        self.tCOheadPlain = ""
        self.tROheadPlain = ""
        self.tIheadPlain = ""
        self.tCheadPlain = ""
        self.tOheadPlain = ""
        self.tLEfootPlain = ""
        self.tCEfootPlain = ""
        self.tREfootPlain = ""
        self.tLOfootPlain = ""
        self.tCOfootPlain = ""
        self.tROfootPlain = ""
        self.tIfootPlain = ""
        self.tCfootPlain = ""
        self.tOfootPlain = ""
        self.tLEheadHeading = ""
        self.tCEheadHeading = ""
        self.tREheadHeading = ""
        self.tLOheadHeading = ""
        self.tCOheadHeading = ""
        self.tROheadHeading = ""
        self.tIheadHeading = ""
        self.tCheadHeading = ""
        self.tOheadHeading = ""
        self.tLEfootHeading = ""
        self.tCEfootHeading = ""
        self.tREfootHeading = ""
        self.tLOfootHeading = ""
        self.tCOfootHeading = ""
        self.tROfootHeading = ""
        self.tIfootHeading = ""
        self.tCfootHeading = ""
        self.tOfootHeading = ""
        
        self.Bind(wx.EVT_CHECKBOX, self.ToggleScrpage, self.cbscrpage)
        self.Bind(wx.EVT_RADIOBOX, self.ToggleValues, self.rbstyle)
        
    def ToggleScrpage(self,id):
        if self.cbscrpage.GetValue():
            self.rbstyle.Enable(True)
            self.LEhead.Enable(True)
            self.CEhead.Enable(True)
            self.REhead.Enable(True)
            self.LOhead.Enable(True)
            self.COhead.Enable(True)
            self.ROhead.Enable(True)
            self.Ihead.Enable(True)
            self.Chead.Enable(True)
            self.Ohead.Enable(True)
            self.LEfoot.Enable(True)
            self.CEfoot.Enable(True)
            self.REfoot.Enable(True)
            self.LOfoot.Enable(True)
            self.COfoot.Enable(True)
            self.ROfoot.Enable(True)
            self.Ifoot.Enable(True)
            self.Cfoot.Enable(True)
            self.Ofoot.Enable(True)
        else:
            self.rbstyle.Enable(False)
            self.LEhead.Enable(False)
            self.CEhead.Enable(False)
            self.REhead.Enable(False)
            self.LOhead.Enable(False)
            self.COhead.Enable(False)
            self.ROhead.Enable(False)
            self.Ihead.Enable(False)
            self.Chead.Enable(False)
            self.Ohead.Enable(False)
            self.LEfoot.Enable(False)
            self.CEfoot.Enable(False)
            self.REfoot.Enable(False)
            self.LOfoot.Enable(False)
            self.COfoot.Enable(False)
            self.ROfoot.Enable(False)
            self.Ifoot.Enable(False)
            self.Cfoot.Enable(False)
            self.Ofoot.Enable(False)
            
    def SaveValues(self,id):
        if self.rbstyle.GetSelection() == id:
            self.tLEheadPlain = self.LEhead.GetValue()
            self.tCEheadPlain = self.CEhead.GetValue()
            self.tREheadPlain = self.REhead.GetValue()
            self.tLOheadPlain = self.LOhead.GetValue()
            self.tCOheadPlain = self.COhead.GetValue()
            self.tROheadPlain = self.ROhead.GetValue()
            self.tIheadPlain = self.Ihead.GetValue()
            self.tCheadPlain = self.Chead.GetValue()
            self.tOheadPlain = self.Ohead.GetValue()
            self.tLEfootPlain = self.LEfoot.GetValue()
            self.tCEfootPlain = self.CEfoot.GetValue()
            self.tREfootPlain = self.REfoot.GetValue()
            self.tLOfootPlain = self.LOfoot.GetValue()
            self.tCOfootPlain = self.COfoot.GetValue()
            self.tROfootPlain = self.ROfoot.GetValue()
            self.tIfootPlain = self.Ifoot.GetValue()
            self.tCfootPlain = self.Cfoot.GetValue()
            self.tOfootPlain = self.Ofoot.GetValue()
        else:
            self.tLEheadHeading = self.LEhead.GetValue()
            self.tCEheadHeading = self.CEhead.GetValue()
            self.tREheadHeading = self.REhead.GetValue()
            self.tLOheadHeading = self.LOhead.GetValue()
            self.tCOheadHeading = self.COhead.GetValue()
            self.tROheadHeading = self.ROhead.GetValue()
            self.tIheadHeading = self.Ihead.GetValue()
            self.tCheadHeading = self.Chead.GetValue()
            self.tOheadHeading = self.Ohead.GetValue()
            self.tLEfootHeading = self.LEfoot.GetValue()
            self.tCEfootHeading = self.CEfoot.GetValue()
            self.tREfootHeading = self.REfoot.GetValue()
            self.tLOfootHeading = self.LOfoot.GetValue()
            self.tCOfootHeading = self.COfoot.GetValue()
            self.tROfootHeading = self.ROfoot.GetValue()
            self.tIfootHeading = self.Ifoot.GetValue()
            self.tCfootHeading = self.Cfoot.GetValue()
            self.tOfootHeading = self.Ofoot.GetValue()
        
    def LoadValues(self,id):
        if self.rbstyle.GetSelection() == 0:
            self.LEhead.ChangeValue(self.tLEheadPlain)
            self.CEhead.ChangeValue(self.tCEheadPlain)
            self.REhead.ChangeValue(self.tREheadPlain)
            self.LOhead.ChangeValue(self.tLOheadPlain)
            self.COhead.ChangeValue(self.tCOheadPlain)
            self.ROhead.ChangeValue(self.tROheadPlain)
            self.Ihead.ChangeValue(self.tIheadPlain)
            self.Chead.ChangeValue(self.tCheadPlain)
            self.Ohead.ChangeValue(self.tOheadPlain)
            self.LEfoot.ChangeValue(self.tLEfootPlain)
            self.CEfoot.ChangeValue(self.tCEfootPlain)
            self.REfoot.ChangeValue(self.tREfootPlain)
            self.LOfoot.ChangeValue(self.tLOfootPlain)
            self.COfoot.ChangeValue(self.tCOfootPlain)
            self.ROfoot.ChangeValue(self.tROfootPlain)
            self.Ifoot.ChangeValue(self.tIfootPlain)
            self.Cfoot.ChangeValue(self.tCfootPlain)
            self.Ofoot.ChangeValue(self.tOfootPlain)
        else:
            self.LEhead.ChangeValue(self.tLEheadHeading)
            self.CEhead.ChangeValue(self.tCEheadHeading)
            self.REhead.ChangeValue(self.tREheadHeading)
            self.LOhead.ChangeValue(self.tLOheadHeading)
            self.COhead.ChangeValue(self.tCOheadHeading)
            self.ROhead.ChangeValue(self.tROheadHeading)
            self.Ihead.ChangeValue(self.tIheadHeading)
            self.Chead.ChangeValue(self.tCheadHeading)
            self.Ohead.ChangeValue(self.tOheadHeading)
            self.LEfoot.ChangeValue(self.tLEfootHeading)
            self.CEfoot.ChangeValue(self.tCEfootHeading)
            self.REfoot.ChangeValue(self.tREfootHeading)
            self.LOfoot.ChangeValue(self.tLOfootHeading)
            self.COfoot.ChangeValue(self.tCOfootHeading)
            self.ROfoot.ChangeValue(self.tROfootHeading)
            self.Ifoot.ChangeValue(self.tIfootHeading)
            self.Cfoot.ChangeValue(self.tCfootHeading)
            self.Ofoot.ChangeValue(self.tOfootHeading)
        
    def ToggleValues(self,id):
        self.SaveValues(1)
        self.LoadValues(0)
        
class PageFour(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.mainsizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.refreshbutton = wx.Button(self,wx.ID_ANY,_("Aktualisieren"))
        self.copybutton = wx.Button(self,wx.ID_ANY,_("Alles kopieren"))
        self.savebutton = wx.Button(self,wx.ID_ANY,_(".tex Speichern"))
        self.buttonsizer.Add(self.refreshbutton,1,wx.EXPAND)
        self.buttonsizer.Add(self.copybutton,1,wx.EXPAND)
        self.buttonsizer.Add(self.savebutton,1,wx.EXPAND)
        self.mainsizer.Add(self.buttonsizer,0,wx.EXPAND)
        self.outputtext = wx.TextCtrl(self,wx.ID_ANY,style=wx.TE_MULTILINE)
        self.mainsizer.Add(self.outputtext,1,wx.EXPAND)
        self.SetSizer(self.mainsizer)
        
class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self, parent, id, size=(600,400)):
        wx.html.HtmlWindow.__init__(self,parent, id, size=size)
        if "gtk2" in wx.PlatformInfo:
            self.SetStandardFonts()
        
class HelpWindow(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, _("Hilfe"),
            style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|
                wx.TAB_TRAVERSAL)
        self.hwin = HtmlWindow(self, -1, size=(600,700))
        self.hwin.LoadFile(os.path.dirname(sys.argv[0])+'\\hilfe.html')
        self.btn = self.hwin.FindWindowById(wx.ID_OK)
        self.irep = self.hwin.GetInternalRepresentation()
        #self.hwin.SetSize((self.irep.GetWidth()+25, self.irep.GetHeight()+25))
        self.SetClientSize(self.hwin.GetSize())
        self.CentreOnParent(wx.BOTH)
        self.SetFocus()

class LaTeXAssistant(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(600, 700))
        #create icon
        self.icon = wx.Icon(os.path.dirname(sys.argv[0])+'pencil.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        #create menu
        self.filemenu = wx.Menu()
        self.menuopen = self.filemenu.Append(wx.ID_OPEN, _("Vorlage &Öffnen\tCtrl+O"))
        self.menusave = self.filemenu.Append(wx.ID_SAVE, _("Vorlage &Speichern\tCtrl+S"))
        self.filemenu.AppendSeparator()
        self.menuquit= self.filemenu.Append(wx.ID_EXIT, _("&Schließen"))
        self.helpmenu = wx.Menu()
        self.menuabout = self.helpmenu.Append(wx.ID_ABOUT, _("Über LaTeXAssistant"))
        self.helpmenu.AppendSeparator()
        self.menuhelp = self.helpmenu.Append(wx.ID_HELP, _("Hilfe"))
        self.menubar = wx.MenuBar()
        self.menubar.Append(self.filemenu, _("&Datei"))
        self.menubar.Append(self.helpmenu, _("&Hilfe"))
        self.SetMenuBar(self.menubar)
        #bind events to functions
        #self.Bind(wx.EVT_MENU, self.Test1, self.menuopen)
        self.Bind(wx.EVT_MENU, self.MenuQuit, self.menuquit)
        self.Bind(wx.EVT_MENU, self.SaveTemplate, self.menusave)
        self.Bind(wx.EVT_MENU, self.LoadTemplate, self.menuopen)
        self.Bind(wx.EVT_MENU, self.ShowAbout, self.menuabout)
        self.Bind(wx.EVT_MENU, self.ShowHelp, self.menuhelp)
        self.Bind(wx.EVT_CLOSE, self.CleanUp)
        #create toolbar
        #self.toolbar = self.CreateToolBar()
        #self.toolbar.AddLabelTool(wx.ID_ANY,_("&Öffnen\tCtrl+O"),wx.Bitmap('open.png'))
        #self.toolbar.Realize()
        #create sizer and notebook
        self.sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.noteb = wx.Notebook(self,-1,wx.DefaultPosition)
        #create tabs
        self.p1 = PageOne(self.noteb)
        self.p2 = PageTwo(self.noteb)
        self.p3 = PageThree(self.noteb)
        self.p4 = PageFour(self.noteb)
        self.Bind(wx.EVT_BUTTON, self.CreateOutput, self.p4.refreshbutton)
        self.Bind(wx.EVT_BUTTON, self.CopyTex, self.p4.copybutton)
        self.Bind(wx.EVT_BUTTON, self.SaveTex, self.p4.savebutton)
        #add tabs to notebook
        self.noteb.AddPage(self.p1,_("Basis"))
        self.noteb.AddPage(self.p2,_("Erweitert 1"))
        self.noteb.AddPage(self.p3,_("Erweitert 2"))
        self.noteb.AddPage(self.p4,_("Ausgabe"))
        #add everything to sizer
        self.sizer1.Add(self.noteb,1,wx.EXPAND|wx.ALL)
        #set sizer
        wx.Frame.SetSizer(self,self.sizer1)
        #create help window
        self.HelpDlg = HelpWindow()
        #show main window
        self.Show(True)
        self.CreateOutput(0)
        
    def CreateOutput(self,id):
        self.p3.SaveValues(0)
        self.p4.outputtext.Clear()
        self.p4.outputtext.AppendText("\\documentclass[")
        if self.p1.psize.GetSelection() == 0:
            self.p4.outputtext.AppendText("\n\tpaper=a5,")
        elif self.p1.psize.GetSelection() == 1:
            self.p4.outputtext.AppendText("\n\tpaper=a4,")
        elif self.p1.psize.GetSelection() == 2:
            self.p4.outputtext.AppendText("\n\tpaper=a3,")
        else:
            self.p4.outputtext.AppendText("\n\tpaper=%s,"%(self.p1.customsize.GetValue()))
        if self.p1.porientation.GetSelection() == 1:
            self.p4.outputtext.AppendText("\n\tpaper=landscape,")
        if self.p1.psides.GetSelection() == 0:
            self.p4.outputtext.AppendText("\n\ttwoside=false,")
        else:
            self.p4.outputtext.AppendText("\n\ttwoside=true,")
        if self.p1.fontsize.GetSelection() == 0:
            self.p4.outputtext.AppendText("\n\tfontsize=10pt,")
        elif self.p1.fontsize.GetSelection() == 1:
            self.p4.outputtext.AppendText("\n\tfontsize=11pt,")
        elif self.p1.fontsize.GetSelection() == 2:
            self.p4.outputtext.AppendText("\n\tfontsize=12pt,")
        else:
            self.p4.outputtext.AppendText("\n\tfontsize=%s,"%(self.p1.customfontsize.GetValue()))
        if self.p2.parskip.GetSelection() == 0:
            self.p4.outputtext.AppendText("\n\tparskip=false,")
        elif self.p2.parskip.GetSelection() == 1:
            self.p4.outputtext.AppendText("\n\tparskip=half,")
        else:
            self.p4.outputtext.AppendText("\n\tparskip=full,")
        if self.p1.dclass.GetSelection() == 0:
            self.p4.outputtext.AppendText("\n\t]{scrartcl}")
        elif self.p1.dclass.GetSelection() == 1:
            self.p4.outputtext.AppendText("\n\t]{scrreprt}")
        elif self.p1.dclass.GetSelection() == 2:
            self.p4.outputtext.AppendText("\n\t]{scrbook}")
        else:
            self.p4.outputtext.AppendText("\n\t]{%s}"%(self.p1.customclass.GetValue()))
        self.p4.outputtext.AppendText("\n\\usepackage{selinput}\n\\SelectInputMappings{adieresis={ä}, germandbls={ß},Euro={€}}")
        self.p4.outputtext.AppendText("\n\\usepackage[T1]{fontenc}")
        self.p4.outputtext.AppendText("\n\\usepackage[")
        if self.p1.langgerman.IsChecked():
            self.p4.outputtext.AppendText("ngerman,")
        if self.p1.langenglish.IsChecked():
            self.p4.outputtext.AppendText("UKenglish,")
        if self.p1.langfrench.IsChecked():
            self.p4.outputtext.AppendText("french,")
        if self.p1.langfinnish.IsChecked():
            self.p4.outputtext.AppendText("finnish,")
        if self.p1.langcustom.IsChecked():
            self.p4.outputtext.AppendText("%s"%(self.p1.tlangcustom.GetValue()))
        self.p4.outputtext.AppendText("]{babel}")
        self.p4.outputtext.AppendText("\n\\usepackage{microtype}")
        if self.p2.font.GetSelection() == 0:
            self.p4.outputtext.AppendText("\n\\usepackage{lmodern}")
        elif self.p2.font.GetSelection() == 1:
            self.p4.outputtext.AppendText("\n\\usepackage{bera}")
        else:
            self.p4.outputtext.AppendText("\n\\usepackage{%s}"%(self.p2.customfont.GetValue()))
        if self.p2.cbgraphicx.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{graphicx}")
        if self.p2.cbtikz.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{tikz}")
        if self.p2.cbpgfplots.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{pgfplots}")
        if self.p2.cbbooktabs.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{booktabs}")
        if self.p2.cbtabularx.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{tabularx")
        if self.p2.cblongtable.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{longtable}")
        if self.p2.cbenumitem.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{enumitem}")
        if self.p2.cbamsmath.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{amsmath}")
        if self.p2.cbisodate.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage[")
            if self.p1.langgerman.IsChecked():
                self.p4.outputtext.AppendText("ngerman,")
            if self.p1.langenglish.IsChecked():
                self.p4.outputtext.AppendText("UKenglish,")
            if self.p1.langfrench.IsChecked():
                self.p4.outputtext.AppendText("french,")
            if self.p1.langcustom.IsChecked():
                self.p4.outputtext.AppendText("%s"%(self.p1.tlangcustom.GetValue()))
            self.p4.outputtext.AppendText("]{isodate}")
        if self.p2.cbsetspace.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{setspace}")
        if self.p2.cbblindtext.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{blindtext}")
        if self.p2.cbxcolor.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{xcolor}")
        if self.p2.cbcsquotes.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage[babel]{csquotes}")
        if self.p2.cbbiblatex.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage[")
            self.p4.outputtext.AppendText("style=%s,"%(self.p2.tbibstyle.GetValue()))
            self.p4.outputtext.AppendText("autocite=%s,"%(self.p2.tbibautocite.GetValue()))
            if self.p2.cbhyperref.IsChecked():
                self.p4.outputtext.AppendText("hyperref=true")
            self.p4.outputtext.AppendText("]{biblatex}")
            self.p4.outputtext.AppendText("\n\t\\bibliography{%s}"%self.p2.tbibbibliography.GetValue())
        if self.p2.cbindex.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{makeidx}")
            self.p4.outputtext.AppendText("\n\\makeindex")
        if self.p2.cbfancyref.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage[")
            if self.p1.langgerman.IsChecked():
                self.p4.outputtext.AppendText("german,")
            self.p4.outputtext.AppendText("]{fancyref}")
        if self.p2.cbsiunitx.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage")
            if self.p2.cbsiunitxpref.IsChecked():
                self.p4.outputtext.AppendText("[%s]"%(self.p2.tsiunitxpref.GetValue()))
            self.p4.outputtext.AppendText("{siunitx}")
        if self.p2.cbmhchem.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage[version=3]{mhchem}")
        if self.p3.cbscrpage.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage{scrpage2}")
            if self.p3.tIheadHeading != "" or self.p3.tIheadPlain != "":
                self.p4.outputtext.AppendText("\n\ihead[%s]{%s}"%(self.p3.tIheadPlain,self.p3.tIheadHeading))
            else:
                self.p4.outputtext.AppendText("\n\\rehead[%s]{%s}\n\\lohead[%s]{%s}"%(self.p3.tREheadPlain,self.p3.tREheadHeading,self.p3.tLOheadPlain,self.p3.tLOheadHeading))
            if self.p3.tCheadHeading != "" or self.p3.tCheadPlain != "":
                self.p4.outputtext.AppendText("\n\\chead[%s]{%s}"%(self.p3.tCheadPlain,self.p3.tCheadHeading))
            else:
                self.p4.outputtext.AppendText("\n\\cehead[%s]{%s}\n\\cohead[%s]{%s}"%(self.p3.tCEheadPlain,self.p3.tCEheadHeading,self.p3.tCOheadPlain,self.p3.tCOheadHeading))
            if self.p3.tOheadHeading != "" or self.p3.tOheadPlain != "":
                self.p4.outputtext.AppendText("\n\\ohead[%s]{%s}"%(self.p3.tOheadPlain,self.p3.tOheadHeading))
            else:
                self.p4.outputtext.AppendText("\n\\lehead[%s]{%s}\n\\rohead[%s]{%s}"%(self.p3.tLEheadPlain,self.p3.tLEheadHeading,self.p3.tROheadPlain,self.p3.tROheadHeading))
            if self.p3.tIfootHeading != "" or self.p3.tIfootPlain != "":
                self.p4.outputtext.AppendText("\n\\ifoot[%s]{%s}"%(self.p3.tIfootPlain,self.p3.tIfootHeading))
            else:
                self.p4.outputtext.AppendText("\n\\refoot[%s]{%s}\n\\lofoot[%s]{%s}"%(self.p3.tREfootPlain,self.p3.tREfootHeading,self.p3.tLOfootPlain,self.p3.tLOfootHeading))
            if self.p3.tCfootHeading != "" or self.p3.tCfootPlain != "":
                self.p4.outputtext.AppendText("\n\\cfoot[%s]{%s}"%(self.p3.tCfootPlain,self.p3.tCfootHeading))
            else:
                self.p4.outputtext.AppendText("\n\\cefoot[%s]{%s}\n\\cofoot[%s]{%s}"%(self.p3.tCEfootPlain,self.p3.tCEfootHeading,self.p3.tCOfootPlain,self.p3.tCOfootHeading))
            if self.p3.tOfootHeading != "" or self.p3.tOfootPlain != "":
                self.p4.outputtext.AppendText("\n\\ofoot[%s]{%s}"%(self.p3.tOfootPlain,self.p3.tOfootHeading))
            else:
                self.p4.outputtext.AppendText("\n\\lefoot[%s]{%s}\n\\rofoot[%s]{%s}"%(self.p3.tLEfootPlain,self.p3.tLEfootHeading,self.p3.tROfootPlain,self.p3.tROfootHeading))
        if self.p2.cbhyperref.IsChecked():
            self.p4.outputtext.AppendText("\n\\usepackage")
            if self.p2.cbhyperrefpref.IsChecked():
                self.p4.outputtext.AppendText("[%s]"%(self.p2.thyperrefpref.GetValue()))
            self.p4.outputtext.AppendText("{hyperref}")
        if self.p1.cbextratitle.IsChecked():
            self.p4.outputtext.AppendText("\n\\extratitle{%s}"%(self.p1.textratitle.GetValue()))
        if self.p1.cbtitlehead.IsChecked():
            self.p4.outputtext.AppendText("\n\\titlehead{%s}"%(self.p1.ttitlehead.GetValue()))
        if self.p1.cbsubject.IsChecked():
            self.p4.outputtext.AppendText("\n\\subject{%s}"%(self.p1.tsubject.GetValue()))
        if self.p1.cbtitle.IsChecked():
            self.p4.outputtext.AppendText("\n\\title{%s}"%(self.p1.ttitle.GetValue()))
        if self.p1.cbsubtitle.IsChecked():
            self.p4.outputtext.AppendText("\n\\subtitle{%s}"%(self.p1.tsubtitle.GetValue()))
        if self.p1.cbauthor.IsChecked():
            self.p4.outputtext.AppendText("\n\\author{%s}"%(self.p1.tauthor.GetValue()))
        if self.p1.cbdate.IsChecked():
            self.p4.outputtext.AppendText("\n\\date{%s}"%(self.p1.tdate.GetValue()))
        if self.p1.cbpublisher.IsChecked():
            self.p4.outputtext.AppendText("\n\\publisher{%s}"%(self.p1.tpublisher.GetValue()))
        if self.p1.cbupperback.IsChecked():
            self.p4.outputtext.AppendText("\n\\uppertitleback{%s}"%(self.p1.tupperback.GetValue()))
        if self.p1.cblowerback.IsChecked():
            self.p4.outputtext.AppendText("\n\\lowertitleback{%s}"%(self.p1.tlowerback.GetValue()))
        if self.p1.cbdedication.IsChecked():
            self.p4.outputtext.AppendText("\n\\dedication{%s}"%(self.p1.tdedication.GetValue()))
        self.p4.outputtext.AppendText("\n\\begin{document}")
        if self.p3.cbscrpage.IsChecked():
            self.p4.outputtext.AppendText("\n\\pagestyle{scrheadings}")
        self.p4.outputtext.AppendText("\n\\end{document}")
        
    def SaveTemplate(self, event):
        self.getsavefiledlg = wx.FileDialog(self,_("Datei zum Speichern wählen"),wildcard=_("Vorlagen-Dateien|*.template|Alle Dateien|*.*"),style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        retval = self.getsavefiledlg.ShowModal()
        if retval == wx.ID_OK:
            config = ConfigParser.RawConfigParser()
            config.add_section("Version")
            config.set("Version", "programmversion", programmversion)
            
            config.add_section("Basic")
            config.set("Basic", "dclass", self.p1.dclass.GetSelection())
            config.set("Basic", "customclass", self.p1.customclass.GetValue().encode('unicode_escape'))
            config.set("Basic", "psize", self.p1.psize.GetSelection())
            config.set("Basic", "customsize", self.p1.customsize.GetValue().encode('unicode_escape'))
            config.set("Basic", "porientation", self.p1.porientation.GetSelection())
            config.set("Basic", "psides", self.p1.psides.GetSelection())
            config.set("Basic", "fontsize", self.p1.fontsize.GetSelection())
            config.set("Basic", "customfontsize", self.p1.customfontsize.GetValue().encode('unicode_escape'))
            config.set("Basic", "langgerman", self.p1.langgerman.GetValue())
            config.set("Basic", "langenglish", self.p1.langenglish.GetValue())
            config.set("Basic", "langfrench", self.p1.langfrench.GetValue())
            config.set("Basic", "langfinnish", self.p1.langfinnish.GetValue())
            config.set("Basic", "langcustom", self.p1.langcustom.GetValue())
            config.set("Basic", "tlangcustom", self.p1.tlangcustom.GetValue().encode('unicode_escape'))
            config.set("Basic", "cbextratitle", self.p1.cbextratitle.GetValue())
            config.set("Basic", "textratitle", self.p1.textratitle.GetValue().encode('unicode_escape'))
            config.set("Basic", "cbtitlehead", self.p1.cbtitlehead.GetValue())
            config.set("Basic", "ttitlehead", self.p1.ttitlehead.GetValue().encode('unicode_escape'))
            config.set("Basic", "cbsubject", self.p1.cbsubject.GetValue())
            config.set("Basic", "tsubject", self.p1.tsubject.GetValue().encode('unicode_escape'))
            config.set("Basic", "cbtitle", self.p1.cbtitle.GetValue())
            config.set("Basic", "ttitle", self.p1.ttitle.GetValue().encode('unicode_escape'))
            config.set("Basic", "cbsubtitle", self.p1.cbsubtitle.GetValue())
            config.set("Basic", "tsubtitle", self.p1.tsubtitle.GetValue().encode('unicode_escape'))
            config.set("Basic", "cbauthor", self.p1.cbauthor.GetValue())
            config.set("Basic", "tauthor", self.p1.tauthor.GetValue().encode('unicode_escape'))
            config.set("Basic", "cbdate", self.p1.cbdate.GetValue())
            config.set("Basic", "tdate", self.p1.tdate.GetValue().encode('unicode_escape'))
            config.set("Basic", "cbpublisher", self.p1.cbpublisher.GetValue())
            config.set("Basic", "tpublisher", self.p1.tpublisher.GetValue().encode('unicode_escape'))
            config.set("Basic", "cbupperback", self.p1.cbupperback.GetValue())
            config.set("Basic", "tupperback", self.p1.tupperback.GetValue().encode('unicode_escape'))
            config.set("Basic", "cblowerback", self.p1.cblowerback.GetValue())
            config.set("Basic", "tlowerback", self.p1.tlowerback.GetValue().encode('unicode_escape'))
            config.set("Basic", "cbdedication", self.p1.cbdedication.GetValue())
            config.set("Basic", "tdedication", self.p1.tdedication.GetValue().encode('unicode_escape'))
            
            config.add_section("Advanced")
            config.set("Advanced", "font", self.p2.font.GetSelection())
            config.set("Advanced", "parskip", self.p2.parskip.GetSelection())
            config.set("Advanced", "customfont", self.p2.customfont.GetValue().encode('unicode_escape'))
            config.set("Advanced", "cbgraphicx", self.p2.cbgraphicx.GetValue())
            config.set("Advanced", "cbtikz", self.p2.cbtikz.GetValue())
            config.set("Advanced", "cbpgfplots", self.p2.cbpgfplots.GetValue())
            config.set("Advanced", "cbbooktabs", self.p2.cbbooktabs.GetValue())
            config.set("Advanced", "cbtabularx", self.p2.cbtabularx.GetValue())
            config.set("Advanced", "cblongtable", self.p2.cblongtable.GetValue())
            config.set("Advanced", "cbfancyref", self.p2.cbfancyref.GetValue())
            config.set("Advanced", "cbhyperref", self.p2.cbhyperref.GetValue())
            config.set("Advanced", "cbhyperrefpref", self.p2.cbhyperrefpref.GetValue())
            config.set("Advanced", "thyperrefpref", self.p2.thyperrefpref.GetValue().encode('unicode_escape'))
            config.set("Advanced", "cbmhchem", self.p2.cbmhchem.GetValue())
            config.set("Advanced", "cbsiunitx", self.p2.cbsiunitx.GetValue())
            config.set("Advanced", "cbsiunitxpref", self.p2.cbsiunitxpref.GetValue())
            config.set("Advanced", "tsiunitxpref", self.p2.tsiunitxpref.GetValue().encode('unicode_escape'))
            config.set("Advanced", "cbenumitem", self.p2.cbenumitem.GetValue())
            config.set("Advanced", "cbamsmath", self.p2.cbamsmath.GetValue())
            config.set("Advanced", "cbisodate", self.p2.cbisodate.GetValue())
            config.set("Advanced", "cbblindtext", self.p2.cbblindtext.GetValue())
            config.set("Advanced", "cbsetspace", self.p2.cbsetspace.GetValue())
            config.set("Advanced", "cbxcolor", self.p2.cbxcolor.GetValue())
            config.set("Advanced", "cbcsquotes", self.p2.cbcsquotes.GetValue())
            config.set("Advanced", "cbindex", self.p2.cbindex.GetValue())
            config.set("Advanced", "cbbiblatex", self.p2.cbbiblatex.GetValue())
            config.set("Advanced", "tbibstyle", self.p2.tbibstyle.GetValue().encode('unicode_escape'))
            config.set("Advanced", "tbibautocite", self.p2.tbibautocite.GetValue().encode('unicode_escape'))
            config.set("Advanced", "tbibbibliography", self.p2.tbibbibliography.GetValue().encode('unicode_escape'))
            
            self.p3.SaveValues(0)
            config.add_section("Advanced2")
            config.set("Advanced2", "cbscrpage", self.p3.cbscrpage.GetValue())
            config.set("Advanced2", "tIheadPlain", self.p3.tIheadPlain.encode('unicode_escape'))
            config.set("Advanced2", "tIheadHeading", self.p3.tIheadHeading.encode('unicode_escape'))
            config.set("Advanced2", "tCheadPlain", self.p3.tCheadPlain.encode('unicode_escape'))
            config.set("Advanced2", "tCheadHeading", self.p3.tCheadHeading.encode('unicode_escape'))
            config.set("Advanced2", "tOheadPlain", self.p3.tOheadPlain.encode('unicode_escape'))
            config.set("Advanced2", "tOheadHeading", self.p3.tOheadHeading.encode('unicode_escape'))
            config.set("Advanced2", "tLEheadPlain", self.p3.tLEheadPlain.encode('unicode_escape'))
            config.set("Advanced2", "tLEheadHeading", self.p3.tLEheadHeading.encode('unicode_escape'))
            config.set("Advanced2", "tCEheadPlain", self.p3.tCEheadPlain.encode('unicode_escape'))
            config.set("Advanced2", "tCEheadHeading", self.p3.tCEheadHeading.encode('unicode_escape'))
            config.set("Advanced2", "tREheadPlain", self.p3.tREheadPlain.encode('unicode_escape'))
            config.set("Advanced2", "tREheadHeading", self.p3.tREheadHeading.encode('unicode_escape'))
            config.set("Advanced2", "tLOheadPlain", self.p3.tLOheadPlain.encode('unicode_escape'))
            config.set("Advanced2", "tLOheadHeading", self.p3.tLOheadHeading.encode('unicode_escape'))
            config.set("Advanced2", "tCOheadPlain", self.p3.tCOheadPlain.encode('unicode_escape'))
            config.set("Advanced2", "tCOheadHeading", self.p3.tCOheadHeading.encode('unicode_escape'))
            config.set("Advanced2", "tROheadPlain", self.p3.tROheadPlain.encode('unicode_escape'))
            config.set("Advanced2", "tROheadHeading", self.p3.tROheadHeading.encode('unicode_escape'))
            config.set("Advanced2", "tIfootPlain", self.p3.tIfootPlain.encode('unicode_escape'))
            config.set("Advanced2", "tIfootHeading", self.p3.tIfootHeading.encode('unicode_escape'))
            config.set("Advanced2", "tCfootPlain", self.p3.tCfootPlain.encode('unicode_escape'))
            config.set("Advanced2", "tCfootHeading", self.p3.tCfootHeading.encode('unicode_escape'))
            config.set("Advanced2", "tOfootPlain", self.p3.tOfootPlain.encode('unicode_escape'))
            config.set("Advanced2", "tOfootHeading", self.p3.tOfootHeading.encode('unicode_escape'))
            config.set("Advanced2", "tLEfootPlain", self.p3.tLEfootPlain.encode('unicode_escape'))
            config.set("Advanced2", "tLEfootHeading", self.p3.tLEfootHeading.encode('unicode_escape'))
            config.set("Advanced2", "tCEfootPlain", self.p3.tCEfootPlain.encode('unicode_escape'))
            config.set("Advanced2", "tCEfootHeading", self.p3.tCEfootHeading.encode('unicode_escape'))
            config.set("Advanced2", "tREfootPlain", self.p3.tREfootPlain.encode('unicode_escape'))
            config.set("Advanced2", "tREfootHeading", self.p3.tREfootHeading.encode('unicode_escape'))
            config.set("Advanced2", "tLOfootPlain", self.p3.tLOfootPlain.encode('unicode_escape'))
            config.set("Advanced2", "tLOfootHeading", self.p3.tLOfootHeading.encode('unicode_escape'))
            config.set("Advanced2", "tCOfootPlain", self.p3.tCOfootPlain.encode('unicode_escape'))
            config.set("Advanced2", "tCOfootHeading", self.p3.tCOfootHeading.encode('unicode_escape'))
            config.set("Advanced2", "tROfootPlain", self.p3.tROfootPlain.encode('unicode_escape'))
            config.set("Advanced2", "tROfootHeading", self.p3.tROfootHeading.encode('unicode_escape'))
            
            with codecs.open(self.getsavefiledlg.GetPath(), 'wb','utf8') as configfile:
                config.write(configfile)
            wx.MessageBox(_("Speichern erfolgreich!"),_("Vorlage Öffnen"),wx.OK)
    
    def LoadTemplate(self, event):
        self.getopenfiledlg = wx.FileDialog(self,_("Datei zum Öffnen wählen"),wildcard=_("Vorlagen-Dateien|*.template|Alle Dateien|*.*"),style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)
        retval = self.getopenfiledlg.ShowModal()
        if retval == wx.ID_OK:
            self.SomeOptionsNotLoaded = False
            config = ConfigParser.RawConfigParser()
            config.read(self.getopenfiledlg.GetPath())
            try:
                self.p1.dclass.SetSelection(config.getint("Basic", "dclass"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.customclass.SetValue(config.get("Basic", "customclass").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.psize.SetSelection(config.getint("Basic", "psize"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.customsize.SetValue(config.get("Basic", "customsize").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.porientation.SetSelection(config.getint("Basic", "porientation"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.psides.SetSelection(config.getint("Basic", "psides"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.fontsize.SetSelection(config.getint("Basic", "fontsize"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.customfontsize.SetValue(config.get("Basic", "customfontsize").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.langgerman.SetValue(config.getboolean("Basic", "langgerman"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.langenglish.SetValue(config.getboolean("Basic", "langenglish"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.langfrench.SetValue(config.getboolean("Basic", "langfrench"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.langfinnish.SetValue(config.getboolean("Basic", "langfinnish"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.langcustom.SetValue(config.getboolean("Basic", "langcustom"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.tlangcustom.SetValue(config.get("Basic", "tlangcustom").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cbextratitle.SetValue(config.getboolean("Basic", "cbextratitle"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.textratitle.SetValue(config.get("Basic", "textratitle").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cbtitlehead.SetValue(config.getboolean("Basic", "cbtitlehead"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.ttitlehead.SetValue(config.get("Basic", "ttitlehead").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cbsubject.SetValue(config.getboolean("Basic", "cbsubject"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.tsubject.SetValue(config.get("Basic", "tsubject").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cbtitle.SetValue(config.getboolean("Basic", "cbtitle"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.ttitle.SetValue(config.get("Basic", "ttitle").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cbsubtitle.SetValue(config.getboolean("Basic", "cbsubtitle"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.tsubtitle.SetValue(config.get("Basic", "tsubtitle").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cbauthor.SetValue(config.getboolean("Basic", "cbauthor"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.tauthor.SetValue(config.get("Basic", "tauthor").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cbdate.SetValue(config.getboolean("Basic", "cbdate"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.tdate.SetValue(config.get("Basic", "tdate").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cbpublisher.SetValue(config.getboolean("Basic", "cbpublisher"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.tpublisher.SetValue(config.get("Basic", "tpublisher").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cbupperback.SetValue(config.getboolean("Basic", "cbupperback"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.tupperback.SetValue(config.get("Basic", "tupperback").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cblowerback.SetValue(config.getboolean("Basic", "cblowerback"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.tlowerback.SetValue(config.get("Basic", "tlowerback").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.cbdedication.SetValue(config.getboolean("Basic", "cbdedication"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p1.tdedication.SetValue(config.get("Basic", "tdedication").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            
            try:
                self.p2.font.SetSelection(config.getint("Advanced", "font"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.customfont.SetValue(config.get("Advanced", "customfont").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.parskip.SetSelection(config.getint("Advanced", "parskip"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbgraphicx.SetValue(config.getboolean("Advanced", "cbgraphicx"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbtikz.SetValue(config.getboolean("Advanced", "cbtikz"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbpgfplots.SetValue(config.getboolean("Advanced", "cbpgfplots"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbbooktabs.SetValue(config.getboolean("Advanced", "cbbooktabs"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbtabularx.SetValue(config.getboolean("Advanced", "cbtabularx"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cblongtable.SetValue(config.getboolean("Advanced", "cblongtable"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbfancyref.SetValue(config.getboolean("Advanced", "cbfancyref"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbhyperref.SetValue(config.getboolean("Advanced", "cbhyperref"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbhyperrefpref.SetValue(config.getboolean("Advanced", "cbhyperrefpref"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.thyperrefpref.SetValue(config.get("Advanced", "thyperrefpref").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            if self.p2.cbhyperref.GetValue():
                self.p2.cbhyperrefpref.Enable()
                self.p2.thyperrefpref.Enable()
            try:
                self.p2.cbmhchem.SetValue(config.getboolean("Advanced", "cbmhchem"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbsiunitx.SetValue(config.getboolean("Advanced", "cbsiunitx"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbsiunitxpref.SetValue(config.getboolean("Advanced", "cbsiunitxpref"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.tsiunitxpref.SetValue(config.get("Advanced", "tsiunitxpref").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            if self.p2.cbsiunitx.GetValue():
                self.p2.cbsiunitxpref.Enable()
                self.p2.tsiunitxpref.Enable()
            try:
                self.p2.cbenumitem.SetValue(config.getboolean("Advanced", "cbenumitem"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbamsmath.SetValue(config.getboolean("Advanced", "cbamsmath"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbisodate.SetValue(config.getboolean("Advanced", "cbisodate"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbsetspace.SetValue(config.getboolean("Advanced", "cbsetspace"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbblindtext.SetValue(config.getboolean("Advanced", "cbblindtext"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbxcolor.SetValue(config.getboolean("Advanced", "cbxcolor"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbcsquotes.SetValue(config.getboolean("Advanced", "cbcsquotes"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbindex.SetValue(config.getboolean("Advanced", "cbindex"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.cbbiblatex.SetValue(config.getboolean("Advanced", "cbbiblatex"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.tbibstyle.SetValue(config.get("Advanced", "tbibstyle").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.tbibautocite.SetValue(config.get("Advanced", "tbibautocite").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p2.tbibbibliography.SetValue(config.get("Advanced", "tbibbibliography").decode('unicode_escape'))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            if self.p2.cbbiblatex.GetValue():
                self.p2.bibstyle.Enable()
                self.p2.tbibstyle.Enable()
                self.p2.bibautocite.Enable()
                self.p2.tbibautocite.Enable()
                self.p2.bibbibliography.Enable()
                self.p2.tbibbibliography.Enable()
            
            try:
                self.p3.cbscrpage.SetValue(config.getboolean("Advanced2","cbscrpage"))
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tIheadPlain = config.get("Advanced2", "tIheadPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tIheadHeading = config.get("Advanced2", "tIheadHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCheadPlain = config.get("Advanced2", "tCheadPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCheadHeading = config.get("Advanced2", "tCheadHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tOheadPlain = config.get("Advanced2", "tOheadPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tOheadHeading = config.get("Advanced2", "tOheadHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tLEheadPlain = config.get("Advanced2", "tLEheadPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tLEheadHeading = config.get("Advanced2", "tLEheadHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCEheadPlain = config.get("Advanced2", "tCEheadPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCEheadHeading = config.get("Advanced2", "tCEheadHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tREheadPlain = config.get("Advanced2", "tREheadPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tREheadHeading = config.get("Advanced2", "tREheadHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tLOheadPlain = config.get("Advanced2", "tLOheadPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tLOheadHeading = config.get("Advanced2", "tLOheadHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCOheadPlain = config.get("Advanced2", "tCOheadPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCOheadHeading = config.get("Advanced2", "tCOheadHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tROheadPlain = config.get("Advanced2", "tROheadPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tROheadHeading = config.get("Advanced2", "tROheadHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tIfootPlain = config.get("Advanced2", "tIfootPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tIfootHeading = config.get("Advanced2", "tIfootHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCfootPlain = config.get("Advanced2", "tCfootPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCfootHeading = config.get("Advanced2", "tCfootHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tOfootPlain = config.get("Advanced2", "tOfootPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tOfootHeading = config.get("Advanced2", "tOfootHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tLEfootPlain = config.get("Advanced2", "tLEfootPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tLEfootHeading = config.get("Advanced2", "tLEfootHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCEfootPlain = config.get("Advanced2", "tCEfootPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCEfootHeading = config.get("Advanced2", "tCEfootHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tREfootPlain = config.get("Advanced2", "tREfootPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tREfootHeading = config.get("Advanced2", "tREfootHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tLOfootPlain = config.get("Advanced2", "tLOfootPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tLOfootHeading = config.get("Advanced2", "tLOfootHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCOfootPlain = config.get("Advanced2", "tCOfootPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tCOfootHeading = config.get("Advanced2", "tCOfootHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tROfootPlain = config.get("Advanced2", "tROfootPlain").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            try:
                self.p3.tROfootHeading = config.get("Advanced2", "tROfootHeading").decode('unicode_escape')
            except ConfigParser.NoOptionError:
                self.SomeOptionsNotLoaded = True
            self.p3.LoadValues(0)
            self.p3.ToggleScrpage(0)
            
            try:
                self.version = config.getint("Version", "programmversion")
            except:
                self.version = 0
            self.message = _("Ergebnis des Ladens:\n")
            if self.version < programmversion:
                self.message = self.message + _("Vorlage wurde mit einer älteren Version von LaTeXAssistant gespeichert.\n")
            elif self.version > programmversion:
                self.message = self.message + _("Vorlage wurde mit einer neueren Version von LaTeXAssistant gespeichert.\n")
            if self.SomeOptionsNotLoaded:
                self.message = self.message + _("Einige Optionen konnten nicht geladen werden!")
            else:
                self.message = self.message + _("Laden war erfolgreich!")
            wx.MessageBox(self.message,_("Vorlage Öffnen"),wx.OK)
            self.CreateOutput(0)
    
    def CopyTex(self, event):
        #self.theClipboard = wx.Clipboard()
        if wx.TheClipboard.Open():
            wx.TheClipboard.Clear()
            wx.TheClipboard.SetData(wx.TextDataObject(self.p4.outputtext.GetValue()))
            wx.TheClipboard.Close()
    
    def SaveTex(self, event):
        self.getsavefiledlg = wx.FileDialog(self,_("Datei zum Speichern wählen"),wildcard=_("TeX-Dateien|*.tex|Alle Dateien|*.*"),style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        retval = self.getsavefiledlg.ShowModal()
        if retval == wx.ID_OK:
            with codecs.open(self.getsavefiledlg.GetPath(), 'wb','utf_8') as configfile:
                configfile.write(self.p4.outputtext.GetValue())
    
    def ShowAbout(self, event):
        info = wx.AboutDialogInfo()
        info.Name = _("LaTeXAssistant")
        info.Version = _("0.1alpha")
        info.Copyright = _("(C) 2010-2015 Thomas Helmke")
        info.Description = wordwrap(
            _("Der LaTeXAssistant hilft dabei, das Grundgerüst einer LaTeX-Datei zusammenzustellen. "
            "Dazu bietet der LaTeXAssistant verschiedene Optionen, mit denen der Nutzer sein Dokument "
            "gestalten kann."),
            350, wx.ClientDC(self.noteb))
        #info.WebSite = (_("http://www.steffiundthomas.net"), _("LaTeXAssistant Homepage"))
        #info.AddDeveloper(_("Thomas Helmke"))
        #info.AddDocWriter(_("Thomas Helmke"))
        #info.AddArtist(_("Thomas Helmke"))
        #info.AddTranslator(_("Thomas Helmke (Englisch)"))
        # info.License = wordwrap(
        #     _("Dieses Programm ist freie Software. Sie können es unter den Bedingungen der GNU General Public License, "
        #     "wie von der Free Software Foundation veröffentlicht, weitergeben und/oder modifizieren, entweder gemäß "
        #     "Version 3 der Lizenz oder (nach Ihrer Option) jeder späteren Version.     \n\n"
        #     "Die Veröffentlichung dieses Programms erfolgt in der Hoffnung, daß es Ihnen von Nutzen sein wird, aber "
        #     "OHNE IRGENDEINE GARANTIE, sogar ohne die implizite Garantie der MARKTREIFE oder der VERWENDBARKEIT FÜR "
        #     "EINEN BESTIMMTEN ZWECK. Details finden Sie in der GNU General Public License.      \n\n"
        #     "Sie sollten ein Exemplar der GNU General Public License zusammen mit diesem Programm erhalten haben. "
        #     "Falls nicht, siehe <http://www.gnu.org/licenses/>. "),
        #     350, wx.ClientDC(self.noteb))
        info.License = wordwrap(
            _("The MIT License (MIT)"
              "\n\n"
              "Copyright (c) 2015 Thomas Helmke"
              "\n\n"
              "Permission is hereby granted, free of charge, to any person obtaining a copy"
              "of this software and associated documentation files (the \"Software\"), to deal"
              "in the Software without restriction, including without limitation the rights"
              "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell"
              "copies of the Software, and to permit persons to whom the Software is"
              "furnished to do so, subject to the following conditions:"
              "\n\n"
              "The above copyright notice and this permission notice shall be included in all"
              "copies or substantial portions of the Software."
              "\n\n"
              "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR"
              "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,"
              "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE"
              "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER"
              "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,"
              "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE"
              "SOFTWARE."),
            350, wx.ClientDC(self.noteb))
        wx.AboutBox(info)

    def ShowHelp(self, event):
        self.HelpDlg.Show()
    
    def MenuQuit(self, event):
        self.Close(True)
    
    def CleanUp(self, event):
        self.HelpDlg.Destroy()
        self.Destroy()

def main():
    print _("Willkommen beim LaTeXAssistant!")
    app = wx.App(redirect=False)
    assistant = LaTeXAssistant(None, -1, _("LaTeXAssistant"))
    assistant.Show()
    app.MainLoop()
    sys.exit(1)
if __name__ == "__main__":
    main()
