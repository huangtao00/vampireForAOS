#this is a good demo to show how to use two axis in one  figure 2015 12 3
import matplotlib.pyplot as plt

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

fig, ax = plt.subplots()
fig.subplots_adjust(right=0.75)

par1 = ax.twinx()
#par2 = ax.twinx()

# Offset the right spine of par2.  The ticks and label have already been
# placed on the right by twinx above.
#par2.spines["right"].set_position(("axes", 1.2))
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
#make_patch_spines_invisible(par2)
# Second, show the right spine.
#par2.spines["right"].set_visible(True)

p1, = ax.plot([0, 1, 2], [0, 1, 2], "b-", label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], "r-", label="Temperature")
#p3, = par2.plot([0, 1, 2], [50, 30, 15], "g-", label="Velocity")

ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
par1.set_ylim(0, 4)
#par2.set_ylim(1, 65)

ax.set_xlabel("Distance")
ax.set_ylabel("Density")
par1.set_ylabel("Temperature")
#par2.set_ylabel("Velocity")

ax.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
#par2.yaxis.label.set_color(p3.get_color())

tkw = dict(size=4, width=1.5)
ax.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
#par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
ax.tick_params(axis='x', **tkw)

#lines = [p1, p2, p3]
lines = [p1, p2]
ax.legend(lines, [l.get_label() for l in lines])

plt.show()