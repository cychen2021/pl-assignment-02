test = {
  'name': 'Problem L2 (100 pts)',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (filter-lst even? '(0 1 1 2 3 5 8))
          (0 2 8)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'list)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
