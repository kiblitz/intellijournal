import os

def get_models_folder():
  return __get_storage()['models']

def get_data_folder():
  return __get_storage()['data']

def get_journal_folder():
  return __get_storage()['journal']

def __get_storage():
  home = os.path.expanduser('~')
  storage = __with_storage(home)
  models = __with_models(home)
  data = __with_data(home)
  journal = __with_journal(home)
  if not os.path.isdir(storage):
    os.mkdir(storage)
  if not os.path.isdir(models):
    os.mkdir(models)
  if not os.path.isdir(data):
    os.mkdir(data)
  if not os.path.isdir(journal):
    os.mkdir(journal)
  return {'storage' : storage, 'models' : models, 'data' : data, 'journal' : journal}

def __with_storage(path):
  return path + '/.intellijournal/'

def __with_models(path):
  return __with_storage(path) + 'models/'

def __with_data(path):
  return __with_storage(path) + 'data/'

def __with_journal(path):
  return __with_storage(path) + 'journal/'
