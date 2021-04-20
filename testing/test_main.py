from main import get_none
from main import flatten_dict

# Test part 1.1

def test_get_none():
    assert get_none() == None

# Test part 2.1

def test_flatten_dict_type():
    assert type(flatten_dict({'a': 42, 'b': 3.14})) == list

def test_flatten_single():
    assert flatten_dict({'a': 42}) == [42]

def test_flatten_dict():
    assert flatten_dict({'a': 42, 'b': 3.14}) == [42, 3.14]

def test_flatten_dict2():
    assert flatten_dict({'a': [42, 350], 'b': 3.14}) == [[42, 350], 3.14]

def test_flatten_multiple():
    assert flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [42, 350, 3.14]

#def test_flatten_multiple2():
#    assert flatten_dict({'a': [{'inner_inner_a': 42}]}) == [42]
