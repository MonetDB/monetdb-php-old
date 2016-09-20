name = monetdb-php
version = `sed -n 's/^Version:[ \t]*\(.*\)/\1/p' php-monetdb.spec`

datadir = /usr/share

all:
	@echo "Nothing to do"

install:
	mkdir -p $(DESTDIR)$(datadir)/php/monetdb
	cp lib/php_mapi.inc lib/php_monetdb.php $(DESTDIR)$(datadir)/php/monetdb

dist:
	tar -c -j -f $(name)-$(version).tar.bz2 --transform "s,^,$(name)-$(version)/," `hg files -X .hgtags`
