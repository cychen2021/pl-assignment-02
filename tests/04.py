test = {
  'name': 'Problem 4',
  'points': 200,
  'suites': [
    {
      'cases': [
        {
          'answer': 'c059a52bf86f2c6183f1afc265d5ded1',
          'choices': [
            r"""
            Pair(A, Pair(B, nil)), where:
                A is the symbol being bound,
                B is an expression whose value should be evaluated and bound to A
            """,
            r"""
            Pair(A, Pair(B, nil)), where:
                A is the symbol being bound,
                B is the value that should be bound to A
            """,
            r"""
            Pair(A, B), where:
                A is the symbol being bound,
                B is the value that should be bound to A
            """,
            r"""
            Pair(A, B), where:
                A is the symbol being bound,
                B is an expression whose value should be evaluated and bound to A
            """,
            r"""
            Pair('define', Pair(A, Pair(B, nil))), where:
                A is the symbol being bound,
                B is an expression whose value should be evaluated and bound to A
            """
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the structure of the expressions argument to do_define_form?'
        },
        {
          'answer': '4fee4e15275ef812930c8176277445f2',
          'choices': [
            'make_child_frame',
            'define',
            'lookup',
            'bindings'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          What method of a Frame instance will bind
          a value to a symbol in that frame?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define size 2)
          9c37c086ea50549f85419efca0d7ea92
          # locked
          scm> size
          c268a6a29ebaf25021185d36b329c434
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x (+ 2 3))
          64030e295636c5ae78e07a452cac2289
          # locked
          scm> x
          0ab95ffe40ec65228e7afb779fbf50aa
          # locked
          scm> (define x (+ 2 7))
          64030e295636c5ae78e07a452cac2289
          # locked
          scm> x
          1112648aa05de799cad1273f921dfa13
          # locked
          scm> (eval (define tau 6.28)) ; eval takes an expression represented as a list and evaluates it
          0396f79ad1e5a2bebf2ea974b0c3faae
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define pi 3.14159)
          pi
          scm> (define radius 10)
          radius
          scm> (define area (* pi (* radius radius)))
          area
          scm> area
          314.159
          scm> (define radius 100)
          radius
          scm> radius
          100
          scm> area
          314.159
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define 0 1)
          SchemeError
          scm> (define error (/ 1 0))
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
