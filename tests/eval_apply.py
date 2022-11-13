test = {
  'name': 'Understanding Eval/Apply',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '375964137237a991e6f99a58281e1369',
          'choices': [
            'Call expressions and special forms',
            'Only call expressions',
            'Only special forms',
            'All expressions are represented as Pairs'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What types of expressions are represented as Pairs?'
        },
        {
          'answer': '9de9670c324cebfed1eb99bc85f7fada',
          'choices': [
            'env.find(name)',
            'scheme_symbolp(expr)',
            'env.lookup(expr)',
            'scheme_forms.SPECIAL_FORMS[first](rest, env)'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What expression in the body of scheme_eval finds the value of a name?'
        },
        {
          'answer': 'fd9d52a0385f1e784fe4f58d667e49a1',
          'choices': [
            r"""
            Check if the first element in the list is a symbol and that the
            symbol is in the dictionary SPECIAL_FORMS
            """,
            'Check if the first element in the list is a symbol',
            'Check if the expression is in the dictionary SPECIAL_FORMS'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How do we know if a given combination is a special form?'
        },
        {
          'answer': '1b1c2ddfb2c1d33aac1c17e65eb6aeed',
          'choices': [
            'I only',
            'II only',
            'III only',
            'I and II',
            'I and III',
            'II and III',
            'I, II and III'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          What is the difference between applying builtins and applying user-defined procedures?
          (Choose all that apply)
          
          I.   User-defined procedures open a new frame; builtins do not
          II.  Builtins simply execute a predefined function; user-defined
               procedures must evaluate additional expressions in the body
          III. Builtins have a fixed number of arguments; user-defined procedures do not
          
          ---
          """
        },
        {
          'answer': 'aca6328dfa7b2c955645cdcb4dd112b7',
          'choices': [
            'SchemeError("malformed list: (1)")',
            'SchemeError("1 is not callable")',
            'AssertionError',
            'SchemeError("unknown identifier: 1")'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What exception should be raised for the expression (1)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
