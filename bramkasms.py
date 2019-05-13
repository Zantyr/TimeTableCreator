slowa = {
"orange": "or ange",
"plus": "plu s",
"play": "pla y",
"bok": "b ok",
"game": "ga me",
"%": "procent",
"promocja": "pro mocja",
"promocji": "pro mocji",
"uwaga": "uwag a",
"porno": "por no",
"losowanie": "losowa nie",
"wyslij sms": "wys lij sms",
"namierz mnie": "na mierz mnie",
"gratulacje": "grat ulacje",
"skorzystac": "skorzy stac",
"doladuj": "do laduj",
"wygrales": "wygral es",
"zapraszamy": "za praszamy",
"kredyt": "kred yt",
"tansze": "tan sze",
"vat": "va t",
"darmowe minuty": "darmo we minuty",
"wez udzial": "wez udz ial",
"pobierz": "pobi erz",
"sciagnij": "scia gnij",
"poszl": "po szl",
}

import sys
s = ' '.join(sys.argv[1:])
for k,v in slowa.items():
    s=s.replace(k,v)
print(s)