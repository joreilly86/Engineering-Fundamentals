import matplotlib.pyplot as plt

from symbeam import beam


test_beam = beam(6, x0=0)
test_beam.add_support(0, "fixed")
test_beam.add_support(2, "hinge")
test_beam.add_support(4, "roller")
test_beam.add_distributed_load(0, 4, "-5/4 * x")
test_beam.add_distributed_load(4, 6, -5)
test_beam.add_point_moment(4, 20)
test_beam.solve()
fig, ax = test_beam.plot()

plt.savefig(__file__.split(".py")[0] + ".svg")