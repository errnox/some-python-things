# -*- coding: utf-8 -*-

import sys
import twitter
import argparse
import random
import codecs


# Note
# ----
#
# We are dealing with Python and Twitter here. So special care has to be
# taken when handling strings/chars. UTF-8 is the absolute minimum.
# Assume the worst.


description = 'Twitter viewer'
url_help = 'Indicates that URL column should not be displayed'

arg_parser = argparse.ArgumentParser(description=description)
arg_parser.add_argument('--no-urls',
                        action='store_true',
                        default=False,
                        help=url_help)
args = arg_parser.parse_args()

class Fetcher(object):
    def __init__(self):
        self.api = twitter.Api()
        # self.api = twitter.Api()
        self.users = []
        self.messages = {}
        self.stdout_encoding = sys.stdout.encoding or sys.getfilesystemencoding()

    def add_user(self, user, *users):
        self.users.append(user)
        for user in users:
            self.users.append(user)

    def fetch(self):
        for user in self.users:
            statuses = self.api.GetUserTimeline(user)
            self.messages[user]=statuses

    def fetch_recent(self):
        for user in self.users:
            statuses = self.api.GetPublicTimeline()
            self.messages[user]=statuses

    def fetch_followers(self):
        for user in self.users:
            statuses = self.api.GetFollowers()
            self.messages[user]=statuses

    def short_report(self):
        c = '+'
        h = '-'
        v = '|'
        arrow = '     |'
        for user in self.messages:
            indent = ' ' * (len(user) + 2)
            hrul = c + h * (len(user) + 2) + c + '\n'
            print '\n', hrul, v, user, v, '\n', hrul, indent, v
            for message in self.messages[user]:
                if 'http' in message.GetText():
                    arrow = ' URL |'
                else:
                    arrow = '     |'
                if message != self.messages[user][-1]:
                    # print indent, v + arrow, message.GetText().decode('utf-8').encode(self.stdout_encoding, 'ignore')
                    print indent, v + arrow, message.GetText().encode(self.stdout_encoding, 'ignore')
                else:
                    # print indent, '`' + arrow, message.GetText().decode('utf-8').encode(self.stdout_encoding, 'ignore')
                    print indent, '`' + arrow, message.GetText().encode(self.stdout_encoding, 'ignore')

    def report(self, urls=True):
        display_urls = urls
        width = 0
        pevious_w = 0
        current_w = 0
        mesgs = []
        urls = []
        end_cap = '--+'
        for user in self.messages:
            # Get longest width
            for message in self.messages[user]:
                mesg = message.GetText().split('... ')
                for m in mesg:
                    urls.append(mesg[1])
                mesgs.append(mesg)
                previous_w = current_w
                current_w = len(max(mesg, key=len))
                if current_w > width:
                    width = current_w

            url_width = len(min(urls, key=len)) + 2

                # print '> ', message.GetText().split('... ')
            # print self._delimiter(width=width), user, '\n', '=' * len(user)  # , '\n' * 2

            if display_urls == True:
                print '+' + self._delimiter(
                    width=width).rstrip() + end_cap + '-' * url_width + end_cap

                print '| %s | %s |' % (user.ljust(width), ''.ljust(url_width, ' '))
                print '| %s | %s |' % (('=' * len(user)).ljust(width), ''.ljust(url_width, ' '))
                print '| %s | %s |' % (' '.ljust(width), ''.ljust(url_width, ' '))
                for mesg in mesgs:
                    print '| %s | %s |' % (mesg[0].ljust(width, ' '), mesg[1].ljust(url_width, ' '))
                # self._process_dict(message.AsDict)
                print '+' + self._delimiter(
                    width=width).rstrip() + end_cap + '-' * url_width + end_cap
            # elif True:
            #     print '+' + self._delimiter(width=width).rstrip() + end_cap

            #     print '| %s |' % (user.ljust(width))
            #     print '| %s |' % (('=' * len(user)).ljust(width))
            #     print '| %s |' % (' '.ljust(width))
            #     for mesg in mesgs:
            #         print '| %s |' % (mesg[0].ljust(width, ' '))
            #     # self._process_dict(message.AsDict)

            #     print '+' + self._delimiter(width=width).rstrip() + end_cap
            else:
                print '\033[' + str(random.randint(31, 36)) + 'm' '+' + self._delimiter(width=width).rstrip() + end_cap

                print '| %s |' % (user.ljust(width))
                print '| %s |' % (('=' * len(user)).ljust(width))
                print '| %s |' % (' '.ljust(width))
                for mesg in mesgs:
                    print '| %s |' % (mesg[0].ljust(width, ' '))
                # self._process_dict(message.AsDict)

                print '+' + self._delimiter(width=width).rstrip() + end_cap + '\033[m'

    # Helpers

    def _delimiter(self, char='-', width=80):
        return char * width + '\n'

    def _process(self, key, value):
        width = max([len(key), len(value)])
        print "%s %s" % (key.lflush(width, ' '), value.lflush(width, ' '))

    def _process_dict(self, dictionary):
        for keyf, value in dictionary:
            if hasattr(value, 'items'):
                self._process_dict(value, callback)
            else:
                self._process(key, value)


if __name__ == '__main__':
    fetcher = Fetcher()

    # Replace "<username>" with twitter handles
    fetcher.add_user('<username>', '<username>', '<username>')))

    # fetcher.add_user('<username>')
    fetcher.fetch()
    # fetcher.fetch_followers()
    # fetcher.fetch_recent()

    if args.no_urls == True:
        # fetcher.report(urls=False)
        fetcher.short_report()
    else:
        # fetcher.report(urls=True)
        fetcher.short_report()

