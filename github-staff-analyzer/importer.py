import re

import sqlite3


class Importer(object):
  def __init__(self, data_file, db_file):
    self.data_file = data_file
    self.db_file = db_file
    self.null_token = 'NULL'
    self.insertion_template = "INSERT INTO Staff (Name, Nick, Site, Location) VALUES ("


  def create_db(self):
    con = sqlite3.connect(self.db_file)
    con.execute(
      """CREATE TABLE Staff (
                     id INTEGER PRIMARY KEY
                     , Name char(100) NOT NULL
                     , Nick char(100)
                     , Site char(100) NOT NULL
                     , Location char(100)
                   );""")

    # Insertion example
    #
    # con.execute(
    #   """INSERT INTO tasks (task, description, status)
    #            VALUES (
    #                'Read A-byte-of-python to get a good introduction into Python'
    #                , 'This is a description'
    #                , 0
    #         )""")

    con.commit()


  def run(self):
    c = -1
    s = '' + self.insertion_template
    with open(self.data_file, 'r') as in_file:
      for line in in_file:
        # Site
        if c == 1:
          # print('SITE: %s' % re.split('Site: ', line)[1].strip())
          s += ', ' + '"' + re.split('Site: ', line)[1].strip() + '"'
        # Location
        elif c == 2:
          # print('SITE: %s' % re.split('Location: ', line)[1].strip())
          s += ', ' + '"' + re.split('Location: ', line)[1].strip() + '"'
          s += ');'

          print(s)

          # Insert into DB
          con = sqlite3.connect(self.db_file)
          con.execute(s)
          con.commit()

          s = '' + self.insertion_template
        # Blank line
        elif c == 3:
          # print(line)
          pass
        # Name + Nick
        else:
          c = 0
          # Name
          # print('NAME: %s' % re.split(' \(', line)[0].strip())
          s += '"' + re.split(' \(', line)[0].strip() + '"'
          # Nick
          # print('NICK: %s' % re.split(' \(', line)[1].strip().strip('\)'))
          s += ', ' + '"' +  re.split(' \(', line)[1].strip().strip('\)') + '"'
        c += 1


if __name__ == '__main__':
  importer = Importer('res/humans.txt.cleanedup', 'res/staff.db')
  importer.create_db()
  importer.run()
