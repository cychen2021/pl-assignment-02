test = {
  'name': 'Problem 7',
  'points': 200,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (lambda (x y) (+ x y))
          242e76bc300c05c2937102bc2c7526fd
          # locked
          scm> (lambda (x)) ; type SchemeError if you think this causes an error
          55386b61b224cc69dcafef802309105a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (lambda (x) (+ x) (+ x x))
          (lambda (x) (+ x) (+ x x))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (lambda () 2)
          (lambda () 2)
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> lambda_line = read_line("(lambda (a b c) (+ a b c))")
          >>> lambda_proc = do_lambda_form(lambda_line.rest, env)
          >>> lambda_proc.formals # use single quotes ' around strings in your answer
          d8bcba0bb21629d9b63f5a48b30e6fe3
          # locked
          >>> lambda_proc.body # the body is a *list* of expressions! Make sure your answer is a properly nested Pair.
          79ade5c750887b0707b3f917994c5fe4
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> env = create_global_frame()
          >>> lambda_line = read_line("(lambda (x y) x)")
          >>> lambda_proc = do_lambda_form(lambda_line.rest, env)
          >>> isinstance(lambda_proc, LambdaProcedure)
          True
          >>> lambda_proc.env is env
          True
          >>> lambda_proc
          LambdaProcedure(Pair('x', Pair('y', nil)), Pair('x', nil), <Global Frame>)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      # >>> from scheme_reader import *
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
