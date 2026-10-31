"""Verbal question types for the Verbal test (one test per type). classify(q) -> type id or None."""
import re
TYPES = [  # (id, name)
 ('series', 'Number and Letter Series'), ('coding', 'Coding and Decoding'), ('mirror', 'Mirror and Water Images'),
 ('direction', 'Direction Sense'), ('blood', 'Blood Relations'), ('age', 'Age Problems'), ('calendar', 'Calendar and Days'),
 ('clock', 'Clock Problems'), ('ranking', 'Ranking and Order'), ('alphabet', 'Alphabet and Word Arrangement'),
 ('analogy', 'Analogy'), ('odd', 'Odd One Out'), ('percent', 'Percentage and Fractions'), ('speed', 'Speed, Time and Work'),
 ('money', 'Profit, Loss and Dozen'), ('english', 'English Vocabulary and Grammar'), ('logic', 'Logical Reasoning'), ('maths', 'Basic Maths and Reasoning'), ('other', 'Mixed Verbal')]
NAMES = dict(TYPES)
R = [
 ('mirror', r'\bmirror\b|water image'),
 ('coding', r'\bcoded?\b|\bcodes?\b|\bcoding\b|is written as|are written as|written in (a|that) code'),
 ('direction', r'\b(north|south|east|west)\w*\b.*\b(walk|walks|walked|turn|turns|turned|moves?|moved|facing|faces|faced|goes|went|direction)\b|\b(walk|walks|walked|turn|turns|turned|facing|moves|moved)\b.*\b(north|south|east|west|left|right)\b'),
 ('age', r'\bhow old\b|\byears old\b|\b(his|her|my|their|the) (present )?age\b|\bages?\b.*\b(years|after|ago|older|younger)\b|\btimes (older|as old)\b'),
 ('blood', r"\b(my|your|his|her|their|the man's|ali's|a's|b's)\b.*\b(brother|sister|father|mother|son|daughter|uncle|aunt|nephew|niece|grandfather|grandmother|husband|wife|cousin)\b.*\b(is|was|of|to)\b|\brelation(ship)?\b.*\b(between|to)\b|\bhow is\b.*\brelated\b"),
 ('analogy', r'\bis to\b.*\b(as|then)\b|\bis related to\b.*\bas\b|::'),
 ('clock', r"\bclock\b|o'clock|\bhands of\b|minute hand|hour hand"),
 ('calendar', r'\bdays? (later|after|before)\b|\b\d+(st|nd|rd|th) (of )?(january|february|march|april|may|june|july|august|september|october|november|december)\b.*\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday|day)\b|\b(yesterday|tomorrow|day after tomorrow|day before yesterday)\b|\bday of (a|the) month\b|\b\d+(st|nd|rd|th) (day|of)\b.*\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b|\bleap year\b|how many (days|months)'),
 ('ranking', r'\b(taller|shorter|older|younger|heavier|lighter|richer|poorer|faster|slower|smarter)\s+than\b|\brank(ed)?\b.*\b(from the (top|bottom)|position)\b|\b(shortest|tallest|oldest|youngest|heaviest|lightest)\b'),
 ('series', r'\bseries\b|comes? next|next (number|term|letter|one)|missing (number|term|letter)|what (will )?comes?\b|\d+\s*,\s*\d+\s*,\s*\d+'),
 ('alphabet', r'\balphabetical(ly)?\b|\bdictionary\b|\barrang(e|ed|ing)\b.*\b(letters?|word)\b|\bletters? of the word\b|\b(jumbled|rearrang)\w*\b|\bletter (from|in) the (word|alphabet)\b|\b\d+(st|nd|rd|th) letter\b'),
 ('english', r'\bsynonyms?\b|\bantonyms?\b|\bopposite of\b|\bmeaning of\b|\bcorrect spelling\b|\bplural of\b|\bone word for\b|\bsame meaning\b|closest in meaning|fill in the blank|passive|\bactive voice\b|correct sentence|\btense\b|\bpreposition\b|\bnarration\b'),
 ('odd', r'\bodd (one|man|word|number)\b|does not belong|different from (the )?(rest|others)|\bodd out\b|which (one )?(of the following )?is different|\bis different\b|not like the others'),
 ('speed', r'\bkm\s*/\s*h|\bkm per hour|\bspeed\b|\bdistance\b|\bmen\b.*\bdays?\b|\bwork\b.*\bdays?\b|\bminutes?\b.*\bcover\b|\btrain\b|\bpipes?\b'),
 ('money', r'\bprofit\b|\bloss\b|\bdozen\b|\bcost price\b|\bselling price\b|\bdiscount\b'),
 ('logic', r'\bwhy\b|\bbecause\b|\bin order to\b|\bpurpose of\b|\bstatements?\b|\bconclusion\b|\bif all\b|\bsome\b.*\ball\b'),
 ('percent', r'%|\bpercent(age)?\b|\bone (third|fourth|tenth|fifth|half)\b|\bquarter of\b|\bhalf of\b|\b\d+/\d+ of\b'),
]
RX = [(t, re.compile(p, re.I)) for t, p in R]
STRICT = {
 'english': r'(?!)',
 'logic': r'(?!)',
 'coding': r'\bcoded\b|is written as|are written as|code language|in a (certain )?code\b',
 'blood': r"what am i\b|who am i\b|relation between (you|me|a|b)\b|is my what|\bis (he|she|a|b) to\b|\bis not (his|her|a's) son\b|\bhow is [a-z]+ related\b",
 'calendar': r'\b(yesterday|tomorrow)\b|\bday of (a|the) month\b|\b\d+(st|nd|rd|th)\b[^.?]*\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b|\bleap year\b|months? (of the year )?(have|has) (31|30)',
 'ranking': r'\b(taller|shorter|older|younger|heavier|lighter|richer|poorer|faster|slower)\s+than\b',
 'speed': r'\d[^?]*\b(km|hours?|minutes?|days?)\b[^?]*\b(how (much|far|long|many)|what is (its|the) speed|in how)\b|\b(how (much|far|long|many))\b[^?]*\d[^?]*\b(km|hours?|minutes?)\b|\bmen\b[^?]*\bdays?\b',
 'money': r'\d',
 'series': r'\d+\s*,\s*\d+\s*,|\b[A-Z]{1,3}\s*,\s*[A-Z]{1,3}\s*,',
 'percent': r'\d+\s*%\s*of\s*\d|\bpercent(age)? of \d|\b(one|two) (third|fourth|tenth|fifth|quarter)s? of\b|\bquarter of\b|\bhalf of\b',
}
SRX = {k: re.compile(v, re.I) for k, v in STRICT.items()}
def text(q):
    return str(q.get('question', ''))
def classify(q, strict):
    s = text(q)
    for t, rx in RX:
        if rx.search(s):
            if strict and t in SRX and not SRX[t].search(s): continue
            return t
    if strict: return None
    return 'maths' if re.search(r'\d', s) else 'other'
