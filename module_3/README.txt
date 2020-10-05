Several important things to consider are mentaioned below.

1) 
	Model uses an external source: worldcities.csv that comes from https://www.kaggle.com/viswanathanc/world-cities-datasets. 
	This file is stored locally and used inside the "your_first_model.ipynb".

2) 
	Model uses an external source: with_additional_data_from_TA_ALL_2.csv
	This file is basically an original csv (main task.xls) with additional data about review dates coming from www.tripadvisor.com.
	This data was extracted using a self-coded web crawler based on "requests" and "beautifulsoup" libraries. The actual crawler is stored
	in a file called "workers.py" (function "from_website") along with another function called "apply_to_dataframe". The second function is used
	to call "from_website" and pass it to the function "parallelize_dataframe" within the "your_first_model.ipynb". This approach is required because
	otherwise it would take a long time to get the data from tripadvisor. Using a separate file for worker functions was required because otherwise 
	it's impossible to use multithreading in Jupyter Notebooks on windows.

	Please note, that the data is already extracted and you don't really need to use this function anymore. It's here for the reference and only to prove
	the source of additional data.

