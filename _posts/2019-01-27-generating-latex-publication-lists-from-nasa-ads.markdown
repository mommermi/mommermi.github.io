---
author: mommermi
comments: true
date: 2019-01-27 21:18:46+00:00
layout: post
link: https://michaelmommert.wordpress.com/2019/01/27/generating-latex-publication-lists-from-nasa-ads/
slug: generating-latex-publication-lists-from-nasa-ads
title: Generating LaTeX Publication lists from NASA ADS
wordpress_id: 528
categories:
- General
- python
- software
---

Compiling lists of publications for proposals, applications, or simply your cv can be a cumbersome process. If only there was some code that could produce a nicely formatted pdf from the information listed on the [NASA ADS system](https://ui.adsabs.harvard.edu/#).... [Like this one. ](https://michaelmommert.files.wordpress.com/2019/01/refereed.pdf)

Et voilà:

[code language="python" highlight=4,5,6,7]
from pylatexenc.latexencode import utf8tolatex
import ads

ads.config.token = ''  # your ADS token
author_name = ''  # your name
years = () # years to be queried: (start year, end year)
refereed = True # if True, only refereed publications will be queried;
                # if False, only non-refereed publications will be queried

latex_header = (
    '\\documentclass[11pt]{article}\n'
    '\\usepackage[inner=1in,outer=1in,top=1in,bottom=1in]{geometry}\n'
    '\\usepackage{hyperref}\n\n'
    '\\begin{document}\n\n'
    '\\section*{Publications}\n\n'
    '\\begin{itemize}\itemsep 0pt\n')

latex_footer = (
    '\\end{itemize}\n'
    '\\end{document}\n')

def query_papers(author, refereed=None, years=None, rows=1000):
    """query papers from NASA ADS

    :param author: str, author name
    :param refereed: boolean or `None`, if `True`, only extract refereed
                     publications; if `False`, only extract not refereed
                     publications; if `None`, extract all; default: `None`
    :param years: tuple, list, or `None`, range of years to query or `None`,
                  default: `None`
    :param rows: int, maximum number of publications to extract

    :return: list of ads publication objects
    """
    # set query payload
    if refereed is None:
        q = ''
    elif refereed:
        q = 'property:refereed'
    elif not refereed:
        q = 'property:notrefereed'
    fq = 'database:astronomy'
    if years is not None:
        fq += " year:{0}-{1}".format(years[0], years[1])

    # perform query
    papers = ads.SearchQuery(author=author,
                             fq=fq,
                             q=q,
                             sort='pubdate',
                             rows=rows,
                             fl=['title', 'author', 'year', 'volume',
                                 'page', 'pub', 'identifier', 'citation'])

    return list(papers)

def create_latex(paper, name=None):
    """turn ads publication objects into strings using latex encoding

    :param paper: ads publication object
    :param name: string or `None`, name that will be highlighted in latex,
                 default: `None`

    :return: str, latex encoded string for paper
    """
    out = ''

    # put paper title in italic font
    title = '{\\it ' + utf8tolatex(paper.title[0]) + '}'

    # build author list
    if name is None:
        # treat all author names equally and list all of them
        authors = [utf8tolatex(paper.author[i])
                   for i in range(len(paper.author))]
        etal = False
    else:
        # highlight `name` in output string, if provided
        authors = []
        name_found = False
        dotdotdot = False
        etal = False
        for i in range(len(paper.author)):
            # `name` is the i-th author on this paper
            author = utf8tolatex(paper.author[i])
            if name in author:
                name_found = True
                authors.append('{\\bf ' + author + '}')
            elif i = 3 and not name_found and not dotdotdot:
                # at least 3 authors and `name` is not among the first 3;
                # insert '...'
                authors.append('...\ ')
                dotdotdot = True
            elif i >= 3 and not name_found and dotdotdot:
                # at least 3 authors, but this one is not `name`
                pass
            elif i >= 3 and name_found:
                # at least 3 authors and this one is `name`
                etal = True
                break

    # join author list and add 'et al.' if required
    if etal:
        authors = ', '.join(authors) + ' et al.'
    else:
        authors = ', '.join(authors)

    year = paper.year

    # create string with journal volume and page number
    pub = str(paper.pub)
    if paper.volume is not None:
        pub += ', ' + str(paper.volume)
    if paper.page is not None:
        pub += ', ' + str(paper.page[0])

    arxiv_link = ''
    for ident in paper.identifier:
        if 'arXiv:' in ident:
            arxiv_id = ident[6:]
            arxiv_link = ('\href{https://arxiv.org/abs/' +
                          arxiv_id + '}{arxiv}')
        elif len(ident) == 10 and ident[4] == '.':
            arxiv_link = ('\href{https://arxiv.org/abs/' +
                          ident + '}{arxiv}')

    # assemble output string as latex bullet list item
    out = ('\\item ' + authors + ' (' + year + '), ' + title +
           ', ' + pub)
    if arxiv_link != '':
        out += ', ' + arxiv_link

    # add number of citations, if available
    if paper.citation is not None and len(paper.citation) > 1:
        out += ', ' + str(len(paper.citation)) + ' citations'
    elif paper.citation is not None and len(paper.citation) == 1:
        out += ', ' + str(len(paper.citation)) + ' citation'

    return out

def fixme(out):
    """fix/reject citation substrings

    :param out: string containing publication information

    :return out: string
    """

    # words leading to a rejection
    reject = ['Erratum']
    for s in reject:
        if s in out:
            return ''

    # substrings to be replaced
    fix = {'': '',
           '': '',
           '': '',
           '': ''}
    for key, val in fix.items():
        if key in out:
            out = out.replace(key, val)

    out = out.replace('#', '\#')

    return out

# pull references from ads
papers = query_papers(author_name, refereed=refereed, years=years)

# write results to file
with open('publication_list.tex', 'w') as outf:
    outf.write(latex_header + '\n\n')
    for paper in list(papers):
        ref = fixme(create_latex(paper, author_name))
        if len(ref) > 0:
            print(paper.author[0], paper.year)
            outf.write(ref + '\n\n')
    outf.write(latex_footer + '\n')
[/code]

This script will produce the LaTeX source file for the pdf linked above. To run the code, you will need the following:



	
  * an [account](https://ui.adsabs.harvard.edu/#user/account/register) with the new ADS system and the private token you have been assigned with in

	
  * python 3 installed along with the modules [ads](https://github.com/andycasey/ads) and [pylatexenc](https://github.com/phfaist/pylatexenc)

	
  * pdflatex or latex installed to compile the resulting LaTeX file as a pdf or ps file, respectively


To create a publication list for yourself (or somebody else) follow these steps:

	
  1. download the code snippet and save it into a file, e.g., _create_publist.py_

	
  2. modify the highlighted lines in the code, i.e., the following items:

	
    * add your ADS token

	
    * add your name (this is the name that will be queried in ADS)

	
    * add the years to be queried, e.g., (2015, 2019) will query all publications published in the years 2015 till 2019

	
    * select whether you want a list of refereed publications or a list of non-refereed publications




	
  3. run the code in a terminal as: _python create_publist.py_

	
  4. compile the LaTeX source file: _pdflatex publication_list.tex_

	
  5. enjoy your publication list!


A few features of this script:

	
  * the number of authors listed is limited to 3; if there are more than 3 authors, the list if culled at 3 authors and "et al." is added automatically

	
  * your name is automatically highlighted in bold and it will never be culled from the author list provided

	
  * article titles are provided, as well as journal names, volume and page numbers

	
  * a hyperlink to the article on [arxiv](https://arxiv.org/) is automatically added (this was chosen over the official journal website since arxiv is open access)

	
  * if an article has been cited by others, the number of citations is provided

	
  * special characters are converted to LaTeX using pylatexenc

	
  * the _fixme_ function allows to reject publications based on buzzwords (e.g., '_erratum_', see line 156) and it will replace certain substrings if the formatting in ADS is messed up (in that case, look up the substring causing trouble in the LaTeX source file and add it to the dictionary ending in line 165)


Have fun with this!


