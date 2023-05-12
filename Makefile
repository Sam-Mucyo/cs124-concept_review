# Remove all auxiliary files, in quiet mode
clean:
	@rm -f *.aux *.log *.out *.toc *.bbl *.blg *.dvi \
	*.ps *.fdb_latexmk *.fls *.synctex.gz *.bcf *.xml
	@rm -rf _minted-*
	@rm -f .DS_Store

