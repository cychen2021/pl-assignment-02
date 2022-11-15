;;; Assignment 2, section 2: Scheme Lists

;;; Required Problems


; Problem L1

(define lst
  (list (list 1) 2 (list 3 4) 5)
)


; Problem L2

(define (filter-lst fn lst)
  (if (null? lst) nil (if (fn (car lst))
      (cons (car lst) (filter-lst fn (cdr lst)))
      (filter-lst fn (cdr lst))))
)
