from linked_list import LinkedList
import pytest

def test_can_pass():
  assert True == True

@pytest.fixture
def ll():
  return LinkedList()

def test_search_on_empty_list_creates_error(ll):
  with pytest.raises(IndexError):
    ll.search(0)

def test_a_single_item_can_be_added_and_searched(ll):
  ll.add_head(123)
  assert ll.search(0) == 123

def test_two_items_can_be_added_and_can_be_searched_in_the_correct_order(ll):
  ll.add_head(123)
  ll.add_head(456)
  assert ll.search(0) == 456
  assert ll.search(1) == 123

def test_more_items_can_be_added_and_can_be_searched_in_the_correct_order(ll):
  ll.add_head("cow")
  ll.add_head("chicken")
  ll.add_head("mom")
  assert ll.search(0) == "mom"
  assert ll.search(1) == "chicken"
  assert ll.search(2) == "cow"