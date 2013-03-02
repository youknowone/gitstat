
all: index

log:
	cd $(GITSTAT_REPO) && git log > $(PWD)/log.txt

index: log
	python gen.py > index.html
