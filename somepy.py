# import pybliometrics
# pybliometrics.scopus.init()  # read API keys
# # Document-specific information
# from pybliometrics.scopus import AbstractRetrieval
# ab = AbstractRetrieval("10.1016/j.softx.2019.100263")
# ab.title
# ab.publicationName
# ab.authors
# # Author-specific information
# from pybliometrics.scopus import AuthorRetrieval
# au2 = AuthorRetrieval(ab.authors[1].auid)
# au2.h_index
# au1 = AuthorRetrieval(ab.authors[0].auid)
# au1.affiliation_current
# # Affiliation information
# from pybliometrics.scopus import AffiliationRetrieval
# aff1 = AffiliationRetrieval(au1.affiliation_current[0].id)
# aff1.author_count