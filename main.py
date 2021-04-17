class Dataset:
  text_path=""
  tags_path=""
  sentences = {}
  keys = []
  vocab = []
  tagset = [] 
  X = ()
  Y = ()
  N = 0
  
  def __init__(self,text_path,tags_path):
    self.text_path = text_path
    self.tags_path = tags_path
    self.create_sentences()
    self.create_keys()
    self.create_vocab()
    self.create_tagset()
    self.create_X()
    self.create_Y()
    self.create_N()

  def create_sentences(self):
    sentence_key = ""
    sentence = ()
    f = open(self.text_path,"r")
    for line in f.readlines():
      if "wo_" in line :
        sentence = ()
        sentence_key = line.replace("\n","")
      elif line !="\n" :
        sentence = sentence + (line.replace("\n","").split("\t")[0],)
      elif line == "\n" and len(sentence) :
        self.sentences[sentence_key] = sentence
    else:
      self.sentences[sentence_key] = sentence
  
  def create_keys(self):
    self.keys = self.sentences.keys()

  def create_vocab(self):
    my_vocab = {}
    for tup in self.sentences.values() :
      for word in tup :
        my_vocab[word] = True
    self.vocab = my_vocab.keys() 
  
  def create_tagset(self):
    tags = []
    f = open(self.tags_path,"r")
    for line in f.readlines():
      tags.append(line.replace("\n",""))
    else:
      self.tagset = tags
  
  def create_X(self):
    self.X = tuple(self.sentences.values())
  
  def create_Y(self):
    my_Y = ()
    f = open(self.text_path,"r")
    sentence_tags = ()
    for line in f.readlines():
      if "wo_" in line :
        sentence_tags = ()
      elif line !="\n" :
        tag = line.replace("\n","").split("\t")[1]
        sentence_tags = sentence_tags + (tag,)
      elif line == "\n" and len(sentence_tags) :
        self.Y = self.Y + (sentence_tags,)
    
  def create_N(self):
    total = 0
    for tup in self.Y :
      total += len(tup)
    self.N = total


dataset = Dataset("./text.txt","tags.txt")

