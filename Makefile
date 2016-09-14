datadir = /usr/share

all:
	@echo "Nothing to do"

install:
	mkdir -p $(DESTDIR)$(datadir)/php/monetdb
	cp lib/php_mapi.inc lib/php_monetdb.php $(DESTDIR)$(datadir)/php/monetdb
