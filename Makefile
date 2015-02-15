
all: deps
	@make run

run:
	./run.py

deps: sass-spec sassc node-sass

sassc: libsass
	- wget -nc https://github.com/sass/sassc/archive/master.zip -O zips/sassc.zip
	cd repos && unzip -u ../zips/sassc.zip
	SASS_LIBSASS_PATH=`pwd`/repos/libsass-master make -C repos/sassc-master

libsass:
	- wget -nc https://github.com/sass/libsass/archive/master.zip -O zips/libsass.zip
	cd repos && unzip -u ../zips/libsass.zip

node-sass:
	npm install

sass-spec:
	- wget -nc https://github.com/sass/sass-spec/archive/master.zip -O zips/spec.zip
	cd repos && unzip -u ../zips/spec.zip

clean:
	rm -rf repos/*
	rm -rf zips/*
