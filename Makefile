install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

TK_SUBDIRS := $(wildcard tk/*/.)

tk: $(TK_SUBDIRS)
	echo "Running make -C $^ $(filter-out $@, $(MAKECMDGOALS))"
	$(MAKE) -C $^ $(filter-out $@, $(MAKECMDGOALS))

all: install tk