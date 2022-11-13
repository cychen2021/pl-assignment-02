test = {
  'name': 'Problem 10',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (f x y) (+ x y))
          206c1f5e311d5bea20cf0df87f8bb1ea
          # locked
          scm> f
          242e76bc300c05c2937102bc2c7526fd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (f) (+ 2 2))
          f
          scm> f
          (lambda () (+ 2 2))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (f x) (* x x))
          206c1f5e311d5bea20cf0df87f8bb1ea
          # locked
          scm> f
          ba5840280a625be3bafcfa3a09762b83
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (foo x) 1 2 3 4 5)
          foo
          scm> foo
          (lambda (x) 1 2 3 4 5)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (foo) (/ 1 0))
          foo
          scm> foo
          (lambda () (/ 1 0))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (f 1 2 3) 4) ; check that you have valid formals
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
    },
    {
      'cases': [
        {
          'code': r"""
          >>> inp = read_line("(define (f x) x)")
          >>> scheme_eval(inp, env)
          'f'
          >>> scheme_eval('f', env)
          LambdaProcedure(Pair('x', nil), Pair('x', nil), <Global Frame>)
          >>> inp == read_line("(define (f x) x)") # Don't mutate the input expression!
          True
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
      >>> env = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
