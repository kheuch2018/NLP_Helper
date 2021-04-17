class Dataset:
  text_path=""
  tags_path=""
  sentences = {}
  keys=[]

  def __init__(self,text_path,tags_path):
    self.text_path = text_path
    self.tags_path = tags_path
    self.create_sentences()
    self.create_keys()

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

  


dataset = Dataset("./text.txt","tags.txt")
