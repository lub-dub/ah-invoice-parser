all: $(shell find ./invoices/*.pdf -type f | sed 's/.pdf/.txt/g')
	ls ./invoices/*.txt | xargs -I{} python ./parser.py {} | sort

%.txt : %.pdf
	pdftotext -layout $<

