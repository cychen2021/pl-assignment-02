test = {
  'name': 'Problem 1',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> global_frame = create_global_frame()
          >>> global_frame.define("x", 3)
          >>> global_frame.parent is None
          06ec923dd70ef4606b4ea940252d4e8b
          # locked
          >>> global_frame.lookup("x")
          1351269de14c601ae8453ecc67560709
          # locked
          >>> global_frame.define("x", 2)
          >>> global_frame.lookup("x")
          c268a6a29ebaf25021185d36b329c434
          # locked
          >>> global_frame.lookup("foo")
          55386b61b224cc69dcafef802309105a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> first_frame = create_global_frame()
          >>> first_frame.define("x", 3)
          >>> first_frame.define("y", False)
          >>> second_frame = Frame(first_frame)
          >>> second_frame.parent == first_frame
          06ec923dd70ef4606b4ea940252d4e8b
          # locked
          >>> second_frame.lookup("x")
          1351269de14c601ae8453ecc67560709
          # locked
          >>> second_frame.lookup("y")
          2d72b2741eeb5f0f806ace0172369f9c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> first_frame = create_global_frame()
          >>> first_frame.define("x", 3)
          >>> second_frame = Frame(first_frame)
          >>> third_frame = Frame(second_frame)
          >>> fourth_frame = Frame(third_frame)
          >>> fourth_frame.lookup("x")
          1351269de14c601ae8453ecc67560709
          # locked
          >>> second_frame.define("y", 1)
          >>> fourth_frame.lookup("y")
          0f8a045127301b80ad84f23379cea71b
          # locked
          >>> first_frame.define("y", 0)
          >>> fourth_frame.lookup("y")
          0f8a045127301b80ad84f23379cea71b
          # locked
          >>> fourth_frame.define("y", 2)
          >>> fourth_frame.lookup("y")
          c268a6a29ebaf25021185d36b329c434
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> first_frame = create_global_frame()
          >>> first_frame.define("x", 1)
          >>> second_frame = Frame(first_frame)
          >>> third_frame = Frame(second_frame)
          >>> fourth_frame = Frame(first_frame)
          >>> fifth_frame = Frame(fourth_frame)
          >>> fifth_frame.lookup("x")
          1
          >>> third_frame.lookup("x")
          1
          >>> second_frame.define("x", 2)
          >>> third_frame.lookup("x")
          2
          >>> fifth_frame.lookup("x")
          1
          >>> fifth_frame.define("x", 5)
          >>> fifth_frame.lookup("x")
          5
          >>> fourth_frame.lookup("x")
          1
          >>> first_frame.define("x", 4)
          >>> fourth_frame.lookup("x")
          4
          >>> third_frame.lookup("x")
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> +
          #[+]
          scm> display
          #[display]
          scm> hello
          SchemeError
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
