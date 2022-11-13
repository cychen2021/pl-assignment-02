test = {
  'name': 'Problem 11',
  'points': 150,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (and)
          d832513e077c68c940a0abe7f3e3f3f5
          # locked
          scm> (and 1 #f)
          09910494a8b90e19b00bc155c15f02fb
          # locked
          scm> (and (+ 1 1) 1)
          0f8a045127301b80ad84f23379cea71b
          # locked
          scm> (and #f 5)
          09910494a8b90e19b00bc155c15f02fb
          # locked
          scm> (and 4 5 (+ 3 3))
          44f8cd5ad836105d8294c2d770d19891
          # locked
          scm> (not (and #t #f 42 (/ 1 0)))
          d832513e077c68c940a0abe7f3e3f3f5
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (not (and #f))
          #t
          scm> (and 3 2 #f)
          #f
          scm> (and 3 2 1)
          1
          scm> (and 3 #f 5)
          #f
          scm> (and 0 1 2 3)
          3
          scm> (define (true-fn) #t)
          true-fn
          scm> (and (true-fn))
          #t
          scm> (define x #f)
          x
          scm> (and x #t)
          #f
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (and (define x (+ x 1))
          ....      (define x (+ x 10))
          ....      (define x (+ x 100))
          ....      (define x (+ x 1000)))
          x
          scm> x
          1111
          scm> (define x 0)
          x
          scm> (and (define x (+ x 1))
          ....      (define x (+ x 10))
          ....      #f
          ....      (define x (+ x 100))
          ....      (define x (+ x 1000)))
          #f
          scm> x
          11
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (and #t #t #t #t))
          no-mutation
          scm> no-mutation
          (lambda () (and #t #t #t #t))
          scm> (no-mutation)
          #t
          scm> no-mutation ; `and` should not cause mutation
          (lambda () (and #t #t #t #t))
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
          scm> (or)
          09910494a8b90e19b00bc155c15f02fb
          # locked
          scm> (or (+ 1 1))
          c268a6a29ebaf25021185d36b329c434
          # locked
          scm> (not (or #f))
          d832513e077c68c940a0abe7f3e3f3f5
          # locked
          scm> (define (zero) 0)
          16d1aec60d9b36cba4c693ff2bb08fe5
          # locked
          scm> (or (zero) 3)
          6d4f64ea4b8847aa1e3e405ec90fd538
          # locked
          scm> (or 4 #t (/ 1 0))
          290aa5770785fe46a438d3826545dbc4
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (or 5 2 1)
          5
          scm> (or 0 1 2)
          0
          scm> (or #f (- 1 1) 1)
          0
          scm> (or 'a #f)
          a
          scm> (or (< 2 3) (> 2 3) 2 'a)
          #t
          scm> (or (< 2 3) 2)
          #t
          scm> (define (false-fn) #f)
          false-fn
          scm> (or (false-fn) 'yay)
          yay
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x 0)
          x
          scm> (or (begin (define x (+ x 1)) #f)
          ....     (begin (define x (+ x 10)) #f)
          ....     (begin (define x (+ x 100)) #f)
          ....     (begin (define x (+ x 1000)) #f))
          #f
          scm> x
          1111
          scm> (define x 0)
          x
          scm> (or (begin (define x (+ x 1)) #f)
          ....     (begin (define x (+ x 10)) #f)
          ....     #t
          ....     (begin (define x (+ x 100)) #f)
          ....     (begin (define x (+ x 1000)) #f))
          #t
          scm> x
          11
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (no-mutation) (or #f #f #f #f))
          no-mutation
          scm> no-mutation
          (lambda () (or #f #f #f #f))
          scm> (no-mutation)
          #f
          scm> no-mutation ; `or` should not cause mutation
          (lambda () (or #f #f #f #f))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (greater-than-5 x) (if (> x 5) #t #f))
          greater-than-5
          scm> (define (other y) (or (greater-than-5 y) #f))
          other
          scm> (other 2)
          #f
          scm> (other 6) ; test for mutation
          #t
          scm> (define (other y) (and (greater-than-5 y) #t))
          other
          scm> (other 2)
          #f
          scm> (other 6) ; test for mutation
          #t
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
