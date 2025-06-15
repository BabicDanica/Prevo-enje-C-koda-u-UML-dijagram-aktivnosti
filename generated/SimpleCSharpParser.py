# Generated from grammars/SimpleCSharpParser.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,103,437,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,1,0,1,0,1,0,5,0,88,8,0,10,0,12,0,91,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,5,1,99,8,1,10,1,12,1,102,9,1,1,1,1,1,1,2,1,
        2,1,2,1,2,5,2,110,8,2,10,2,12,2,113,9,2,1,2,1,2,5,2,117,8,2,10,2,
        12,2,120,9,2,1,2,1,2,1,3,3,3,125,8,3,1,3,1,3,1,3,1,3,5,3,131,8,3,
        10,3,12,3,134,9,3,1,3,1,3,1,4,1,4,1,5,3,5,141,8,5,1,5,1,5,3,5,145,
        8,5,1,5,1,5,3,5,149,8,5,1,5,3,5,152,8,5,1,6,1,6,1,6,3,6,157,8,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,166,8,7,1,7,1,7,1,7,1,8,1,8,1,8,
        5,8,174,8,8,10,8,12,8,177,9,8,1,9,1,9,1,9,1,10,3,10,183,8,10,1,10,
        1,10,1,10,1,10,3,10,189,8,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,206,8,12,1,13,1,13,
        5,13,210,8,13,10,13,12,13,213,9,13,1,13,1,13,1,14,1,14,1,14,1,15,
        1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,230,8,16,1,17,
        1,17,1,17,3,17,235,8,17,1,17,1,17,3,17,239,8,17,1,17,1,17,3,17,243,
        8,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,254,8,18,
        1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,5,22,278,8,22,10,22,
        12,22,281,9,22,1,22,1,22,1,23,4,23,286,8,23,11,23,12,23,287,1,23,
        4,23,291,8,23,11,23,12,23,292,1,24,1,24,1,24,1,24,1,24,1,24,3,24,
        301,8,24,1,25,1,25,1,25,4,25,306,8,25,11,25,12,25,307,1,25,3,25,
        311,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,28,
        1,28,3,28,325,8,28,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,30,1,30,
        3,30,336,8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,5,31,
        347,8,31,10,31,12,31,350,9,31,1,32,1,32,1,32,1,32,1,32,1,32,5,32,
        358,8,32,10,32,12,32,361,9,32,1,33,1,33,1,33,1,33,1,33,1,33,5,33,
        369,8,33,10,33,12,33,372,9,33,1,34,1,34,1,34,1,34,1,34,1,34,5,34,
        380,8,34,10,34,12,34,383,9,34,1,35,1,35,1,35,1,35,1,35,1,35,5,35,
        391,8,35,10,35,12,35,394,9,35,1,36,1,36,1,36,3,36,399,8,36,1,37,
        1,37,5,37,403,8,37,10,37,12,37,406,9,37,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,3,38,416,8,38,1,38,1,38,1,38,1,38,1,38,3,38,423,8,
        38,1,39,1,39,1,40,1,40,1,41,1,41,1,41,5,41,432,8,41,10,41,12,41,
        435,9,41,1,41,0,5,62,64,66,68,70,42,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,72,74,76,78,80,82,0,9,1,0,33,36,3,0,17,23,25,25,56,56,1,
        0,72,73,1,0,74,77,1,0,61,62,1,0,63,65,3,0,61,62,80,80,87,88,1,0,
        87,88,3,0,26,26,54,55,57,60,450,0,89,1,0,0,0,2,94,1,0,0,0,4,105,
        1,0,0,0,6,124,1,0,0,0,8,137,1,0,0,0,10,151,1,0,0,0,12,153,1,0,0,
        0,14,161,1,0,0,0,16,170,1,0,0,0,18,178,1,0,0,0,20,182,1,0,0,0,22,
        192,1,0,0,0,24,205,1,0,0,0,26,207,1,0,0,0,28,216,1,0,0,0,30,219,
        1,0,0,0,32,222,1,0,0,0,34,231,1,0,0,0,36,253,1,0,0,0,38,255,1,0,
        0,0,40,261,1,0,0,0,42,269,1,0,0,0,44,275,1,0,0,0,46,285,1,0,0,0,
        48,300,1,0,0,0,50,302,1,0,0,0,52,312,1,0,0,0,54,319,1,0,0,0,56,322,
        1,0,0,0,58,328,1,0,0,0,60,335,1,0,0,0,62,337,1,0,0,0,64,351,1,0,
        0,0,66,362,1,0,0,0,68,373,1,0,0,0,70,384,1,0,0,0,72,398,1,0,0,0,
        74,400,1,0,0,0,76,422,1,0,0,0,78,424,1,0,0,0,80,426,1,0,0,0,82,428,
        1,0,0,0,84,88,3,2,1,0,85,88,3,4,2,0,86,88,3,6,3,0,87,84,1,0,0,0,
        87,85,1,0,0,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,
        0,0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,93,5,0,0,1,93,1,1,0,0,0,94,
        95,5,32,0,0,95,100,5,56,0,0,96,97,5,94,0,0,97,99,5,56,0,0,98,96,
        1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,
        0,0,0,102,100,1,0,0,0,103,104,5,92,0,0,104,3,1,0,0,0,105,106,5,31,
        0,0,106,111,5,56,0,0,107,108,5,94,0,0,108,110,5,56,0,0,109,107,1,
        0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,114,1,
        0,0,0,113,111,1,0,0,0,114,118,5,97,0,0,115,117,3,6,3,0,116,115,1,
        0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,121,1,
        0,0,0,120,118,1,0,0,0,121,122,5,98,0,0,122,5,1,0,0,0,123,125,7,0,
        0,0,124,123,1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,127,5,27,
        0,0,127,128,5,56,0,0,128,132,5,97,0,0,129,131,3,10,5,0,130,129,1,
        0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,135,1,
        0,0,0,134,132,1,0,0,0,135,136,5,98,0,0,136,7,1,0,0,0,137,138,7,0,
        0,0,138,9,1,0,0,0,139,141,3,8,4,0,140,139,1,0,0,0,140,141,1,0,0,
        0,141,142,1,0,0,0,142,152,3,14,7,0,143,145,3,8,4,0,144,143,1,0,0,
        0,144,145,1,0,0,0,145,146,1,0,0,0,146,152,3,12,6,0,147,149,3,8,4,
        0,148,147,1,0,0,0,148,149,1,0,0,0,149,150,1,0,0,0,150,152,3,20,10,
        0,151,140,1,0,0,0,151,144,1,0,0,0,151,148,1,0,0,0,152,11,1,0,0,0,
        153,154,5,56,0,0,154,156,5,95,0,0,155,157,3,16,8,0,156,155,1,0,0,
        0,156,157,1,0,0,0,157,158,1,0,0,0,158,159,5,96,0,0,159,160,3,26,
        13,0,160,13,1,0,0,0,161,162,3,22,11,0,162,163,5,56,0,0,163,165,5,
        95,0,0,164,166,3,16,8,0,165,164,1,0,0,0,165,166,1,0,0,0,166,167,
        1,0,0,0,167,168,5,96,0,0,168,169,3,26,13,0,169,15,1,0,0,0,170,175,
        3,18,9,0,171,172,5,93,0,0,172,174,3,18,9,0,173,171,1,0,0,0,174,177,
        1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,17,1,0,0,0,177,175,1,
        0,0,0,178,179,3,22,11,0,179,180,5,56,0,0,180,19,1,0,0,0,181,183,
        5,43,0,0,182,181,1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,184,185,
        3,22,11,0,185,188,5,56,0,0,186,187,5,66,0,0,187,189,3,58,29,0,188,
        186,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,191,5,92,0,0,191,
        21,1,0,0,0,192,193,7,1,0,0,193,23,1,0,0,0,194,206,3,26,13,0,195,
        206,3,32,16,0,196,206,3,34,17,0,197,206,3,38,19,0,198,206,3,40,20,
        0,199,206,3,42,21,0,200,206,3,50,25,0,201,206,3,56,28,0,202,206,
        3,28,14,0,203,206,3,20,10,0,204,206,3,30,15,0,205,194,1,0,0,0,205,
        195,1,0,0,0,205,196,1,0,0,0,205,197,1,0,0,0,205,198,1,0,0,0,205,
        199,1,0,0,0,205,200,1,0,0,0,205,201,1,0,0,0,205,202,1,0,0,0,205,
        203,1,0,0,0,205,204,1,0,0,0,206,25,1,0,0,0,207,211,5,97,0,0,208,
        210,3,24,12,0,209,208,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,
        212,1,0,0,0,212,214,1,0,0,0,213,211,1,0,0,0,214,215,5,98,0,0,215,
        27,1,0,0,0,216,217,5,9,0,0,217,218,5,92,0,0,218,29,1,0,0,0,219,220,
        3,58,29,0,220,221,5,92,0,0,221,31,1,0,0,0,222,223,5,1,0,0,223,224,
        5,95,0,0,224,225,3,58,29,0,225,226,5,96,0,0,226,229,3,24,12,0,227,
        228,5,2,0,0,228,230,3,24,12,0,229,227,1,0,0,0,229,230,1,0,0,0,230,
        33,1,0,0,0,231,232,5,4,0,0,232,234,5,95,0,0,233,235,3,36,18,0,234,
        233,1,0,0,0,234,235,1,0,0,0,235,236,1,0,0,0,236,238,5,92,0,0,237,
        239,3,58,29,0,238,237,1,0,0,0,238,239,1,0,0,0,239,240,1,0,0,0,240,
        242,5,92,0,0,241,243,3,58,29,0,242,241,1,0,0,0,242,243,1,0,0,0,243,
        244,1,0,0,0,244,245,5,96,0,0,245,246,3,24,12,0,246,35,1,0,0,0,247,
        248,3,22,11,0,248,249,5,56,0,0,249,250,5,66,0,0,250,251,3,58,29,
        0,251,254,1,0,0,0,252,254,3,58,29,0,253,247,1,0,0,0,253,252,1,0,
        0,0,254,37,1,0,0,0,255,256,5,3,0,0,256,257,5,95,0,0,257,258,3,58,
        29,0,258,259,5,96,0,0,259,260,3,24,12,0,260,39,1,0,0,0,261,262,5,
        5,0,0,262,263,3,24,12,0,263,264,5,3,0,0,264,265,5,95,0,0,265,266,
        3,58,29,0,266,267,5,96,0,0,267,268,5,92,0,0,268,41,1,0,0,0,269,270,
        5,6,0,0,270,271,5,95,0,0,271,272,3,58,29,0,272,273,5,96,0,0,273,
        274,3,44,22,0,274,43,1,0,0,0,275,279,5,97,0,0,276,278,3,46,23,0,
        277,276,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,
        280,282,1,0,0,0,281,279,1,0,0,0,282,283,5,98,0,0,283,45,1,0,0,0,
        284,286,3,48,24,0,285,284,1,0,0,0,286,287,1,0,0,0,287,285,1,0,0,
        0,287,288,1,0,0,0,288,290,1,0,0,0,289,291,3,24,12,0,290,289,1,0,
        0,0,291,292,1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,47,1,0,0,
        0,294,295,5,7,0,0,295,296,3,80,40,0,296,297,5,91,0,0,297,301,1,0,
        0,0,298,299,5,8,0,0,299,301,5,91,0,0,300,294,1,0,0,0,300,298,1,0,
        0,0,301,49,1,0,0,0,302,303,5,12,0,0,303,305,3,26,13,0,304,306,3,
        52,26,0,305,304,1,0,0,0,306,307,1,0,0,0,307,305,1,0,0,0,307,308,
        1,0,0,0,308,310,1,0,0,0,309,311,3,54,27,0,310,309,1,0,0,0,310,311,
        1,0,0,0,311,51,1,0,0,0,312,313,5,13,0,0,313,314,5,95,0,0,314,315,
        3,22,11,0,315,316,5,56,0,0,316,317,5,96,0,0,317,318,3,26,13,0,318,
        53,1,0,0,0,319,320,5,14,0,0,320,321,3,26,13,0,321,55,1,0,0,0,322,
        324,5,11,0,0,323,325,3,58,29,0,324,323,1,0,0,0,324,325,1,0,0,0,325,
        326,1,0,0,0,326,327,5,92,0,0,327,57,1,0,0,0,328,329,3,60,30,0,329,
        59,1,0,0,0,330,331,3,74,37,0,331,332,5,66,0,0,332,333,3,58,29,0,
        333,336,1,0,0,0,334,336,3,62,31,0,335,330,1,0,0,0,335,334,1,0,0,
        0,336,61,1,0,0,0,337,338,6,31,-1,0,338,339,3,64,32,0,339,348,1,0,
        0,0,340,341,10,3,0,0,341,342,5,79,0,0,342,347,3,64,32,0,343,344,
        10,2,0,0,344,345,5,78,0,0,345,347,3,64,32,0,346,340,1,0,0,0,346,
        343,1,0,0,0,347,350,1,0,0,0,348,346,1,0,0,0,348,349,1,0,0,0,349,
        63,1,0,0,0,350,348,1,0,0,0,351,352,6,32,-1,0,352,353,3,66,33,0,353,
        359,1,0,0,0,354,355,10,2,0,0,355,356,7,2,0,0,356,358,3,66,33,0,357,
        354,1,0,0,0,358,361,1,0,0,0,359,357,1,0,0,0,359,360,1,0,0,0,360,
        65,1,0,0,0,361,359,1,0,0,0,362,363,6,33,-1,0,363,364,3,68,34,0,364,
        370,1,0,0,0,365,366,10,2,0,0,366,367,7,3,0,0,367,369,3,68,34,0,368,
        365,1,0,0,0,369,372,1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,
        67,1,0,0,0,372,370,1,0,0,0,373,374,6,34,-1,0,374,375,3,70,35,0,375,
        381,1,0,0,0,376,377,10,2,0,0,377,378,7,4,0,0,378,380,3,70,35,0,379,
        376,1,0,0,0,380,383,1,0,0,0,381,379,1,0,0,0,381,382,1,0,0,0,382,
        69,1,0,0,0,383,381,1,0,0,0,384,385,6,35,-1,0,385,386,3,72,36,0,386,
        392,1,0,0,0,387,388,10,2,0,0,388,389,7,5,0,0,389,391,3,72,36,0,390,
        387,1,0,0,0,391,394,1,0,0,0,392,390,1,0,0,0,392,393,1,0,0,0,393,
        71,1,0,0,0,394,392,1,0,0,0,395,396,7,6,0,0,396,399,3,72,36,0,397,
        399,3,74,37,0,398,395,1,0,0,0,398,397,1,0,0,0,399,73,1,0,0,0,400,
        404,3,76,38,0,401,403,7,7,0,0,402,401,1,0,0,0,403,406,1,0,0,0,404,
        402,1,0,0,0,404,405,1,0,0,0,405,75,1,0,0,0,406,404,1,0,0,0,407,423,
        3,78,39,0,408,423,5,56,0,0,409,410,5,56,0,0,410,411,5,94,0,0,411,
        423,5,56,0,0,412,413,5,56,0,0,413,415,5,95,0,0,414,416,3,82,41,0,
        415,414,1,0,0,0,415,416,1,0,0,0,416,417,1,0,0,0,417,423,5,96,0,0,
        418,419,5,95,0,0,419,420,3,58,29,0,420,421,5,96,0,0,421,423,1,0,
        0,0,422,407,1,0,0,0,422,408,1,0,0,0,422,409,1,0,0,0,422,412,1,0,
        0,0,422,418,1,0,0,0,423,77,1,0,0,0,424,425,7,8,0,0,425,79,1,0,0,
        0,426,427,3,58,29,0,427,81,1,0,0,0,428,433,3,58,29,0,429,430,5,93,
        0,0,430,432,3,58,29,0,431,429,1,0,0,0,432,435,1,0,0,0,433,431,1,
        0,0,0,433,434,1,0,0,0,434,83,1,0,0,0,435,433,1,0,0,0,42,87,89,100,
        111,118,124,132,140,144,148,151,156,165,175,182,188,205,211,229,
        234,238,242,253,279,287,292,300,307,310,324,335,346,348,359,370,
        381,392,398,404,415,422,433
    ]

class SimpleCSharpParser ( Parser ):

    grammarFileName = "SimpleCSharpParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'for'", 
                     "'do'", "'switch'", "'case'", "'default'", "'break'", 
                     "'continue'", "'return'", "'try'", "'catch'", "'finally'", 
                     "'throw'", "'goto'", "'int'", "'float'", "'double'", 
                     "'char'", "'string'", "'bool'", "'void'", "'object'", 
                     "'var'", "'null'", "'class'", "'struct'", "'interface'", 
                     "'enum'", "'namespace'", "'using'", "'public'", "'private'", 
                     "'protected'", "'internal'", "'static'", "'virtual'", 
                     "'override'", "'abstract'", "'sealed'", "'readonly'", 
                     "'const'", "'new'", "'this'", "'base'", "'in'", "'out'", 
                     "'ref'", "'params'", "'is'", "'as'", "'typeof'", "'true'", 
                     "'false'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", "'!'", 
                     "'&'", "'|'", "'^'", "'~'", "'<<'", "'>>'", "'++'", 
                     "'--'", "'??'", "'?'", "':'", "';'", "','", "'.'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "FOR", "DO", "SWITCH", 
                      "CASE", "DEFAULT", "BREAK", "CONTINUE", "RETURN", 
                      "TRY", "CATCH", "FINALLY", "THROW", "GOTO", "INT", 
                      "FLOAT", "DOUBLE", "CHAR", "STRING", "BOOL", "VOID", 
                      "OBJECT", "VAR", "NULL", "CLASS", "STRUCT", "INTERFACE", 
                      "ENUM", "NAMESPACE", "USING", "PUBLIC", "PRIVATE", 
                      "PROTECTED", "INTERNAL", "STATIC", "VIRTUAL", "OVERRIDE", 
                      "ABSTRACT", "SEALED", "READONLY", "CONST", "NEW", 
                      "THIS", "BASE", "IN", "OUT", "REF", "PARAMS", "IS", 
                      "AS", "TYPEOF", "TRUE", "FALSE", "IDENT", "INTEGER", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "CHAR_LITERAL", 
                      "PLUS", "MINUS", "STAR", "DIV", "MOD", "ASSIGN", "PLUS_ASSIGN", 
                      "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "EQUAL", "NOTEQUAL", "LT", "GT", "LE", "GE", "AND", 
                      "OR", "NOT", "BIT_AND", "BIT_OR", "BIT_XOR", "BIT_NOT", 
                      "LSHIFT", "RSHIFT", "INCREMENT", "DECREMENT", "NULL_COALESCING", 
                      "TERNARY_COND", "COLON", "SEMICOLON", "COMMA", "DOT", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_compilationUnit = 0
    RULE_usingDirective = 1
    RULE_namespaceDecl = 2
    RULE_classDecl = 3
    RULE_accessModifier = 4
    RULE_classMember = 5
    RULE_constructorDecl = 6
    RULE_methodDecl = 7
    RULE_parameterList = 8
    RULE_parameter = 9
    RULE_varDecl = 10
    RULE_type = 11
    RULE_statement = 12
    RULE_block = 13
    RULE_breakStatement = 14
    RULE_expressionStatement = 15
    RULE_ifStatement = 16
    RULE_forStatement = 17
    RULE_forInit = 18
    RULE_whileStatement = 19
    RULE_doWhileStatement = 20
    RULE_switchStatement = 21
    RULE_switchBlock = 22
    RULE_switchSection = 23
    RULE_switchLabel = 24
    RULE_tryCatchStatement = 25
    RULE_catchClause = 26
    RULE_finallyClause = 27
    RULE_returnStatement = 28
    RULE_expression = 29
    RULE_assignmentExpr = 30
    RULE_logicExpr = 31
    RULE_equalityExpr = 32
    RULE_relationalExpr = 33
    RULE_additiveExpr = 34
    RULE_multExpr = 35
    RULE_unaryExpr = 36
    RULE_postfixExpr = 37
    RULE_primaryExpr = 38
    RULE_literal = 39
    RULE_constantExpression = 40
    RULE_argumentList = 41

    ruleNames =  [ "compilationUnit", "usingDirective", "namespaceDecl", 
                   "classDecl", "accessModifier", "classMember", "constructorDecl", 
                   "methodDecl", "parameterList", "parameter", "varDecl", 
                   "type", "statement", "block", "breakStatement", "expressionStatement", 
                   "ifStatement", "forStatement", "forInit", "whileStatement", 
                   "doWhileStatement", "switchStatement", "switchBlock", 
                   "switchSection", "switchLabel", "tryCatchStatement", 
                   "catchClause", "finallyClause", "returnStatement", "expression", 
                   "assignmentExpr", "logicExpr", "equalityExpr", "relationalExpr", 
                   "additiveExpr", "multExpr", "unaryExpr", "postfixExpr", 
                   "primaryExpr", "literal", "constantExpression", "argumentList" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    FOR=4
    DO=5
    SWITCH=6
    CASE=7
    DEFAULT=8
    BREAK=9
    CONTINUE=10
    RETURN=11
    TRY=12
    CATCH=13
    FINALLY=14
    THROW=15
    GOTO=16
    INT=17
    FLOAT=18
    DOUBLE=19
    CHAR=20
    STRING=21
    BOOL=22
    VOID=23
    OBJECT=24
    VAR=25
    NULL=26
    CLASS=27
    STRUCT=28
    INTERFACE=29
    ENUM=30
    NAMESPACE=31
    USING=32
    PUBLIC=33
    PRIVATE=34
    PROTECTED=35
    INTERNAL=36
    STATIC=37
    VIRTUAL=38
    OVERRIDE=39
    ABSTRACT=40
    SEALED=41
    READONLY=42
    CONST=43
    NEW=44
    THIS=45
    BASE=46
    IN=47
    OUT=48
    REF=49
    PARAMS=50
    IS=51
    AS=52
    TYPEOF=53
    TRUE=54
    FALSE=55
    IDENT=56
    INTEGER=57
    FLOAT_LITERAL=58
    STRING_LITERAL=59
    CHAR_LITERAL=60
    PLUS=61
    MINUS=62
    STAR=63
    DIV=64
    MOD=65
    ASSIGN=66
    PLUS_ASSIGN=67
    MINUS_ASSIGN=68
    MUL_ASSIGN=69
    DIV_ASSIGN=70
    MOD_ASSIGN=71
    EQUAL=72
    NOTEQUAL=73
    LT=74
    GT=75
    LE=76
    GE=77
    AND=78
    OR=79
    NOT=80
    BIT_AND=81
    BIT_OR=82
    BIT_XOR=83
    BIT_NOT=84
    LSHIFT=85
    RSHIFT=86
    INCREMENT=87
    DECREMENT=88
    NULL_COALESCING=89
    TERNARY_COND=90
    COLON=91
    SEMICOLON=92
    COMMA=93
    DOT=94
    LPAREN=95
    RPAREN=96
    LBRACE=97
    RBRACE=98
    LBRACK=99
    RBRACK=100
    LINE_COMMENT=101
    BLOCK_COMMENT=102
    WS=103

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SimpleCSharpParser.EOF, 0)

        def usingDirective(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.UsingDirectiveContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.UsingDirectiveContext,i)


        def namespaceDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.NamespaceDeclContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.NamespaceDeclContext,i)


        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.ClassDeclContext,i)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)




    def compilationUnit(self):

        localctx = SimpleCSharpParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 135425687552) != 0):
                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32]:
                    self.state = 84
                    self.usingDirective()
                    pass
                elif token in [31]:
                    self.state = 85
                    self.namespaceDecl()
                    pass
                elif token in [27, 33, 34, 35, 36]:
                    self.state = 86
                    self.classDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(SimpleCSharpParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsingDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USING(self):
            return self.getToken(SimpleCSharpParser.USING, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCSharpParser.IDENT)
            else:
                return self.getToken(SimpleCSharpParser.IDENT, i)

        def SEMICOLON(self):
            return self.getToken(SimpleCSharpParser.SEMICOLON, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCSharpParser.DOT)
            else:
                return self.getToken(SimpleCSharpParser.DOT, i)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_usingDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingDirective" ):
                listener.enterUsingDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingDirective" ):
                listener.exitUsingDirective(self)




    def usingDirective(self):

        localctx = SimpleCSharpParser.UsingDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_usingDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(SimpleCSharpParser.USING)
            self.state = 95
            self.match(SimpleCSharpParser.IDENT)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==94:
                self.state = 96
                self.match(SimpleCSharpParser.DOT)
                self.state = 97
                self.match(SimpleCSharpParser.IDENT)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(SimpleCSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMESPACE(self):
            return self.getToken(SimpleCSharpParser.NAMESPACE, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCSharpParser.IDENT)
            else:
                return self.getToken(SimpleCSharpParser.IDENT, i)

        def LBRACE(self):
            return self.getToken(SimpleCSharpParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SimpleCSharpParser.RBRACE, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCSharpParser.DOT)
            else:
                return self.getToken(SimpleCSharpParser.DOT, i)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.ClassDeclContext,i)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_namespaceDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespaceDecl" ):
                listener.enterNamespaceDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespaceDecl" ):
                listener.exitNamespaceDecl(self)




    def namespaceDecl(self):

        localctx = SimpleCSharpParser.NamespaceDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_namespaceDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(SimpleCSharpParser.NAMESPACE)
            self.state = 106
            self.match(SimpleCSharpParser.IDENT)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==94:
                self.state = 107
                self.match(SimpleCSharpParser.DOT)
                self.state = 108
                self.match(SimpleCSharpParser.IDENT)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
            self.match(SimpleCSharpParser.LBRACE)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 128983236608) != 0):
                self.state = 115
                self.classDecl()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self.match(SimpleCSharpParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(SimpleCSharpParser.CLASS, 0)

        def IDENT(self):
            return self.getToken(SimpleCSharpParser.IDENT, 0)

        def LBRACE(self):
            return self.getToken(SimpleCSharpParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SimpleCSharpParser.RBRACE, 0)

        def classMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.ClassMemberContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.ClassMemberContext,i)


        def PUBLIC(self):
            return self.getToken(SimpleCSharpParser.PUBLIC, 0)

        def PRIVATE(self):
            return self.getToken(SimpleCSharpParser.PRIVATE, 0)

        def PROTECTED(self):
            return self.getToken(SimpleCSharpParser.PROTECTED, 0)

        def INTERNAL(self):
            return self.getToken(SimpleCSharpParser.INTERNAL, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)




    def classDecl(self):

        localctx = SimpleCSharpParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0):
                self.state = 123
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 126
            self.match(SimpleCSharpParser.CLASS)
            self.state = 127
            self.match(SimpleCSharpParser.IDENT)
            self.state = 128
            self.match(SimpleCSharpParser.LBRACE)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 72066519030169600) != 0):
                self.state = 129
                self.classMember()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(SimpleCSharpParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(SimpleCSharpParser.PUBLIC, 0)

        def PRIVATE(self):
            return self.getToken(SimpleCSharpParser.PRIVATE, 0)

        def PROTECTED(self):
            return self.getToken(SimpleCSharpParser.PROTECTED, 0)

        def INTERNAL(self):
            return self.getToken(SimpleCSharpParser.INTERNAL, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_accessModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessModifier" ):
                listener.enterAccessModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessModifier" ):
                listener.exitAccessModifier(self)




    def accessModifier(self):

        localctx = SimpleCSharpParser.AccessModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_accessModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDecl(self):
            return self.getTypedRuleContext(SimpleCSharpParser.MethodDeclContext,0)


        def accessModifier(self):
            return self.getTypedRuleContext(SimpleCSharpParser.AccessModifierContext,0)


        def constructorDecl(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ConstructorDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(SimpleCSharpParser.VarDeclContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_classMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassMember" ):
                listener.enterClassMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassMember" ):
                listener.exitClassMember(self)




    def classMember(self):

        localctx = SimpleCSharpParser.ClassMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classMember)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0):
                    self.state = 139
                    self.accessModifier()


                self.state = 142
                self.methodDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0):
                    self.state = 143
                    self.accessModifier()


                self.state = 146
                self.constructorDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0):
                    self.state = 147
                    self.accessModifier()


                self.state = 150
                self.varDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SimpleCSharpParser.IDENT, 0)

        def LPAREN(self):
            return self.getToken(SimpleCSharpParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SimpleCSharpParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SimpleCSharpParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ParameterListContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_constructorDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorDecl" ):
                listener.enterConstructorDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorDecl" ):
                listener.exitConstructorDecl(self)




    def constructorDecl(self):

        localctx = SimpleCSharpParser.ConstructorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_constructorDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(SimpleCSharpParser.IDENT)
            self.state = 154
            self.match(SimpleCSharpParser.LPAREN)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594088128512) != 0):
                self.state = 155
                self.parameterList()


            self.state = 158
            self.match(SimpleCSharpParser.RPAREN)
            self.state = 159
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SimpleCSharpParser.TypeContext,0)


        def IDENT(self):
            return self.getToken(SimpleCSharpParser.IDENT, 0)

        def LPAREN(self):
            return self.getToken(SimpleCSharpParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SimpleCSharpParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SimpleCSharpParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ParameterListContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_methodDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDecl" ):
                listener.enterMethodDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDecl" ):
                listener.exitMethodDecl(self)




    def methodDecl(self):

        localctx = SimpleCSharpParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.type_()
            self.state = 162
            self.match(SimpleCSharpParser.IDENT)
            self.state = 163
            self.match(SimpleCSharpParser.LPAREN)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594088128512) != 0):
                self.state = 164
                self.parameterList()


            self.state = 167
            self.match(SimpleCSharpParser.RPAREN)
            self.state = 168
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.ParameterContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCSharpParser.COMMA)
            else:
                return self.getToken(SimpleCSharpParser.COMMA, i)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = SimpleCSharpParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.parameter()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==93:
                self.state = 171
                self.match(SimpleCSharpParser.COMMA)
                self.state = 172
                self.parameter()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SimpleCSharpParser.TypeContext,0)


        def IDENT(self):
            return self.getToken(SimpleCSharpParser.IDENT, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = SimpleCSharpParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.type_()
            self.state = 179
            self.match(SimpleCSharpParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SimpleCSharpParser.TypeContext,0)


        def IDENT(self):
            return self.getToken(SimpleCSharpParser.IDENT, 0)

        def SEMICOLON(self):
            return self.getToken(SimpleCSharpParser.SEMICOLON, 0)

        def CONST(self):
            return self.getToken(SimpleCSharpParser.CONST, 0)

        def ASSIGN(self):
            return self.getToken(SimpleCSharpParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = SimpleCSharpParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 181
                self.match(SimpleCSharpParser.CONST)


            self.state = 184
            self.type_()
            self.state = 185
            self.match(SimpleCSharpParser.IDENT)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==66:
                self.state = 186
                self.match(SimpleCSharpParser.ASSIGN)
                self.state = 187
                self.expression()


            self.state = 190
            self.match(SimpleCSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SimpleCSharpParser.INT, 0)

        def FLOAT(self):
            return self.getToken(SimpleCSharpParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(SimpleCSharpParser.DOUBLE, 0)

        def BOOL(self):
            return self.getToken(SimpleCSharpParser.BOOL, 0)

        def CHAR(self):
            return self.getToken(SimpleCSharpParser.CHAR, 0)

        def STRING(self):
            return self.getToken(SimpleCSharpParser.STRING, 0)

        def VOID(self):
            return self.getToken(SimpleCSharpParser.VOID, 0)

        def VAR(self):
            return self.getToken(SimpleCSharpParser.VAR, 0)

        def IDENT(self):
            return self.getToken(SimpleCSharpParser.IDENT, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = SimpleCSharpParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 72057594088128512) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(SimpleCSharpParser.BlockContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.DoWhileStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.SwitchStatementContext,0)


        def tryCatchStatement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.TryCatchStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.BreakStatementContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(SimpleCSharpParser.VarDeclContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionStatementContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = SimpleCSharpParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 196
                self.forStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 197
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 198
                self.doWhileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 199
                self.switchStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 200
                self.tryCatchStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 201
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 202
                self.breakStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 203
                self.varDecl()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 204
                self.expressionStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SimpleCSharpParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SimpleCSharpParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = SimpleCSharpParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(SimpleCSharpParser.LBRACE)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 9205366434555632250) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 164225) != 0):
                self.state = 208
                self.statement()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 214
            self.match(SimpleCSharpParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(SimpleCSharpParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(SimpleCSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = SimpleCSharpParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(SimpleCSharpParser.BREAK)
            self.state = 217
            self.match(SimpleCSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(SimpleCSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = SimpleCSharpParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.expression()
            self.state = 220
            self.match(SimpleCSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SimpleCSharpParser.IF, 0)

        def LPAREN(self):
            return self.getToken(SimpleCSharpParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SimpleCSharpParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(SimpleCSharpParser.ELSE, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = SimpleCSharpParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(SimpleCSharpParser.IF)
            self.state = 223
            self.match(SimpleCSharpParser.LPAREN)
            self.state = 224
            self.expression()
            self.state = 225
            self.match(SimpleCSharpParser.RPAREN)
            self.state = 226
            self.statement()
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 227
                self.match(SimpleCSharpParser.ELSE)
                self.state = 228
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(SimpleCSharpParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(SimpleCSharpParser.LPAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCSharpParser.SEMICOLON)
            else:
                return self.getToken(SimpleCSharpParser.SEMICOLON, i)

        def RPAREN(self):
            return self.getToken(SimpleCSharpParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.StatementContext,0)


        def forInit(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ForInitContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = SimpleCSharpParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(SimpleCSharpParser.FOR)
            self.state = 232
            self.match(SimpleCSharpParser.LPAREN)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9205357638462603264) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 33153) != 0):
                self.state = 233
                self.forInit()


            self.state = 236
            self.match(SimpleCSharpParser.SEMICOLON)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9205357638412402688) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 33153) != 0):
                self.state = 237
                self.expression()


            self.state = 240
            self.match(SimpleCSharpParser.SEMICOLON)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9205357638412402688) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 33153) != 0):
                self.state = 241
                self.expression()


            self.state = 244
            self.match(SimpleCSharpParser.RPAREN)
            self.state = 245
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_forInit

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarInitContext(ForInitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCSharpParser.ForInitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(SimpleCSharpParser.TypeContext,0)

        def IDENT(self):
            return self.getToken(SimpleCSharpParser.IDENT, 0)
        def ASSIGN(self):
            return self.getToken(SimpleCSharpParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarInit" ):
                listener.enterVarInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarInit" ):
                listener.exitVarInit(self)


    class ExprInitContext(ForInitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCSharpParser.ForInitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprInit" ):
                listener.enterExprInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprInit" ):
                listener.exitExprInit(self)



    def forInit(self):

        localctx = SimpleCSharpParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_forInit)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = SimpleCSharpParser.VarInitContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.type_()
                self.state = 248
                self.match(SimpleCSharpParser.IDENT)
                self.state = 249
                self.match(SimpleCSharpParser.ASSIGN)
                self.state = 250
                self.expression()
                pass

            elif la_ == 2:
                localctx = SimpleCSharpParser.ExprInitContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SimpleCSharpParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(SimpleCSharpParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SimpleCSharpParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.StatementContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = SimpleCSharpParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(SimpleCSharpParser.WHILE)
            self.state = 256
            self.match(SimpleCSharpParser.LPAREN)
            self.state = 257
            self.expression()
            self.state = 258
            self.match(SimpleCSharpParser.RPAREN)
            self.state = 259
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(SimpleCSharpParser.DO, 0)

        def statement(self):
            return self.getTypedRuleContext(SimpleCSharpParser.StatementContext,0)


        def WHILE(self):
            return self.getToken(SimpleCSharpParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(SimpleCSharpParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SimpleCSharpParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(SimpleCSharpParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)




    def doWhileStatement(self):

        localctx = SimpleCSharpParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(SimpleCSharpParser.DO)
            self.state = 262
            self.statement()
            self.state = 263
            self.match(SimpleCSharpParser.WHILE)
            self.state = 264
            self.match(SimpleCSharpParser.LPAREN)
            self.state = 265
            self.expression()
            self.state = 266
            self.match(SimpleCSharpParser.RPAREN)
            self.state = 267
            self.match(SimpleCSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(SimpleCSharpParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(SimpleCSharpParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(SimpleCSharpParser.RPAREN, 0)

        def switchBlock(self):
            return self.getTypedRuleContext(SimpleCSharpParser.SwitchBlockContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = SimpleCSharpParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(SimpleCSharpParser.SWITCH)
            self.state = 270
            self.match(SimpleCSharpParser.LPAREN)
            self.state = 271
            self.expression()
            self.state = 272
            self.match(SimpleCSharpParser.RPAREN)
            self.state = 273
            self.switchBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(SimpleCSharpParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(SimpleCSharpParser.RBRACE, 0)

        def switchSection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.SwitchSectionContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.SwitchSectionContext,i)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_switchBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBlock" ):
                listener.enterSwitchBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBlock" ):
                listener.exitSwitchBlock(self)




    def switchBlock(self):

        localctx = SimpleCSharpParser.SwitchBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_switchBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(SimpleCSharpParser.LBRACE)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 276
                self.switchSection()
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 282
            self.match(SimpleCSharpParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switchLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.SwitchLabelContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.SwitchLabelContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_switchSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchSection" ):
                listener.enterSwitchSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchSection" ):
                listener.exitSwitchSection(self)




    def switchSection(self):

        localctx = SimpleCSharpParser.SwitchSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_switchSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 284
                self.switchLabel()
                self.state = 287 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7 or _la==8):
                    break

            self.state = 290 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 289
                self.statement()
                self.state = 292 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 9205366434555632250) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 164225) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(SimpleCSharpParser.CASE, 0)

        def constantExpression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ConstantExpressionContext,0)


        def COLON(self):
            return self.getToken(SimpleCSharpParser.COLON, 0)

        def DEFAULT(self):
            return self.getToken(SimpleCSharpParser.DEFAULT, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_switchLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchLabel" ):
                listener.enterSwitchLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchLabel" ):
                listener.exitSwitchLabel(self)




    def switchLabel(self):

        localctx = SimpleCSharpParser.SwitchLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_switchLabel)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(SimpleCSharpParser.CASE)
                self.state = 295
                self.constantExpression()
                self.state = 296
                self.match(SimpleCSharpParser.COLON)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.match(SimpleCSharpParser.DEFAULT)
                self.state = 299
                self.match(SimpleCSharpParser.COLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryCatchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(SimpleCSharpParser.TRY, 0)

        def block(self):
            return self.getTypedRuleContext(SimpleCSharpParser.BlockContext,0)


        def catchClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.CatchClauseContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.CatchClauseContext,i)


        def finallyClause(self):
            return self.getTypedRuleContext(SimpleCSharpParser.FinallyClauseContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_tryCatchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryCatchStatement" ):
                listener.enterTryCatchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryCatchStatement" ):
                listener.exitTryCatchStatement(self)




    def tryCatchStatement(self):

        localctx = SimpleCSharpParser.TryCatchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_tryCatchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(SimpleCSharpParser.TRY)
            self.state = 303
            self.block()
            self.state = 305 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 304
                self.catchClause()
                self.state = 307 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 309
                self.finallyClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(SimpleCSharpParser.CATCH, 0)

        def LPAREN(self):
            return self.getToken(SimpleCSharpParser.LPAREN, 0)

        def type_(self):
            return self.getTypedRuleContext(SimpleCSharpParser.TypeContext,0)


        def IDENT(self):
            return self.getToken(SimpleCSharpParser.IDENT, 0)

        def RPAREN(self):
            return self.getToken(SimpleCSharpParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(SimpleCSharpParser.BlockContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_catchClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchClause" ):
                listener.enterCatchClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchClause" ):
                listener.exitCatchClause(self)




    def catchClause(self):

        localctx = SimpleCSharpParser.CatchClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_catchClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(SimpleCSharpParser.CATCH)
            self.state = 313
            self.match(SimpleCSharpParser.LPAREN)
            self.state = 314
            self.type_()
            self.state = 315
            self.match(SimpleCSharpParser.IDENT)
            self.state = 316
            self.match(SimpleCSharpParser.RPAREN)
            self.state = 317
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinallyClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINALLY(self):
            return self.getToken(SimpleCSharpParser.FINALLY, 0)

        def block(self):
            return self.getTypedRuleContext(SimpleCSharpParser.BlockContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_finallyClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinallyClause" ):
                listener.enterFinallyClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinallyClause" ):
                listener.exitFinallyClause(self)




    def finallyClause(self):

        localctx = SimpleCSharpParser.FinallyClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_finallyClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(SimpleCSharpParser.FINALLY)
            self.state = 320
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SimpleCSharpParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(SimpleCSharpParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = SimpleCSharpParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(SimpleCSharpParser.RETURN)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9205357638412402688) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 33153) != 0):
                self.state = 323
                self.expression()


            self.state = 326
            self.match(SimpleCSharpParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.AssignmentExprContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = SimpleCSharpParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.assignmentExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfixExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.PostfixExprContext,0)


        def ASSIGN(self):
            return self.getToken(SimpleCSharpParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def logicExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.LogicExprContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_assignmentExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpr" ):
                listener.enterAssignmentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpr" ):
                listener.exitAssignmentExpr(self)




    def assignmentExpr(self):

        localctx = SimpleCSharpParser.AssignmentExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignmentExpr)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.postfixExpr()
                self.state = 331
                self.match(SimpleCSharpParser.ASSIGN)
                self.state = 332
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.logicExpr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.EqualityExprContext,0)


        def logicExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.LogicExprContext,0)


        def OR(self):
            return self.getToken(SimpleCSharpParser.OR, 0)

        def AND(self):
            return self.getToken(SimpleCSharpParser.AND, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_logicExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpr" ):
                listener.enterLogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpr" ):
                listener.exitLogicExpr(self)



    def logicExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCSharpParser.LogicExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_logicExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.equalityExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 346
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = SimpleCSharpParser.LogicExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicExpr)
                        self.state = 340
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 341
                        self.match(SimpleCSharpParser.OR)
                        self.state = 342
                        self.equalityExpr(0)
                        pass

                    elif la_ == 2:
                        localctx = SimpleCSharpParser.LogicExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicExpr)
                        self.state = 343
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 344
                        self.match(SimpleCSharpParser.AND)
                        self.state = 345
                        self.equalityExpr(0)
                        pass

             
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EqualityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.RelationalExprContext,0)


        def equalityExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.EqualityExprContext,0)


        def EQUAL(self):
            return self.getToken(SimpleCSharpParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(SimpleCSharpParser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_equalityExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)



    def equalityExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCSharpParser.EqualityExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_equalityExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.relationalExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCSharpParser.EqualityExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpr)
                    self.state = 354
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 355
                    _la = self._input.LA(1)
                    if not(_la==72 or _la==73):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 356
                    self.relationalExpr(0) 
                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.AdditiveExprContext,0)


        def relationalExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.RelationalExprContext,0)


        def LT(self):
            return self.getToken(SimpleCSharpParser.LT, 0)

        def LE(self):
            return self.getToken(SimpleCSharpParser.LE, 0)

        def GT(self):
            return self.getToken(SimpleCSharpParser.GT, 0)

        def GE(self):
            return self.getToken(SimpleCSharpParser.GE, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_relationalExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)



    def relationalExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCSharpParser.RelationalExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_relationalExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.additiveExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 370
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCSharpParser.RelationalExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relationalExpr)
                    self.state = 365
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 366
                    _la = self._input.LA(1)
                    if not(((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & 15) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 367
                    self.additiveExpr(0) 
                self.state = 372
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.MultExprContext,0)


        def additiveExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.AdditiveExprContext,0)


        def PLUS(self):
            return self.getToken(SimpleCSharpParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SimpleCSharpParser.MINUS, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)



    def additiveExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCSharpParser.AdditiveExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_additiveExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.multExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCSharpParser.AdditiveExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpr)
                    self.state = 376
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 377
                    _la = self._input.LA(1)
                    if not(_la==61 or _la==62):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 378
                    self.multExpr(0) 
                self.state = 383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.UnaryExprContext,0)


        def multExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.MultExprContext,0)


        def STAR(self):
            return self.getToken(SimpleCSharpParser.STAR, 0)

        def DIV(self):
            return self.getToken(SimpleCSharpParser.DIV, 0)

        def MOD(self):
            return self.getToken(SimpleCSharpParser.MOD, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_multExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultExpr" ):
                listener.enterMultExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultExpr" ):
                listener.exitMultExpr(self)



    def multExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCSharpParser.MultExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_multExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCSharpParser.MultExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multExpr)
                    self.state = 387
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 388
                    _la = self._input.LA(1)
                    if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & 7) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 389
                    self.unaryExpr() 
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.UnaryExprContext,0)


        def PLUS(self):
            return self.getToken(SimpleCSharpParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SimpleCSharpParser.MINUS, 0)

        def NOT(self):
            return self.getToken(SimpleCSharpParser.NOT, 0)

        def INCREMENT(self):
            return self.getToken(SimpleCSharpParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(SimpleCSharpParser.DECREMENT, 0)

        def postfixExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.PostfixExprContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)




    def unaryExpr(self):

        localctx = SimpleCSharpParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [61, 62, 80, 87, 88]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                _la = self._input.LA(1)
                if not(((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & 201850883) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 396
                self.unaryExpr()
                pass
            elif token in [26, 54, 55, 56, 57, 58, 59, 60, 95]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.postfixExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(SimpleCSharpParser.PrimaryExprContext,0)


        def INCREMENT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCSharpParser.INCREMENT)
            else:
                return self.getToken(SimpleCSharpParser.INCREMENT, i)

        def DECREMENT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCSharpParser.DECREMENT)
            else:
                return self.getToken(SimpleCSharpParser.DECREMENT, i)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_postfixExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfixExpr" ):
                listener.enterPostfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfixExpr" ):
                listener.exitPostfixExpr(self)




    def postfixExpr(self):

        localctx = SimpleCSharpParser.PostfixExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_postfixExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.primaryExpr()
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 401
                    _la = self._input.LA(1)
                    if not(_la==87 or _la==88):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(SimpleCSharpParser.LiteralContext,0)


        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCSharpParser.IDENT)
            else:
                return self.getToken(SimpleCSharpParser.IDENT, i)

        def DOT(self):
            return self.getToken(SimpleCSharpParser.DOT, 0)

        def LPAREN(self):
            return self.getToken(SimpleCSharpParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SimpleCSharpParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ArgumentListContext,0)


        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_primaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpr" ):
                listener.enterPrimaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpr" ):
                listener.exitPrimaryExpr(self)




    def primaryExpr(self):

        localctx = SimpleCSharpParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_primaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.match(SimpleCSharpParser.IDENT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.match(SimpleCSharpParser.IDENT)
                self.state = 410
                self.match(SimpleCSharpParser.DOT)
                self.state = 411
                self.match(SimpleCSharpParser.IDENT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
                self.match(SimpleCSharpParser.IDENT)
                self.state = 413
                self.match(SimpleCSharpParser.LPAREN)
                self.state = 415
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9205357638412402688) != 0) or ((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & 33153) != 0):
                    self.state = 414
                    self.argumentList()


                self.state = 417
                self.match(SimpleCSharpParser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 418
                self.match(SimpleCSharpParser.LPAREN)
                self.state = 419
                self.expression()
                self.state = 420
                self.match(SimpleCSharpParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(SimpleCSharpParser.INTEGER, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(SimpleCSharpParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(SimpleCSharpParser.STRING_LITERAL, 0)

        def CHAR_LITERAL(self):
            return self.getToken(SimpleCSharpParser.CHAR_LITERAL, 0)

        def TRUE(self):
            return self.getToken(SimpleCSharpParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SimpleCSharpParser.FALSE, 0)

        def NULL(self):
            return self.getToken(SimpleCSharpParser.NULL, 0)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = SimpleCSharpParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2215771016733392896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_constantExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExpression" ):
                listener.enterConstantExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExpression" ):
                listener.exitConstantExpression(self)




    def constantExpression(self):

        localctx = SimpleCSharpParser.ConstantExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_constantExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCSharpParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleCSharpParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCSharpParser.COMMA)
            else:
                return self.getToken(SimpleCSharpParser.COMMA, i)

        def getRuleIndex(self):
            return SimpleCSharpParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = SimpleCSharpParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.expression()
            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==93:
                self.state = 429
                self.match(SimpleCSharpParser.COMMA)
                self.state = 430
                self.expression()
                self.state = 435
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[31] = self.logicExpr_sempred
        self._predicates[32] = self.equalityExpr_sempred
        self._predicates[33] = self.relationalExpr_sempred
        self._predicates[34] = self.additiveExpr_sempred
        self._predicates[35] = self.multExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicExpr_sempred(self, localctx:LogicExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def equalityExpr_sempred(self, localctx:EqualityExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def relationalExpr_sempred(self, localctx:RelationalExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def additiveExpr_sempred(self, localctx:AdditiveExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def multExpr_sempred(self, localctx:MultExprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




