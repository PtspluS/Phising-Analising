import os, time

path_to_watch = "." #chemin d'acess vers le dossier contenant les mails
before = dict ([(f, None) for f in os.listdir (path_to_watch)])

while 1:
    
  time.sleep (10); #temps entre chaque check
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  
  
  if added: 
      print("Added: ", ", ".join (added))
      
      #
      #  Lancement de la fonction d'analyse sur le mail arrivé (added)
      #
      
  if removed: 
      print("Removed: ", ", ".join (removed));
      
      
  before = after