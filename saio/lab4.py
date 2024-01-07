def get_memtable(B, v, c):
      area, value = v, c
      n = len(value) # находим размеры таблицы
      
      OPT = [[0 for b in range(B+1)] for i in range(n+1)]

      for i in range(n+1):
            for b in range(B+1):
                  if i == 0 or b == 0:
                        OPT[i][b] = 0

                  # если площадь предмета меньше площади столбца,
                  # максимизируем значение суммарной ценности
                  elif area[i-1] <= b:
                        OPT[i][b] = max(value[i-1] + OPT[i-1][b-area[i-1]], OPT[i-1][b])

                  # если площадь предмета больше площади столбца,
                  # забираем значение ячейки из предыдущей строки
                  else:
                        OPT[i][b] = OPT[i-1][b]       
      return OPT, area, value

def get_selected_items_list(B, v, c):
      OPT, area, value = get_memtable(B, v, c)
      n = len(value)
      res = OPT[n][B]      # начинаем с последнего элемента таблицы
      b = B 
      items_list = []    # список площадей и ценностей
    
      for i in range(n, 0, -1):  
            if res <= 0:  # собрали "рюкзак" 
                  break
            if res == OPT[i-1][b]:  
                  continue
            else:
                  items_list.append(i)
                  res -= value[i-1]   
                  b -= area[i-1]  
            
      return OPT[n][B], items_list

def main():
    B = 5
    c = [1, 2, 3]
    v = [4, 5, 1]
    max_price, items = get_selected_items_list(B, v, c)
    print(max_price)
    print(items)

if __name__ == "__main__":
      main()   
