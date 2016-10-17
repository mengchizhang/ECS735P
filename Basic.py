# This script is for construct and populate data into my own ontology

import logging
import rdflib
from rdflib.graph import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, RDF
from rdflib.plugins.memory import IOMemory

# Configuring logging
logging.basicConfig()
 
# Configuring the end-point and constructing query
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
construct_query="""
      PREFIX vgo: <http://www.semanticweb.org/mengchizhang/ontologies/VideoGame#>
      PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>        
      PREFIX foaf: <http://xmlns.com/foaf/0.1/>
      PREFIX dbo: <http://dbpedia.org/ontology/>
      PREFIX dbp: <http://dbpedia.org/property/>
      
      CONSTRUCT {
      ?VideoGame rdf:type vgo:VideoGame .
      ?VideoGame vgo:developed_by ?developer .
      ?developer rdf:type vgo:Developer .
      ?VideoGame vgo:published_by ?publisher .
      ?publisher rdf:type vgo:Publisher .
      ?VideoGame vgo:composed_by ?composer .
      ?composer rdf:type vgo:Composer .
      ?VideoGame vgo:designed_by ?designer .
      ?designer rdf:type vgo:Designer .
      ?VideoGame vgo:directed_by ?director .
      ?director rdf:type vgo:Director .
      ?VideoGame vgo:produced_by ?producer .
      ?producer rdf:type vgo:Producer .
      ?VideoGame vgo:written_by ?writer .
      ?writer rdf:type vgo:Writer .
      ?VideoGame vgo:has_genre ?genre .    
      ?genre rdf:type vgo:GameGenre .      
      ?VideoGame vgo:released_for ?platform .
      ?platform rdf:type vgo:computingPlatform .
      ?VideoGame vgo:use_engine ?engine .
      ?engine rdf:type vgo:gameEngine .
      ?VideoGame vgo:released_on ?releaseDate .
      ?VideoGame vgo:has_title ?title .
      ?VideoGame vgo:artist_name ?artist .
      ?VideoGame vgo:programmer_name ?programmer .
      ?VideoGame vgo:award_name ?award .
      ?VideoGame vgo:ign_rating ?ign .
      }
       WHERE{
       ?VideoGame rdf:type dbo:VideoGame .
       ?VideoGame foaf:name ?title
       OPTIONAL {?VideoGame dbo:developer ?developer}
       OPTIONAL {?VideoGame dbo:publisher ?publisher}
       OPTIONAL {?VideoGame dbo:composer ?composer}
       OPTIONAL {?VideoGame dbo:designer ?designer}
       OPTIONAL {?VideoGame dbo:director ?director}
       OPTIONAL {?VideoGame dbo:producer ?producer}
       OPTIONAL {?VideoGame dbo:writer ?writer}
       OPTIONAL {?VideoGame dbo:genre ?genre}
       OPTIONAL {?VideoGame dbo:computingPlatform ?platform}      
       OPTIONAL {?VideoGame dbo:gameEngine ?engine}
       OPTIONAL {?VideoGame dbo:releaseDate ?releaseDate}
       OPTIONAL {?VideoGame dbp:artist ?artist}
       OPTIONAL {?VideoGame dbp:programmer ?programmer}
       OPTIONAL {?VideoGame dbp:award ?award}
       OPTIONAL {?VideoGame dbp:ign ?ign}
       }
       """

sparql.setQuery(construct_query)
sparql.setReturnFormat(RDF)

# Creating the RDF store and graph
memory_store=IOMemory()
graph_id=URIRef("http://www.semanticweb.org/mengchizhang/ontologies/VideoGame")
g = Graph(store=memory_store, identifier=graph_id)
rdflib.plugin.register('sparql', rdflib.query.Processor, 'rdfextras.sparql.processor', 'Processor')
rdflib.plugin.register('sparql', rdflib.query.Result, 'rdfextras.sparql.query', 'SPARQLQueryResult')

# Merging results and saving the store
g = sparql.query().convert()
g.parse("VideoGame.owl")
g.serialize("example_final.owl", "xml")
