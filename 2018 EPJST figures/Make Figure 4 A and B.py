## Hi Zach, put this code in a cell at the end of the python notebook
# drift subtracted vs non drift subtracted janus particles.ipynb
# Then send me the four files (two pdfs and two png files) that it creates.

import seaborn as sns
sns.set(style='ticks')
sns.set_context('paper')
#sns.set_palette(sns.husl_palette())

# Big font
#font = {'size'   : 9}
#plt.rc('font', **font)

plt.subplot(1,2, 2)
#plt.figsize=(8,10)
plt.rcParams.update({'legend.handlelength': 0})
plt.rcParams.update({'axes.titlesize' : 14 })
plt.rcParams.update({'xtick.major.size': 3 ,
                     'ytick.major.size': 3,
#                     'axes.linewidth' : 10,
                     'xtick.minor.size': 2 ,
                     'ytick.minor.size': 2})

emt1.plot(style = 'g.',label = 'not drift subtracted')
emtm.plot(style = 'b.', label = 'drift subtracted')
emtmc.plot(style = 'r.',label = 'control')
fig1 = plt.gcf()
axB = plt.gca()
#plt.title('Tracer 3% $H_2O_2$ vs Tracers no $H_2O_2$ janus particles')
#plt.title('Janus')
plt.title('B', loc='left')
plt.title('Janus')
plt.yscale('log')
plt.xscale('log')
#plt.xlabel('lag time $\Delta t$ [s]')
#plt.ylabel(r'$\langle \Delta r^2 \rangle$ [$\mu$m$^2$]')
plt.ylabel(r'$\langle \Delta r^2 \rangle$ ($\mathrm{\mu}$m$^2$)')
plt.xlabel(r'$\Delta{}t$ (s)')
axB.yaxis.labelpad = -1 
plt.legend(loc='upper left' , prop={'size': 8},markerscale= 1.5)
#plt.ylim(ymax=100)
plt.xlim(xmax=10)

plt.subplot(1,2, 1)
emt1.plot(style = 'g.',label = 'not drift subtracted')
emtm.plot(style = 'b.', label = 'drift subtracted')
emtmc.plot(style = 'r.',label = 'control')
#plt.title('Tracer 3% $H_2O_2$ vs Tracers no $H_2O_2$ tracer particles')
#plt.title('Tracers')
plt.title('A', loc='left')
plt.title('Janus')

plt.yscale('linear')
plt.xscale('linear')
#plt.xlabel('lag time $\Delta t$ [s]')
#plt.ylabel(r'$\langle \Delta r^2 \rangle$ [$\mu$m$^2$]')
plt.ylabel(r'$\langle \Delta r^2 \rangle$ ($\mathrm{\mu}$m$^2$)')
plt.xlabel(r'$\Delta{}t$ (s)')
plt.xticks(np.arange(0,10, step=2)) # order I call this matters
#plt.ylim(ymin=0,ymax=25)
#plt.xlim(xmin=0)
#plt.text(.5,0,'Tracer',transform=ax.transAxes, ha='right')
axA = plt.gca()

plt.legend(loc='upper left' , prop={'size': 8},markerscale= 1.5)

print("Tracer 3% $H_2O_2$ vs Tracers no $H_2O_2$ janus particles")

thisheight=2.3
thiswidth=4.5
fig1.set_figheight(thisheight)
fig1.set_figwidth(thiswidth)

axA.tick_params(which='both', pad=3)
axB.tick_params( which='both', pad=2)
#ax.tick_params(width=.18, which='minor')

plt.tight_layout()
#plt.show()

try:
    plt.savefig('Tracer 3% H2O2 vs Tracers no H2O2 Janus particles.pdf', 
                bbox_inches='tight', figsize=(thiswidth, thisheight))
    print('pdf saved')
    plt.savefig('Tracer 3% H2O2 vs Tracers no H2O2 Janus particles.png', 
                bbox_inches='tight', dpi=600, figsize=(thiswidth, thisheight))
except IOError:
    print('Close the pdf file so I can overwrite it.')
    

sns.despine(offset=6, trim=False); 

plt.tight_layout()


try:
    plt.savefig('Tracer 3% H2O2 vs Tracers no H2O2 Janus particles despine.pdf', 
                bbox_inches='tight', figsize=(thiswidth, thisheight))
    print('pdf saved')
    plt.savefig('Tracer 3% H2O2 vs Tracers no H2O2 Janus particles despine.png', 
                bbox_inches='tight', dpi=600, figsize=(thiswidth, thisheight))
except IOError:
    print('Close the pdf file so I can overwrite it.')
    
plt.show()
