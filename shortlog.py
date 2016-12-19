#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE


def git(*args):
    command = ["git"]
    command.extend(map(str, args))
    out = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()
    return [i for i in out][0]


def format_author_list(author_list):
    return str.join("\n", map(lambda line: str(line[0][0]).rjust(6) + "\t" + str(line[1][0]), author_list))


def get_shortlog(dry=True):
    all_authors = [line.split(":")[-1].rsplit(' ', 1)[0] for line in git("log").split("\n") if "Author: " in line]
    unsorted_authors = [[[all_authors.count(author)], [author.strip()]] for author in set(all_authors)]
    sorted_authors = sorted(unsorted_authors, key=lambda commit: commit[0], reverse=True)
    if dry:
        print(format_author_list(sorted_authors))
    else:
        return format_author_list(sorted_authors)

get_shortlog()
