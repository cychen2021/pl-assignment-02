test = {
  'name': 'Problem 6',
  'points': 150,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> eval_all(Pair(2, nil), env)
          c268a6a29ebaf25021185d36b329c434
          # locked
          >>> eval_all(Pair(4, Pair(5, nil)), env)
          0ab95ffe40ec65228e7afb779fbf50aa
          # locked
          >>> eval_all(nil, env) # return None (meaning undefined)
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> lst = Pair(1, Pair(2, Pair(3, nil)))
          >>> eval_all(lst, env)
          1351269de14c601ae8453ecc67560709
          # locked
          >>> lst     # The list should not be mutated!
          d35937a26aa4c4d1f86ee9a04092281b
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> env = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (begin (+ 2 3) (+ 5 6))
          3ad72f8913a675690a2adcc3f13e0739
          # locked
          scm> (begin (define x 3) x)
          1351269de14c601ae8453ecc67560709
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (begin 30 '(+ 2 2))
          0e5bbd1b15403208e2888ee24f3bf521
          # locked
          scm> (define x 0)
          64030e295636c5ae78e07a452cac2289
          # locked
          scm> (begin (define x (+ x 1)) 42 (define y (+ x 1)))
          557b055db9ceb996548b33392eedfbad
          # locked
          scm> x
          0f8a045127301b80ad84f23379cea71b
          # locked
          scm> y
          c268a6a29ebaf25021185d36b329c434
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (begin 30 'hello)
          hello
          scm> (begin (define x 3) (cons x '(y z)))
          (3 y z)
          scm> (begin (define x 3) (cons x '(x z)))
          (3 x z)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (begin (define x (+ x 1))
          ....        (define x (+ x 10))
          ....        (define x (+ x 100))
          ....        (define x (+ x 1000)))
          x
          scm> x
          1111
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
