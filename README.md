# using_trackpy
I have a used trackpy with HDF5 xyt hyperstack movies and with avi movies. Here are my ipython notebooks.

### choosing_trajectories_of_particles_that_travel_further_than_some_threshold.ipynb

 This notebook 
 1. opens an HDF5 xyt hyperstack file, 
 2. converts it (slowly) into a file that can be used with trackpy, 
 3. backgrounds the movie but recovers if there is not enough memory available, 
 4. locates dark spots in the movie, 
 5. links these into trajectories, 
 6. filters out trajectories of few frames using filter_stubs, 
 7. filters out trajectories of particles that move a distance below some threshold (currently 4 microns), and 
 8. saves the results (below an 'error' lines that prevents accidentally saving the results if you run the whole notebook.

(original file name: 2015-09-15 movie150902,17 particles in droplet _ save trajectories, minimal human intervention, improved_2016-02-10.ipynb)

### backgrounding_color_avi_movie_examples.ipynb

This notebook shows some examples of how to work with a color avi file in python. If you run into errors opening an avi file using pims, make sure to run the setup script, available at https://github.com/vivarose/setup_script.

(original file name: 2015-02-20 & 06-25 & 07-01 Background subtracting color -- red swimmers and blue tracers.ipynb)
