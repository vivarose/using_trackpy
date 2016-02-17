# using_trackpy
I have used trackpy with HDF5 xyt hyperstack movies and with avi movies. Here are my ipython notebooks.

### tracking_avi_movie_and_saving_movie_of_trajectories.ipynb
This notebook
1. opens a color avi movie in greyscale,
2. calculates median darkcount and bright background images, 
3. backgrounds the movie with both darkcount and bright background images, but recovers if there is not enough memory available,
4. locates dark spots in the movie with trackpy, 
5. links these into trajectories with trackpy, 
6. filters out trajectories of few frames using trackpy.filter_stubs, 
7. saves the results, 
8. creates a movie of the particle trajectories.

(original file name: 2016-02-11_tracking_movie_2016-01-26-01_60x1.0_Hematite_swimmers.ipynb)

### choosing_trajectories_of_particles_that_travel_further_than_some_threshold.ipynb
 This notebook 
 1. opens an HDF5 xyt hyperstack file, 
 2. converts it (slowly) into a file that can be used with trackpy, 
 3. background divides the movie but recovers if there is not enough memory available, 
 4. locates dark spots in the movie, 
 5. links these into trajectories, 
 6. filters out trajectories of few frames using filter_stubs, 
 7. filters out trajectories of particles that move a distance below some threshold (currently 4 microns), and 
 8. saves the results (below an 'error' lines that prevents accidentally saving the results if you run the whole notebook.

Note that displacement_um will overestimate the maximum extents of the particle trajectory because it obtains the extreme x and y independently, not as an (x,y) pair from the same frame.

(original file name: 2015-09-15 movie150902,17 particles in droplet _ save trajectories, minimal human intervention, improved_2016-02-10.ipynb)

### backgrounding_color_avi_movie_examples.ipynb
This notebook shows some examples of how to work with a color avi file in python. If you run into errors opening an avi file using pims, make sure to run the setup script, available at https://github.com/vivarose/setup_script.

(original file name: 2015-02-20 & 06-25 & 07-01 Background subtracting color -- red swimmers and blue tracers.ipynb)
