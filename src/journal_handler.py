import dir_handler

import sqlite3
import time

def get_conn():
  return sqlite3.connect(dir_handler.get_journal())

def exec_command(comm, *args):
  conn = get_conn()
  cursor = conn.cursor()
  res = comm(cursor, *args)
  conn.commit()
  conn.close()
  return res

def create_entries_table(cursor):
  comm = '''CREATE TABLE IF NOT EXISTS entries (
              id integer PRIMARY KEY,
              creation_time integer NOT NULL,
              last_edit_time integer NOT NULL,
              entry text
            )'''
  cursor.execute(comm)

def insert_entry(cursor, entry):
  comm = '''INSERT INTO entries (
              creation_time,
              last_edit_time,
              entry
            )
            VALUES (?, ?, ?)'''
  now = int(time.time())
  cursor.execute(comm, (now, now, entry))

def update_entry(cursor, pk, entry):
  comm = '''UPDATE entries SET
              last_edit_time = ?,
              entry = ?
            WHERE id = ?'''
  now = int(time.time())
  cursor.execute(comm, (now, entry, pk))

def delete_entry(cursor, pk):
  comm = 'DELETE FROM entries WHERE id = ?'
  cursor.execute(comm, (pk,))

def get_all_entries(cursor):
  comm = 'SELECT * FROM entries'
  cursor.execute(comm)
  rows = cursor.fetchall()
  return rows

def get_entry(cursor, pk):
  comm = 'SELECT * FROM entries WHERE id = ?'
  cursor.execute(comm, (pk,))
  rows = cursor.fetchall()
  return rows
