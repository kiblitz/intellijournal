import pathlib

def get_folder():
  folder = pathlib.Path.home() / '.intellijournal'
  folder.mkdir(exist_ok=True) 
  return folder

def get_journal():
  journal = get_folder() / 'journal.db'
  journal.touch()
  return journal

def get_config():
  config = get_folder() / 'config'
  config.touch()
  return config
