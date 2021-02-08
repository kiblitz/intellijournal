import subprocess

def edit(editor, file_path):
  subprocess.run((editor, file_path))
