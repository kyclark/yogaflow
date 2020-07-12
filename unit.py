import io
from yogaflow import pairs, read_training


# --------------------------------------------------
def test_pairs():
    """ Test pairs """

    assert pairs([]) == []
    assert pairs([1]) == []
    assert pairs([1, 2]) == [(1, 2)]
    assert pairs([1, 2, 3]) == [(1, 2), (2, 3)]
    assert pairs([1, 2, 3, 4]) == [(1, 2), (2, 3), (3, 4)]
    assert pairs(['foo']) == []
    assert pairs(['foo', 'bar']) == [('foo', 'bar')]
    assert pairs(['foo', 'bar', 'baz']) == [('foo', 'bar'), ('bar', 'baz')]
    assert pairs(['foo', 'bar', 'baz', 'quux']) == [('foo', 'bar'),
                                                    ('bar', 'baz'),
                                                    ('baz', 'quux')]


# --------------------------------------------------
def test_read_training():
    """ Test read_training """

    t1 = io.StringIO('foo\nbar\nbaz\n')
    t2 = io.StringIO('foo\nquux\nbar\n')
    t3 = io.StringIO('bar\nblip\nflop\n')

    expected = {
        'bar': ['baz', 'blip'],
        'blip': ['flop'],
        'foo': ['bar', 'quux'],
        'quux': ['bar']
    }

    assert read_training([t1, t2, t3]) == expected
