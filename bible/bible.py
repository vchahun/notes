#!/usr/bin/env python
import sys
import lxml.etree as et

def iterparse(stream, tag=None, events=('end',)):
    it = et.iterparse(stream, events)
    prev = next(it)
    for item in it:
        yield prev
        if prev[0] == 'end' and prev[1].tag == tag:
            prev[1].clear()
            prev[1].getparent().remove(prev[1])
        prev = item
    yield prev

def main(stream):
    """ Process http://homepages.inf.ed.ac.uk/s0787820/bible/ """
    for _, element in iterparse(stream, tag='seg'):
        if element.tag == 'seg':
            print element.text

if __name__ == '__main__':
    main(sys.stdin)
