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
  training_set = {
    "sentences": {},
    "keys": [],
    "vocab": [],
    "tagset": [], 
    "X": (),
    "Y": (),
    "N": 0
  }

  testing_set = {
    "sentences": {},
    "keys": [],
    "vocab": [],
    "tagset": [], 
    "X": (),
    "Y": (),
    "N": 0
  }
  
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
    self.create_sets()

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
      if line !="\n" and line !="" :
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
      elif line == "\n" and len(sentence_tags) and line!="" :
        self.Y = self.Y + (sentence_tags,)
        sentence_tags = ()
    
    
  def create_N(self):
    total = 0
    for tup in self.Y :
      total += len(tup)
    self.N = total
  
  def create_sets(self):

    #Sentences
    self.testing_set["sentences"] = dict(list(self.sentences.items())[int(len(self.sentences)*0.8):])

    self.training_set["sentences"] = {i:self.sentences[i] for i in self.sentences if i not in self.testing_set["sentences"].keys()}

    #Keys
    self.testing_set["keys"] = self.testing_set["sentences"].keys()
    self.training_set["keys"] = self.training_set["sentences"].keys()

    #Vocab
    my_vocab = {}
    for tup in self.testing_set["sentences"].values() :
      for word in tup :
        my_vocab[word] = True
    self.testing_set["vocab"] = my_vocab.keys() 

    my_vocab = {}
    for tup in self.training_set["sentences"].values() :
      for word in tup :
        my_vocab[word] = True
    self.training_set["vocab"] = my_vocab.keys()

    #X
    self.testing_set["X"] = self.X[int(len(self.X)*.8):]
    self.training_set["X"] = tuple(i for i in self.X if i not in self.testing_set["X"])
  
    #Y
    self.testing_set["Y"] = self.Y[int(len(self.Y)*.8):]
    self.training_set["Y"] = tuple(i for i in self.Y if i not in self.testing_set["Y"])

    #Tagsets and N
    train_tags = {}
    for tup in self.training_set["Y"] :
      self.training_set["N"] += len(tup) 
      for tag in tup :
        train_tags[tag] = True
    self.training_set["tagset"] = train_tags.keys()

    test_tags = {}
    for tup in self.testing_set["Y"] :
      self.testing_set["N"] += len(tup) 
      for tag in tup :
        test_tags[tag] = True
    self.testing_set["tagset"] = test_tags.keys()

    


