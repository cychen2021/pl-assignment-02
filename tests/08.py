test = {
  'name': 'Problem 8',
  'points': 200,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> formals = Pair('a', Pair('b', Pair('c', nil)))
          >>> vals = Pair(1, Pair(2, Pair(3, nil)))
          >>> frame = global_frame.make_child_frame(formals, vals)
          >>> global_frame.lookup('a') # Type SchemeError if you think this errors
          55386b61b224cc69dcafef802309105a
          # locked
          >>> frame.lookup('a')        # Type SchemeError if you think this errors
          0f8a045127301b80ad84f23379cea71b
          # locked
          >>> frame.lookup('b')        # Type SchemeError if you think this errors
          c268a6a29ebaf25021185d36b329c434
          # locked
          >>> frame.lookup('c')        # Type SchemeError if you think this errors
          1351269de14c601ae8453ecc67560709
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> frame = global_frame.make_child_frame(nil, nil)
          >>> frame.parent is global_frame
          06ec923dd70ef4606b4ea940252d4e8b
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> first = Frame(global_frame)
          >>> second = first.make_child_frame(nil, nil)
          >>> second.parent is first
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # More argument values than formal parameters
          >>> global_frame.make_child_frame(Pair('a', nil), Pair(1, Pair(2, Pair(3, nil))))
          SchemeError
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # More formal parameters than argument values
          >>> global_frame.make_child_frame(Pair('a', Pair('b', Pair('c', nil))), Pair(1, nil))
          SchemeError
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Values can be pairs.
          >>> formals = Pair('a', Pair('b', nil))
          >>> values = Pair(Pair(1, nil), Pair(Pair(2, nil), nil))
          >>> frame = global_frame.make_child_frame(formals, values)
          >>> frame.lookup('a')
          Pair(1, nil)
          >>> frame.lookup('b')
          Pair(2, nil)
          >>> frame2 = frame.make_child_frame(nil, nil) # Bind parents correctly
          >>> frame2.lookup('a')
          Pair(1, nil)
          >>> formals # Ensure that formals was not mutated
          Pair('a', Pair('b', nil))
          >>> values # Ensure that values was not mutated
          Pair(Pair(1, nil), Pair(Pair(2, nil), nil))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
