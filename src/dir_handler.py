import pathlib

def get_folder():
  return pathlib.Path.home() / '.intellijournal'

def mk_folder():
  get_folder().mkdir(exist_ok=True) 

def get_journal():
  return get_folder() / 'journal.db'

def touch_journal():
  get_journal().touch()

def get_config():
  return get_folder() / 'config'

def touch_config():
  get_config().touch()
