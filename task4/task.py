import numpy as np

def task():
  min_score = 1
  max_score = 6

  all_variants_count = max_score * max_score
  mults_count = all_variants_count
  sums_count = max_score * 2 - min_score * 2 + 1

  # формирование исходной матрицы

  variants = [[0 for j in range(mults_count)] for i in range(sums_count)]
  mult_norm = 1
  sum_norm = 2

  used_cols = set()

  for i in range(min_score, max_score + 1):
    for j in range(min_score, max_score + 1):
      cur_mult = i * j
      cur_sum = i + j

      used_cols.add(cur_mult - mult_norm)
      variants[cur_sum - sum_norm][cur_mult - mult_norm] += 1

  resized_variants = []

  for i in range(sums_count):
    cur_row = []

    for j in range(mults_count):
      if (j in used_cols):
        cur_row.append(variants[i][j])

    resized_variants.append(cur_row)

  matrix = np.array(resized_variants)
  mults_count = len(resized_variants[0])

  # получение матрицы вероятностей
  matrix = matrix * 1.0 / all_variants_count

  # получение массива сумм по строкам (A)
  PA = matrix.sum(axis=1)

  # получение массива сумм по столбцам (B)
  PB = matrix.sum(axis=0)

  # получение матриц и массивов энтропий
  def entropiya(p):
    if (p != 0):
      return -p * np.log2(p)
    else:
      return 0
  
  vectorized_entropiya = np.vectorize(entropiya)

  matrix = vectorized_entropiya(matrix)
  PA = vectorized_entropiya(PA)
  PB = vectorized_entropiya(PB)

  # вычисление энтропий H(AB), H(A), H(B), Ha(B), H(I(A,B))

  HA = np.sum(PA)
  HB = np.sum(PB)
  HAB = np.sum(matrix)
  HaB = HAB - HA
  HI = HB - HaB

  # return result
  def toFixed(num):
    return format(num, '.2f')

  return [toFixed(HAB), toFixed(HA), toFixed(HB), toFixed(HaB), toFixed(HI)]

print(task())