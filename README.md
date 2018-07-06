# using_trackpy
I have used trackpy with HDF5 xyt hyperstack movies and with avi movies. Here are my ipython notebooks.

### using_ipyparallel_with_trackpy.ipynb
Using ipyparallel is recommended in the trackpy walkthrough for speeding up particle tracking. Here I have implemented it.
This notebook 
 1. opens a color avi movie in greyscale,
 4. imports ipyparallel for parallel processing, (You will need to start the appropriate number of engines either in the clusters tab or from the command line.)
 5. locates dark spots in the movie with trackpy and parallel processing,
 6. filters out trajectories of few frames using trackpy.filter_stubs.

(original file name: 2016-02-11_track_mov_2016-01-26_02_60x1.0_Hem_swim_w_violet_100%--2016-02-26,ipyparallel.ipynb)

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

### MSD_standard_deviation.ipynb
This notebook explores the standard deviation in the ensemble mean square displacement.

### backgrounding_color_avi_movie_examples.ipynb
This notebook shows some examples of how to work with a color avi file in python. If you run into errors opening an avi file using pims, make sure to run the setup script, available at https://github.com/vivarose/setup_script.

(original file name: 2015-02-20 & 06-25 & 07-01 Background subtracting color -- red swimmers and blue tracers.ipynb)

### Rotational_drift_subtract_entire_movie.ipynb
An implementation of rotational drift subtraction. Particles that are tracked are assumed to have correlated three-dimensional motion; this removes that average motion.

(original file name: 2016-08-04_Rotational_drift_subtract_entire_movie.ipynb)
