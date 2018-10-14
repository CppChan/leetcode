class Sever(object):
  hosttype_server = {}
  def next_server_number(self, server):
  	n = len(server)
  	for i in range(n):
  		while server[i]>0 and server[i]<=n and server[server[i]-1]!=server[i]:
  			swap = server[i]-1
  			server[i],server[swap] = server[swap],server[i]
  	for i in range(len(server)):
  		if server[i]!=i+1:return i+1
  	return n+1

  def allocate(self, hosttype):
  	if hosttype not in self.hosttype_server: self.hosttype_server[hosttype] = []
  	server_num = self.next_server_number(self.hosttype_server[hosttype])
  	self.hosttype_server[hosttype].append(server_num)
  	return hosttype+str(server_num)

  def deallocate(self, hostname):
  	for i in range(len(hostname)-1,-1,-1):
  		if not hostname[i].isdigit():break
  	server_num, hosttype= int(hostname[i+1: len(hostname)]), hostname[:i+1]
  	server_list = self.hosttype_server[hosttype]
  	for i in range(len(server_list)):
  		if server_list[i]==server_num:
  			server_list.pop(i)
  			break

if __name__ == "__main__":
    s = Sever()
    print s.allocate('abc')
    print s.allocate('abc')
    print s.allocate('abc')
    print s.allocate('abc')
    print s.allocate('abc')
    s.deallocate('abc3')
    s.deallocate('abc2')
    print s.allocate('abc')
    print s.allocate('efg')