#This is a query for getting some role-playing games that composed by Masaharu and published by Square-Enix.
#For better results displaying, please use Apache Jena Fuseki by only copy and paste the query part.
#For the instruction of using Apache Jena as well as the query explaination, please see the report.

import logging
import rdflib
from _pyio import open

# Configuring logging
logging.basicConfig()

query = """
PREFIX vgo: <http://www.semanticweb.org/mengchizhang/ontologies/VideoGame#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?Game_Title ?Composer ?Publisher ?Genre
WHERE {
  ?VideoGame vgo:has_title ?Game_Title .
  ?VideoGame vgo:composed_by ?Composer .
  ?VideoGame vgo:published_by ?Publisher .
  ?VideoGame vgo:has_genre ?Genre .
  FILTER (
    REGEX(Str(?Composer), "Masaharu")&&
    REGEX(Str(?Publisher), "Square") &&
    REGEX(Str(?Genre), "role")
  )
}
"""

# Creating the graph
g=rdflib.Graph()
result=g.parse("example_final.owl", "xml")
print("graph has %s statements.\n" % len(g))

# Querying and displaying the results
print ('{0:25s} {1:45s} {2:40s} {3:45}'.format("Game_Title","Composer","Publisher","Genre"))
for a,b,c,d in g.query(query):
    print ('{0:25s} {1:45s} {2:40s} {3:45}'.format(a,b,c,d))