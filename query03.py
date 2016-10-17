#This is a query for getting the full staff list of a game that can be played on Windows and using Unreal game engine.
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

SELECT ?Game_Title ?Platform ?Engine ?Developer ?Publisher ?Artist ?Designer ?Director ?Producer ?Programmer

WHERE {
  ?VideoGame vgo:has_title ?Game_Title .
  ?VideoGame vgo:released_for ?Platform .
  ?VideoGame vgo:use_engine ?Engine .
  ?VideoGame vgo:developed_by ?Developer .
  ?VideoGame vgo:published_by ?Publisher .
  ?VideoGame vgo:artist_name ?Artist .
  ?VideoGame vgo:designed_by ?Designer .
  ?VideoGame vgo:directed_by ?Director .
  ?VideoGame vgo:produced_by ?Producer .
  ?VideoGame vgo:programmer_name ?Programmer .
  FILTER (
    REGEX(Str(?Platform), "Windows") &&
    REGEX(Str(?Engine), "Unreal")
  ) 
}
"""

# Creating the graph
g=rdflib.Graph()
result=g.parse("example_final.owl", "xml")
print("graph has %s statements.\n" % len(g))

# Querying and displaying the results
print ('{0:25s} {1:45s} {2:40s} {3:45} {4:30} {5:30} {6:30} {7:30} {8:30} {9:30}'.format("Game_Title","Platform","Engine","Developer","Publisher","Artist","Designer","Director","Producer","Programmer"))
for a,b,c,d,e,f,g,h,i,j in g.query(query):
    print ('{0:25s} {1:45s} {2:40s} {3:45} {4:30} {5:30} {6:30} {7:30} {8:30} {9:30}'.format(a,b,c,d,e,f,g,h,i,j))