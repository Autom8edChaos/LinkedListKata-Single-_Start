from linked_list import LinkedList
from out_of_bound_error import OutOfBoundError
import pytest

def test_can_pass():
  assert True == True

@pytest.fixture()
def ll():
  return LinkedList()

def test_search_empty_raises_error(ll):
  with pytest.raises(RuntimeError):
    ll.search(0)
    
def test_one_item_to_the_head_and_find_it(ll):
  ll.add_head("one")
  assert ll.search(0) == "one"
 
def test_searching_for_not_existing_index_raises_an_error(ll):
  ll.add_head('linde')
  with pytest.raises(OutOfBoundError):
    ll.search(1)

def test_add_two_items_to_the_head_and_find_second(ll):
  ll.add_head("first")
  ll.add_head("second")
  assert ll.search(0) == "second"
  assert ll.search(1) == "first"

def test_add_more_items_to_the_head_and_find_all(ll):
  ll.add_head("first")
  ll.add_head("second")
  ll.add_head("last")
  assert ll.search(0) == "last"
  assert ll.search(1) == "second"
  assert ll.search(2) == "first"