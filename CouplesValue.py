def Count(arr):
  uniqueArr = set(arr)
  uniqueCount = []
  for i in uniqueArr:
    tmp = arr.count(i)
    uniqueCount.append(tmp)

  couples = 0
  for i in uniqueCount:
    tmp = i//2
    couples +=tmp
  return couples

arr1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
arr2 = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]
arr3 = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
res1 = Count(arr1)
res2 = Count(arr2)
res3 = Count(arr3)
print("Hasil Soal 1 = ",res1,"  Hasil Soal 2 = ",res2,"  Hasil Soal 3 = ",res3)