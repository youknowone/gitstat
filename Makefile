
all: index

log:
	cd $(GITSTAT_REPO) && git log > ../log.txt

index: log
	python gen.py > index.html
