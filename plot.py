import numpy as np
# from basic_units import cm, inch
import matplotlib.pyplot as plt

def plot_clusters(datas,N,n_column = 2):
	
	
	ind = np.arange(N)    # the x locations for the groups


	# p1 = plt.bar(ind, data, width, yerr=menStd)
	# p2 = plt.bar(ind, wodata, width,
	#              bottom=data, yerr=womenStd)



	fig, axs = plt.subplots(n_column, int(N/n_column))

	for x in range(n_column):
		for y in range( int(N/n_column)):
			axs[x, y].bar(ind, datas[ y + x * int(N/2) ])

	
	# axs[0, 1].bar(ind, data)
	# axs[0, 2].bar(ind, data)
	# axs[0, 3].bar(ind, data)
	# axs[0, 4].bar(ind, data)

	# axs[1, 0].bar(ind, data)
	# axs[1, 1].bar(ind, data)
	# axs[1, 2].bar(ind, data)
	# axs[1, 3].bar(ind, data)
	# axs[1, 4].bar(ind, data)


	fig.tight_layout()
	plt.show()


if __name__ == "__main__":
    # execute only if run as a script
    data = (.20, .35, .30, .35, .27, .20, .35, .30, .35, .27)
    datas = []
    for i in range(10):
    	datas.append(data)
    # 
    plot_clusters(datas,10,2)
    main()
