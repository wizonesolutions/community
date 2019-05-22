from talon import Context, actions

ctx = Context()
dictate = actions.dictate

# wordwordword ...
def smash(m):
  smash = ""
  words = dictate.parse_words(m)
  for word in words:
    smash += word
  actions.insert(smash)

# word_word_word ...
def snake(m):
  snake = ""
  words = dictate.parse_words(m)
  for i in range(len(words)):
    if i == 0:
      snake += words[i]
    else:
      snake += "_" + words[i]
  actions.insert(snake)

# .word_word_word ...
def dotsnake(m):
  snake = ""
  words = dictate.parse_words(m)
  for i in range(len(words)):
    if i == 0:
      snake += "." + words[i]
    else:
      snake += "_" + words[i]
  actions.insert(snake)

# word-word-word ...
def spine(m):
  spine = ""
  words = dictate.parse_words(m)
  for i in range(len(words)):
    if i == 0:
      spine += words[i]
    else:
      spine += "-" + words[i]
  actions.insert(spine)

# word/word/word ...
def pathway(m):
  pathway = ""
  words = dictate.parse_words(m)
  for i in range(len(words)):
    if i == 0:
      pathway += words[i]
    else:
      pathway += "/" + words[i]
  actions.insert(pathway)

# word.word.word ...
def dotsway(m):
  pathway = ""
  words = dictate.parse_words(m)
  for i in range(len(words)):
    if i == 0:
      pathway += words[i]
    else:
      pathway += "." + words[i]
  actions.insert(pathway)

# wordWordWord ...
def camel(m):
  camel = ""
  words = dictate.parse_words(m)
  for i in range(len(words)):
    if i == 0:
      camel += words[i]
    else:
      camel += words[i].capitalize()
  actions.insert(camel)

# Word word word ...
def sentence(m):
  words = dictate.parse_words(m)
  words[0] = words[0].capitalize()
  sentence = dictate.join_words(words)
  actions.insert(sentence)

# Word Word and Word ...
def title(m):
  words = dictate.parse_words(m)
  words_to_keep_lowercase = "a,an,the,at,by,for,in,of,on,to,up,and,as,but,or,nor".split(",")
  for i in range(len(words)):
    if i == 0 or words[i] not in words_to_keep_lowercase:
      words[i] = words[i].capitalize()
  title = dictate.join_words(words)
  actions.insert(title)

# WORD WORD WORD
def yell(m):
  words = dictate.parse_words(m)
  for i in range(len(words)):
    words[i] = words[i].upper()
  yell = dictate.join_words(words)
  actions.insert(yell)

# WORD_WORD_WORD ...
def yellsnake(m):
  yellsnake = ""
  words = dictate.parse_words(m)
  for i in range(len(words)):
    if i == 0:
      yellsnake += words[i].upper()
    else:
      yellsnake += "_" + words[i].upper()
  actions.insert(yellsnake)

# WORDWORDWORD ...
def yellsmash(m):
  yellsmash = ""
  words = dictate.parse_words(m)
  for word in words:
      yellsmash+= word.upper()
  actions.insert(yellsmash)

# Voice Commands
ctx.commands = {
    # word word word ...
    'say <dgndictation> [over]': dictate.lower, 'phrase <dgndictation> [over]': dictate.lower,
    # Word word word ...
    'sentence <dgndictation>': sentence,
    # wordwordword ...
    'smash <dgndictation>': smash,
    # word_word_word ...
    'snake <dgndictation>': snake, 'dotsnik <dgndictation>': dotsnake,
    # word-word-word ...
    'spine <dgndictation>': spine, 'kebab <dgndictation>': spine,
    # wordWordWord ...
    'camel <dgndictation>': camel, 'cram <dgndictation>': camel,
    # Word Word and Word ...
    'title <dgndictation>': title,
    # WORD WORD WORD ...
    'yell <dgndictation>': yell, 'allcaps <dgndictation>': yell, 'yeller <dgndictation>': yell,
    # WORD_WORD_WORD ...
    'yellsnake <dgndictation>': yellsnake, 'yellsnik <dgndictation>': yellsnake,
    # WORDWORDWORD ...
    'yellsmash <dgndictation>': yellsmash,
    # word/word/word ...
    'pathway <dgndictation>': pathway,
    # word.word.word ...
    'dotsway <dgndictation>': dotsway,
}