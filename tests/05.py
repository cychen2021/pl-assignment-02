test = {
  'name': 'Problem 5',
  'points': 150,
  'suites': [
    {
      'cases': [
        {
          'answer': '4e29d76ed91f86d9b79bb36589747663',
          'choices': [
            r"""
            Pair('quote', Pair(A, nil)), where:
                A is the quoted expression
            """,
            r"""
            [A], where:
                A is the quoted expression
            """,
            r"""
            Pair(A, nil), where:
                A is the quoted expression
            """,
            r"""
            A, where:
                A is the quoted expression
            """
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the structure of the expressions argument to do_quote_form?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> do_quote_form(Pair(3, nil), global_frame)
          1351269de14c601ae8453ecc67560709
          # locked
          >>> do_quote_form(Pair('hi', nil), global_frame)
          d6af908677dab821d7d9b3126570560b
          # locked
          >>> expr = Pair(Pair('+', Pair('x', Pair(2, nil))), nil)
          >>> do_quote_form(expr, global_frame) # Make sure to use Pair notation
          582c4e1461ad3d910c490d4e6b2ced2c
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
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> ''hello
          20f45bb2ec437e1e9b79d546f7d06233
          # locked
          scm> (quote (1 2))
          b70abaea0b3ae77610089bf1416daa87
          # locked
          scm> (car '(1 2 3))
          0f8a045127301b80ad84f23379cea71b
          # locked
          scm> (cdr '(1 2))
          578e0ccae301441c646f9842080cb112
          # locked
          scm> (cons 'car '('(4 2)))
          e3e4c89cb2c949747418483ae7f0fb8e
          # locked
          scm> (eval (cons 'car '('(4 2))))
          290aa5770785fe46a438d3826545dbc4
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (quote hello)
          hello
          scm> 'hello
          hello
          scm> ''hello
          (quote hello)
          scm> (quote (1 2))
          (1 2)
          scm> '(1 2)
          (1 2)
          scm> (car (car '((1))))
          1
          scm> (quote 3)
          3
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
