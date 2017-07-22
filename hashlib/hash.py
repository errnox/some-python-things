import hashlib


class App(object):
  def __init__(self, payload='abc', repetitions=10):
    self.payload = payload
    self.repetitions = repetitions
    self.hashes = []

  def run(self):
    hash = self.generate_md5(self.payload)
    for i in range(self.repetitions):
      hash = self.generate_md5(hash)
      self.hashes.append(hash)
    self.print_hashes()

  def generate_md5(self, payload):
    return hashlib.md5(payload).hexdigest()

  def sort_string(self, string):
    return str.join('', sorted(string))

  def print_hashes(self):
    for hash in self.hashes:
        print(self.sort_string(hash))


if __name__ == '__main__':
  app = App(payload='123', repetitions=30)
  app.run()
