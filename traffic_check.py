from collections import defaultdict
def traffic_check(filename):
	services=defaultdict(list)
	with open(filename, 'r') as file:
		file.readline()
		for line in file:
			service,cell,qps,throughput = line.split()
			for item in [service,cell]:
				if item not in services:
					services[item].append(int(qps))
					services[item].append(int(throughput))
				else:
					services[item][0] +=int(qps)
					services[item][1] +=int(throughput)
			
	sorted_services= sorted(services.items(), key=lambda x:x[0])
	for item,count in sorted_services:
		print(f'{item}, QPS: {count[0]}, Throughput(Mbps): {count[1]}')

traffic_check('service.txt')