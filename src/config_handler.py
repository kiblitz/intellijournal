import dir_handler

def get_config():
  return dir_handler.get_config()

def get_config_default():
  return get_config()['DEFAULT'] 

def get_default_attr(attr):
  config_default = get_config_default()
  if attr in config_default:
    return config_default[attr]
  return None

def get_editor():
  return get_default_attr('editor')
