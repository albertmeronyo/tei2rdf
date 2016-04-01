# to @mhbeals

from rdflib import Graph, URIRef, RDF, RDFS, Literal
import xml.etree.ElementTree

e = xml.etree.ElementTree.parse('TEISAP.xml').getroot()

g = Graph()

iden = 0
for p in e.findall('.//TEI'):
    elem = URIRef("http://www.ancientwisdoms.ac.uk/mss/" + str(iden))
    el_type = URIRef("http://purl.org/saws/ontology#LinguisticObject")

    text = p.find('text/body/p').text

    g.add( (elem, RDF.type, el_type) )
    g.add( (elem, RDFS.label, Literal(text)))

    iden += 1

g.serialize('mhb.ttl', format='turtle')
