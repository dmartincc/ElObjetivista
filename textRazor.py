from textrazor import TextRazor

client = TextRazor(YOUR_API_KEY_HERE, extractors=["entities"])

response = client.analyze(text)

entities = list(response.entities())
entities.sort(key=lambda x: x.relevance_score, reverse=True)

seen = set()
for entity in entities:
	if entity.id not in seen:
		print entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types
		seen.add(entity.id)