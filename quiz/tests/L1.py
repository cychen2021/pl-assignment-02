test = {
  'name': 'Problem L1 (100 pts)',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> lst
          ((1) 2 (3 4) 5)
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
