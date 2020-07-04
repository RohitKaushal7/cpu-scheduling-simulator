# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

GH_PAGES_SOURCES = source Makefile
GH_PAGES_BASE_BRANCH = master 

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

.PHONY: gh-pages
.ONESHELL:
gh-pages:
	rm -rf /tmp/gh-pages
	cp -r $(BUILDDIR)/html /tmp/gh-pages
	git checkout gh-pages
	cd .. && rm -rf src main.py setup.py docs && cp -r /tmp/gh-pages/* ./ && rm -rf /tmp/gh-pages && touch .nojekyll && git add . && git commit -m "Updated gh-pages" && git push origin gh-pages && git checkout master

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)