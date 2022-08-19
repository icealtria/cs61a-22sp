(define (tail-replicate x n)
  ; BEGIN
  (define (helper x n s)
    (if (= n 0)
    s
    (helper x (- n 1) (cons x s)))
  )
  (helper x n nil)
  ; END
)