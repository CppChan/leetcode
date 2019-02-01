class Solution(object):
    def prisonAfterNDays(self, cells, N):
        pre, loop, start= {}, None, N
        while N>0:
            newcell = [0]
            for i in range(1, len(cells)-1):
                if cells[i-1]==cells[i+1]: newcell.append(1)
                else:newcell.append(0)
            newcell.append(0)
            newcell = tuple(newcell)
            if newcell in pre:
                loop = pre[newcell]-N #detect loop
                N%=loop
            pre[newcell]=N
            cells = newcell
            N-=1
        return cells