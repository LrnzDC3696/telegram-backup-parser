import vampytest
from margelet import TextEntity


example_test_entity_type = "plain"
example_test_entity_text = "plain"
example_text_entity = {
    "type": example_test_entity_type,
    "text": example_test_entity_text,
}


def test_text_entity():
    entity_init = TextEntity(example_test_entity_type, example_test_entity_text)
    entity_from_dict = TextEntity.from_dict(example_text_entity)
    vampytest.assert_eq = (entity_init, entity_from_dict)
