#This is a query for getting most recent high rating awarded playstation game.
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

    SELECT ?Game_Title ?Platform ?IGN_Score ?Release_Date ?Award

    WHERE {
      ?VideoGame rdf:type vgo:VideoGame .
      ?VideoGame vgo:has_title ?Game_Title .
      ?VideoGame vgo:released_for ?Platform .
      ?VideoGame vgo:ign_rating ?IGN_Score .
      ?VideoGame vgo:released_on ?Release_Date .
      ?VideoGame vgo:award_name ?Award .
      FILTER (
        (?IGN_Score > 9) &&
        REGEX(Str(?Platform), "PlayStation_3") &&
        REGEX(Str(?Award), "Game_of_the_Year")
      ) 
    }

    ORDER BY DESC(?Release_Date)
    """

# Creating the graph
g=rdflib.Graph()
result=g.parse("example_final.owl", "XML")
print("graph has %s statements.\n" % len(g))

# Querying and displaying the results
print ('{0:20s} {1:43s} {2:20s} {3:20s} {4:30s}'.format("Game_Title","Platform","IGN_Rating", "Release_Date", "Award"))
for a,b,c,d,e in g.query(query):
    print ('{0:20s} {1:43s} {2:20s} {3:20s} {4:30s}'.format(a,b,c,d,e))